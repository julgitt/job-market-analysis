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
│   └── service/
├── docs/
│   ├── decision_log.md
│   └── project_context.md
├── src/
│   ├── application/
│   │   ├── __init__.py
│   │   └── fetch_job_offers.py
│   ├── domain/
│   │   └── job_offer.py
│   ├── infrastructure/
│   │   ├── job_offers_client.py
│   │   └── json_job_offer_repository.py
│   ├── app.py
│   └── config.py
├── tests/
├── .env
├── .env.example
├── .gitignore
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

### Instalacja zależności

Zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt
```

### Uruchamianie potoku danych

Będąc w głównym katalogu job-market-analysis uruchom te polecenia:

```bash
python3 -m src.application.fetch_job_offers
python3 -m src.application.clean_job_offers
```

### Uruchamianie dashboarda

```bash
streamlit run src/app.py
```
