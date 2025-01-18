from flask import Flask, render_template, request
from tensorflow import keras
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
import numpy as np

app = Flask(__name__)

# Wczytanie modeli
models = {
    'klasyfikator_gatunku_piwa': keras.models.load_model('models/model_klasyfikacji_piwa.h5'),
    'klasyfikator_gatunku_piwa_top20': keras.models.load_model('models/model_klasyfikacji_20_styli_piwa.h5'),
    'regresja_alkohol_piwa': keras.models.load_model('models/model_regresji_alkoholu.h5'),
    'regresja_kolor_piwa': keras.models.load_model('models/model_regresji_koloru_piwa.h5')
}

# Wczytanie danych do normalizacji
data = pd.read_csv('data.csv')
numeric_columns_classification = ['Size(L)', 'OG', 'FG', 'ABV', 'IBU', 'Color', 'BoilSize', 'BoilTime', 'BoilGravity', 'Efficiency']
numeric_columns_regression_alcohol = ['Size(L)', 'OG', 'FG', 'IBU', 'Color', 'BoilSize', 'BoilTime', 'BoilGravity', 'Efficiency']
numeric_columns_regression_color = ['Size(L)', 'OG', 'FG', 'IBU', 'ABV', 'BoilSize', 'BoilTime', 'BoilGravity', 'Efficiency']

# Upewnij się, że wszystkie kolumny są numeryczne
data[numeric_columns_classification] = data[numeric_columns_classification].apply(pd.to_numeric, errors='coerce')
data[numeric_columns_regression_alcohol] = data[numeric_columns_regression_alcohol].apply(pd.to_numeric, errors='coerce')
data[numeric_columns_regression_color] = data[numeric_columns_regression_color].apply(pd.to_numeric, errors='coerce')

X_classification = data[numeric_columns_classification].copy().fillna(data[numeric_columns_classification].mean())
X_regression_alcohol = data[numeric_columns_regression_alcohol].copy().fillna(data[numeric_columns_regression_alcohol].mean())
X_regression_color = data[numeric_columns_regression_color].copy().fillna(data[numeric_columns_regression_color].mean())

scaler_classification = StandardScaler().fit(X_classification)
scaler_regression_alcohol = StandardScaler().fit(X_regression_alcohol)
scaler_regression_color = StandardScaler().fit(X_regression_color)

# Label Encoder dla klasyfikatorów
label_encoder = LabelEncoder().fit(data['Style'])

# Przykładowe dane dla gatunków piwa
piwa = {
    'IPA': {'Size(L)': 20.0, 'OG': 1.065, 'FG': 1.015, 'IBU': 60, 'ABV': 6.5, 'Color': 10, 'BoilSize': 25.0, 'BoilTime': 60, 'BoilGravity': 1.060, 'Efficiency': 75},
    'Stout': {'Size(L)': 20.0, 'OG': 1.075, 'FG': 1.020, 'IBU': 40, 'ABV': 7.0, 'Color': 40, 'BoilSize': 25.0, 'BoilTime': 60, 'BoilGravity': 1.070, 'Efficiency': 75},
    'Pilsner': {'Size(L)': 20.0, 'OG': 1.050, 'FG': 1.010, 'IBU': 30, 'ABV': 5.0, 'Color': 5, 'BoilSize': 25.0, 'BoilTime': 60, 'BoilGravity': 1.045, 'Efficiency': 75},
    'Wheat': {'Size(L)': 20.0, 'OG': 1.055, 'FG': 1.012, 'IBU': 20, 'ABV': 5.5, 'Color': 5, 'BoilSize': 25.0, 'BoilTime': 60, 'BoilGravity': 1.050, 'Efficiency': 75},
    'APA': {'Size(L)': 20.0, 'OG': 1.050, 'FG': 1.010, 'IBU': 35, 'ABV': 5.5, 'Color': 10, 'BoilSize': 25.0, 'BoilTime': 60, 'BoilGravity': 1.045, 'Efficiency': 75},
    'Barleywine': {'Size(L)': 20.0, 'OG': 1.100, 'FG': 1.025, 'IBU': 80, 'ABV': 10.0, 'Color': 20, 'BoilSize': 25.0, 'BoilTime': 90, 'BoilGravity': 1.095, 'Efficiency': 75},
    'Saison': {'Size(L)': 20.0, 'OG': 1.060, 'FG': 1.008, 'IBU': 25, 'ABV': 6.0, 'Color': 10, 'BoilSize': 25.0, 'BoilTime': 60, 'BoilGravity': 1.055, 'Efficiency': 75},
    'Porter': {'Size(L)': 20.0, 'OG': 1.065, 'FG': 1.018, 'IBU': 35, 'ABV': 6.5, 'Color': 30, 'BoilSize': 25.0, 'BoilTime': 60, 'BoilGravity': 1.060, 'Efficiency': 75}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model/<model_name>', methods=['GET', 'POST'])
def model(model_name):
    if request.method == 'POST':
        if model_name in ['klasyfikator_gatunku_piwa', 'klasyfikator_gatunku_piwa_top20']:
            input_data = [float(request.form[col]) for col in numeric_columns_classification]
            input_data_scaled = scaler_classification.transform([input_data])
            model = models[model_name]
            prediction = model.predict(input_data_scaled)
            predicted_class = label_encoder.inverse_transform([np.argmax(prediction)])[0]
            result = f'Przewidywany gatunek piwa: {predicted_class}'
        elif model_name == 'regresja_alkohol_piwa':
            input_data = [float(request.form[col]) for col in numeric_columns_regression_alcohol]
            input_data_scaled = scaler_regression_alcohol.transform([input_data])
            model = models[model_name]
            prediction = model.predict(input_data_scaled)[0][0]
            result = f'Przewidywana zawartość alkoholu: {prediction:.2f}%'
        elif model_name == 'regresja_kolor_piwa':
            input_data = [float(request.form[col]) for col in numeric_columns_regression_color]
            input_data_scaled = scaler_regression_color.transform([input_data])
            model = models[model_name]
            prediction = model.predict(input_data_scaled)[0][0]
            result = f'Przewidywany kolor piwa: {prediction:.2f}'
        return render_template('model.html', model_name=model_name, result=result, input_data=request.form, piwa=piwa)
    return render_template('model.html', model_name=model_name, result=None, input_data=None, piwa=piwa)

if __name__ == '__main__':
    app.run(debug=True)