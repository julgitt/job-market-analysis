# Job Market Analysis

## Cel projektu

Celem projektu jest automatyczne pobieranie i analizowanie ofert pracy z API Arbeitnow.
Projekt obejmuje potok danych, który pobiera surowe dane, oczyszcza je i przygotowuje do analizy.
Dane będą udostępniane w aplikacji umożliwiającej przeglądanie, filtrowanie i porównywanie ofert pracy 
oraz analizowanie wybranych trendów na rynku pracy.

Źródło danych: [Arbeitnow Job Board API](https://www.arbeitnow.com/api/job-board-api).

## Struktura repozytorium

```text
job-market-analysis/
├── data/
│   ├── raw/
│   ├── clean/
│   └── serving/
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   ├── decision_log.md
│   └── project_context.md
├── src/
│   ├── application/
│   │   ├── fetch_job_offers.py
│   │   ├── clean_job_offers.py
│   │   ├── build_serving_data.py
│   │   └── run_pipeline.py
│   ├── domain/
│   │   ├── job_offer.py
│   │   └── job_offer_quality.py
│   ├── infrastructure/
│   │   ├── job_offers_client.py
│   │   └── json_job_offer_repository.py
│   ├── app.py
│   └── config.py
├── tests/
│   └── test_job_offer_quality.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── PROGRESS.md
└── README.md
```

## Instalacja

### Pobranie repozytorium

Sklonuj repozytorium i przejdź do katalogu projektu:

```bash
git clone https://github.com/julgitt/job-market-analysis
cd job-market-analysis
```

### Utworzenie środowiska wirtualnego

Utwórz środowisko wirtualne:

```bash
python -m venv .venv
```

lub

```bash
python3 -m venv .venv
```

Aktywuj je w systemie Windows:

```bash
.venv\Scripts\activate
```

W systemie Linux lub macOS użyj:

```bash
source .venv/bin/activate
```

### Konfiguracja zmiennych środowiskowych

Utwórz plik `.env` na podstawie szablonu `.env.example`:

W systemie Windows:
```bash
copy .env.example .env
```

W systemie Linux:
```bash
cp .env.example .env
```

### Instalacja zależności

Zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt
```

### Uruchamianie potoku danych

Będąc w głównym katalogu job-market-analysis uruchom potok danych tym poleceniem:

```bash
python -m src.application.run_pipeline
```

### Uruchamianie dashboarda

```bash
streamlit run src/app.py
```
