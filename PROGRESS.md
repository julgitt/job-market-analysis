## Tydzień 1: 11.10.2026

- Określono cel i zakres projektu.
- Wybrano API Arbeitnow jako źródło danych o ofertach pracy.
- Przygotowano początkową strukturę repozytorium.
- Utworzono katalogi `data/raw/`, `data/clean/` i `data/service/`.
- Przygotowano strukturę kodu z podziałem na warstwy `application`, `domain` i `infrastructure` zgodnie z architekturą DDD.
- Utworzono konfigurację projektu w plikach `.env` i `.env.example`.
- Rozpoczęto dokumentację projektu w `docs/project_context.md`.
- Utworzono rejestr najważniejszych decyzji projektowych `docs/decision_log.md`.
- Przygotowano podstawowe moduły klienta API, modelu oferty pracy i repozytorium JSON.
- Przygotowano plik `README.md` z opisem projektu i instrukcją instalacji.

## Tydzień 2: 15.10.2026

- Utworzenie potoku oczyszczającego surowe dane z API (budowa warstwy Silver w `clean_job_offers.py`).
- Zaimplementowanie logiki walidacji w pliku `job_offer_quality.py`, która weryfikuje kompletność, typy danych oraz wymagane pola w ofertach pracy. 
- Wdrożenie funkcji czyszczącej znaki HTML z tekstów ofert.
- Napisanie i uruchomienie zautomatyzowanych testów jakości danych w pytest (test_job_offer_quality.py).
- Zbudowanie pierwszej wersji interaktywnego dashboardu analitycznego za pomocą biblioteki Streamlit (`app.py`).

## Tydzień 3: 21.10.2026
- Wdrożenie warstwy Gold (Serving).
- Stworzenie skryptu `build_serving_data.py`, który generuje gotowe, zagregowane modele JSON dla lokalizacji, tagów i typów umów.
- Rozbudowa czyszczenia danych o scentralizowaną funkcję usuwającą podwójne ukośniki z list i ciągów znaków zgodnie z zasadą DRY.
- Zoptymalizowanie dashboardu poprzez podpięcie go wyłącznie pod gotowe dane z warstwy Gold, odciążając aplikację z ciężkich transformacji (grupowanie, explode).