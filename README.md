# 🍺 Project B.E.E.R. 🍺

## Opis Projektu 📋

Projekt B.E.E.R. (Badanie Estetyki i Etylometrii Roztworów) zawiera kilka modeli uczenia maszynowego do analizy danych piwa. Modele te obejmują regresję zawartości alkoholu, regresję koloru piwa oraz klasyfikację gatunków piwa. Poniżej znajduje się szczegółowy opis każdego z modeli oraz zbioru danych używanego w projekcie.

## Struktura Projektu 📂

```
Project-B.E.E.R/
├── models/
│   ├── model_klasyfikacji_20_styli_piwa.h5
│   ├── model_klasyfikacji_piwa.h5
│   ├── model_regresji_alkoholu.h5
│   ├── model_regresji_koloru_piwa.h5
│   ├── tuned_model_klasyfikacji_20_styli_piwa.h5
│   ├── tuned_model_klasyfikacji_piwa.h5
│   ├── tuned_model_regresji_alkoholu.h5
│   └── tuned_model_regresji_koloru_piwa.h5
├── notebooks/
│   ├── analiza_danych_piwa.ipynb
│   ├── klasyfikator_gatunku_piwa.ipynb 
│   ├── klasyfikator_gatunku_piwa_top20.ipynb
│   ├── regresja_alkohol_piwa.ipynb
│   ├── regresja_kolor_piwa.ipynb
│   ├── tensorboard.ipynb
│   ├── tuning_regresji_koloru_piwa.ipynb
│   ├── tuning_regresji_alkoholu.ipynb
│   ├── tuning_klasyfikacja_styli_piwa.ipynb
│   ├── tuning_klasyfikacja_20_styli_piwa.ipynb
│   └── logs/
│       ├── fit
│           ├── klasyfikacja_20_styli_piwa/
│           ├── klasyfikacja_styli_piwa/
│           ├── regresja_alkoholu/
│           └── regresja_koloru_piwa/
├── templates/
│   ├── index.html
│   └── model.html
├── data.csv
├── app.py
├── requirements.txt
└── README.md 
```

## Zbiór Danych 📊

Zbiór danych używany w projekcie znajduje się w pliku `data.csv`. Zawiera on informacje o różnych piwach, takie jak:

- `BeerID`: Unikalny identyfikator piwa.
- `Name`: Nazwa piwa.
- `URL`: Link do przepisu na piwo.
- `Style`: Styl piwa.
- `StyleID`: Unikalny identyfikator stylu piwa.
- `Size(L)`: Objętość piwa w litrach.
- `OG` (Original Gravity): Początkowa gęstość brzeczki.
- `FG` (Final Gravity): Końcowa gęstość brzeczki.
- `ABV` (Alcohol By Volume): Zawartość alkoholu w piwie.
- `IBU` (International Bitterness Units): Miara goryczki piwa.
- `Color`: Kolor piwa w skali SRM.
- `BoilSize`: Objętość brzeczki przed gotowaniem.
- `BoilTime`: Czas gotowania brzeczki.
- `BoilGravity`: Gęstość brzeczki przed gotowaniem.
- `Efficiency`: Wydajność procesu warzenia.
- `MashThickness`: Gęstość zacieru.
- `SugarScale`: Skala cukru (np. Specific Gravity, Brix).
- `BrewMethod`: Metoda warzenia (np. All Grain, Extract).
- `PitchRate`: Ilość drożdży dodanych do brzeczki.
- `PrimaryTemp`: Temperatura fermentacji.
- `PrimingMethod`: Metoda refermentacji.
- `PrimingAmount`: Ilość cukru do refermentacji.
- `UserId`: Unikalny identyfikator użytkownika.

### Przykładowe dane:

| BeerID | Name                          | URL                                                         | Style                                | StyleID | Size(L) | OG    | FG    | ABV  | IBU   | Color | BoilSize | BoilTime | BoilGravity | Efficiency | MashThickness | SugarScale       | BrewMethod | PitchRate | PrimaryTemp | PrimingMethod | PrimingAmount | UserId |
|--------|-------------------------------|-------------------------------------------------------------|--------------------------------------|---------|---------|-------|-------|------|-------|-------|----------|----------|-------------|------------|---------------|------------------|-------------|-----------|-------------|----------------|----------------|--------|
| 1      | Vanilla Cream Ale             | /homebrew/recipe/view/1633/vanilla-cream-ale                | Cream Ale                            | 45      | 21.77   | 1.055 | 1.013 | 5.48 | 17.65 | 4.83  | 28.39    | 75       | 1.038       | 70         | N/A           | Specific Gravity | All Grain   | N/A       | 17.78       | corn sugar     | 4.5 oz         | 116    |
| 2      | Southern Tier Pumking clone   | /homebrew/recipe/view/16367/southern-tier-pumking-clone     | Holiday/Winter Special Spiced Beer   | 85      | 20.82   | 1.083 | 1.021 | 8.16 | 60.65 | 15.64 | 24.61    | 60       | 1.07        | 70         | N/A           | Specific Gravity | All Grain   | N/A       | N/A         | N/A            | N/A            | 955    |
| 3      | Zombie Dust Clone - EXTRACT   | /homebrew/recipe/view/5920/zombie-dust-clone-extract        | American IPA                         | 7       | 18.93   | 1.063 | 1.018 | 5.91 | 59.25 | 8.98  | 22.71    | 60       | N/A         | 70         | N/A           | Specific Gravity | Extract     | N/A       | N/A         | N/A            | N/A            |        |
| 4      | Zombie Dust Clone - ALL GRAIN | /homebrew/recipe/view/5916/zombie-dust-clone-all-grain      | American IPA                         | 7       | 22.71   | 1.061 | 1.017 | 5.8  | 54.48 | 8.5   | 26.5     | 60       | N/A         | 70         | N/A           | Specific Gravity | All Grain   | N/A       | N/A         | N/A            | N/A            |        |
| 5      | Bakke Brygg Belgisk Blonde 50 l | /homebrew/recipe/view/89534/bakke-brygg-belgisk-blonde-50-l | Belgian Blond Ale                    | 20      | 50      | 1.06  | 1.01  | 6.48 | 17.84 | 4.57  | 60       | 90       | 1.05        | 72         | N/A           | Specific Gravity | All Grain   | N/A       | 19          | Sukkerlake     | 6-7 g sukker/l | 18325  |

Zbiór danych zawiera informacje o różnych stylach piwa, które są używane do trenowania modeli regresji i klasyfikacji w projekcie.

## Modele 🧠

### 1. Regresja Zawartości Alkoholu 🍻

Model regresji zawartości alkoholu przewiduje zawartość alkoholu w piwie na podstawie różnych parametrów warzenia. Model ten jest zaimplementowany w notebooku `regresja_alkohol_piwa.ipynb`.

#### Kroki:

1. **Importowanie Bibliotek**: Import niezbędnych bibliotek, takich jak TensorFlow, Keras, NumPy, Pandas oraz bibliotek do przetwarzania danych.
2. **Przygotowanie Danych**: Wczytanie danych z pliku CSV, normalizacja danych, podział na zbiór treningowy i testowy.
3. **Utworzenie Modelu**: Utworzenie modelu sieci neuronowej za pomocą Keras.
4. **Kompilacja Modelu**: Kompilacja modelu z optymalizatorem Adam i funkcją straty mean_squared_error.
5. **Trenowanie Modelu**: Trenowanie modelu na danych treningowych.
6. **Testowanie i Ewaluacja**: Ocena modelu na zbiorze testowym, obliczenie średniego błędu kwadratowego, wykres porównujący rzeczywiste i przewidywane wartości.
7. **Zapisywanie Modelu**: Zapisanie wytrenowanego modelu do pliku dla późniejszego wykorzystania.

### 2. Regresja Koloru Piwa 🌈

Model regresji koloru piwa przewiduje kolor piwa na podstawie różnych parametrów warzenia. Model ten jest zaimplementowany w notebooku `regresja_kolor_piwa.ipynb`.

#### Kroki:

1. **Importowanie Bibliotek**: Import niezbędnych bibliotek, takich jak TensorFlow, Keras, NumPy, Pandas oraz bibliotek do przetwarzania danych.
2. **Przygotowanie Danych**: Wczytanie danych z pliku CSV, normalizacja danych, podział na zbiór treningowy i testowy.
3. **Utworzenie Modelu**: Utworzenie modelu sieci neuronowej za pomocą Keras.
4. **Kompilacja Modelu**: Kompilacja modelu z optymalizatorem Adam i funkcją straty mean_squared_error.
5. **Trenowanie Modelu**: Trenowanie modelu na danych treningowych.
6. **Testowanie i Ewaluacja**: Ocena modelu na zbiorze testowym, obliczenie średniego błędu kwadratowego, wykres porównujący rzeczywiste i przewidywane wartości.
7. **Zapisywanie Modelu**: Zapisanie wytrenowanego modelu do pliku dla późniejszego wykorzystania.

### 3. Klasyfikacja Gatunków Piwa 🍺🍻

Model klasyfikacji gatunków piwa przewiduje gatunek piwa na podstawie różnych parametrów warzenia. Model ten jest zaimplementowany w notebookach `klasyfikator_gatunku_piwa.ipynb` oraz `klasyfikator_gatunku_piwa_top20.ipynb`.

#### Kroki:

1. **Importowanie Bibliotek**: Import niezbędnych bibliotek, takich jak TensorFlow, Keras, NumPy, Pandas oraz bibliotek do przetwarzania danych.
2. **Przygotowanie Danych**: Wczytanie danych z pliku CSV, normalizacja danych, podział na zbiór treningowy i testowy.
3. **Utworzenie Modelu**: Utworzenie modelu sieci neuronowej za pomocą Keras.
4. **Kompilacja Modelu**: Kompilacja modelu z optymalizatorem Adam i funkcją straty categorical_crossentropy.
5. **Trenowanie Modelu**: Trenowanie modelu na danych treningowych.
6. **Testowanie i Ewaluacja**: Ocena modelu na zbiorze testowym, generowanie macierzy pomyłek i raportu klasyfikacji.
7. **Zapisywanie Modelu**: Zapisanie wytrenowanego modelu do pliku dla późniejszego wykorzystania.

## Pliki 📂

- `analiza_danych_piwa.ipynb`: Notebook do analizy danych piwa.
- `data.csv`: Plik CSV zawierający dane piwa.
- `klasyfikator_gatunku_piwa_top20.ipynb`: Notebook do klasyfikacji gatunków piwa dla 20 najczęstszych gatunków.
- `klasyfikator_gatunku_piwa.ipynb`: Notebook do klasyfikacji gatunków piwa.
- `logs/fit/klasyfikacja_20_styli_piwa`: Logi z trenowania modelu klasyfikacji 20 stylów piwa.
- `logs/fit/klasyfikacja_styli_piwa`: Logi z trenowania modelu klasyfikacji stylów piwa.
- `logs/fit/regresja_alkoholu`: Logi z trenowania modelu regresji alkoholu.
- `logs/fit/regresja_koloru_piwa`: Logi z trenowania modelu regresji koloru piwa.
- `model_klasyfikacji_20_styli_piwa.h5`: Zapisany model klasyfikacji 20 stylów piwa.
- `model_klasyfikacji_piwa.h5`: Zapisany model klasyfikacji piwa.
- `model_regresji_alkoholu.h5`: Zapisany model regresji zawartości alkoholu.
- `model_regresji_koloru_piwa.h5`: Zapisany model regresji koloru piwa.
- `README.md`: Plik z opisem projektu.
- `regresja_alkohol_piwa.ipynb`: Notebook do regresji zawartości alkoholu.
- `regresja_kolor_piwa.ipynb`: Notebook do regresji koloru piwa.
- `tensorboard.ipynb`: Notebook do wizualizacji procesu uczenia modeli w TensorBoard.
- `tuned_model_klasyfikacji_20_styli_piwa.h5`: Dostrojony model klasyfikacji 20 stylów piwa
- `tuned_model_klasyfikacji_piwa.h5`: Dostrojony model klasyfikacji piwa
- `tuned_model_regresji_alkoholu.h5`: Dostrojony model regresji alkoholu  
- `tuned_model_regresji_koloru_piwa.h5`: Dostrojony model regresji koloru piwa
- `tuning_regresji_koloru_piwa.ipynb`: Notebook do tuningu modelu regresji koloru piwa.
- `tuning_regresji_alkoholu.ipynb`: Notebook do tuningu modelu regresji zawartości alkoholu.
- `tuning_klasyfikacja_styli_piwa.ipynb`: Notebook do tuningu modelu klasyfikacji stylów piwa.
- `tuning_klasyfikacja_20_styli_piwa.ipynb`: Notebook do tuningu modelu klasyfikacji 20 stylów piwa.
- `requirements.txt`: Plik z wymaganiami dotyczącymi bibliotek.
- `app.py`: Główny plik aplikacji Flask.
- `templates/index.html`: Strona główna aplikacji.
- `templates/model.html`: Strona modelu aplikacji.

## Wymagania 📦

Aby uruchomić notebooki i aplikację Flask, należy zainstalować następujące biblioteki:

- TensorFlow
- Keras
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Flask

Można je zainstalować wszystkie wymagane biblioteki za pomocą pliku `requirements.txt`:

```
pip install -r requirements.txt
```

## Uruchamianie 🚀

Aby uruchomić notebooki, należy otworzyć je w Jupyter Notebook lub JupyterLab i wykonać wszystkie komórki kodu. Notebooki zawierają szczegółowe instrukcje dotyczące każdego kroku analizy i trenowania modeli.

Aby uruchomić aplikację Flask, wykonaj następujące kroki:

1. Upewnij się, że masz zainstalowane wszystkie wymagane biblioteki za pomocą pliku `requirements.txt`:

    ```
    pip install -r requirements.txt
    ```

2. Uruchom aplikację Flask:

    ```
    python app.py
    ```

3. Otwórz przeglądarkę internetową i przejdź do adresu `http://127.0.0.1:5000/`.

## Autor 👨‍💻👩‍💻

Projekt został stworzony przez LiCHUTKO, Kailowsky, kolynski.
