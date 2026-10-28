# Słownik Danych

Dokument opisuje strukturę danych w poszczególnych warstwach potoku (`raw`, `clean`, `serving`).

---

## 1. Warstwa Raw (`data/raw/`)
Surowe dane z API Arbeitnow w formacie JSON bez żadnych modyfikacji.
* **Źródło:** `https://www.arbeitnow.com/api/job-board-api`

### Struktura pól surowych (kluczowe pola):
| Pole | Typ danych | Opis                                                                   |
| :--- | :--- |:-----------------------------------------------------------------------------|
| `slug` | String | Unikalny identyfikator oferty w serwisie Arbeitnow                       |
| `company_name` | String | Nazwa firmy publikującej ogłoszenie                              |
| `title` | String | Tytuł stanowiska                                                        |
| `description` | String | Treść ogłoszenia w formacie HTML                                  |
| `remote` | Boolean | Czy praca jest zdalna (`true`/`false`)                                |
| `url` | String | Bezpośredni link do ogłoszenia                                            |
| `tags` | List[String] | Lista słów kluczowych / technologii powiązanych z ofertą           |
| `job_types` | List[String] | Typ zatrudnienia (np. `full_time`, `contract`)                |
| `location` | String | Nazwa lokalizacji wykonywania pracy (ewentualnie `remote` dla pracy zdalnej) |
| `created_at` | Integer | Czas utworzenia oferty w formacie Timestamp (Unix)                |

---

## 2. Warstwa Clean / Silver (`data/clean/`)
Oczyszczone i zwalidowane dane o ofertach pracy. 
Dane zawierają usunięty znacznik HTML z opisów, poprawione ukośniki (`\/` -> `/`), usunięte duplikaty po kluczu `slug`
oraz zwalidowane typy danych.

### Struktura pól:
| Pole | Typ danych | Wymagane | Opis                                                         |
| :--- | :--- | :--- |:-----------------------------------------------------------------------|
| `slug` | String | Tak | Oczyszczony identyfikator (bez białych znaków)                      |
| `company_name` | String | Tak | Oczyszczona nazwa firmy                                     |
| `title` | String | Tak | Oczyszczony tytuł                                                  |
| `description` | String | Nie | Czysty tekst ogłoszenia z usuniętymi znacznikami HTML i nowymi liniami |
| `remote` | Boolean | Tak | Czy praca jest zdalna                                            |
| `url` | String | Tak | Zwalidowany adres URL (musi zaczynać się od `http://` lub `https://`) |
| `tags` | List[String] | Tak | Znormalizowana lista słów kluczowych                          |
| `job_types` | List[String] | Tak | Typ zatrudnienia                                         |
| `location` | String | Nie | Znormalizowana nazwa lokalizacji                                |
| `created_at` | Integer | Tak | Poprawny znacznik czasu powstania oferty                     |

---

## 3. Warstwa Serving / Gold (`data/serving/`)
Agregaty oraz tabele przygotowane bezpośrednio pod szybkie odczyty i wizualizacje w aplikacji Streamlit (`src/app.py`).

### 3.1 `serving_job_offers.json`
Tabela wyciągnięta z warstwy oczyszczonej zawierająca tylko kolumny prezentowane w interfejsie użytkownika.
* **Kolumny:** `title`, `company_name`, `location`, `remote`, `job_types`, `tags`

### 3.2 `serving_location_stats.json`
Zestawienie liczby ofert przypisanych do poszczególnych lokalizacji.

| Kolumna | Typ danych | Opis |
| :--- | :--- | :--- |
| `location` | String | Nazwa lokalizacji |
| `count` | Integer | Zagregowana liczba ofert pracy |

### 3.3 `serving_tags_summary.json`
Zagregowana lista najpopularniejszych słów kluczowych i technologii.

| Kolumna | Typ danych | Opis |
| :--- | :--- | :--- |
| `tag` | String | Nazwa technologii / słowa kluczowe |
| `count` | Integer | Liczba ogłoszeń, w których pojawił się dany tag |

### 3.4 `serving_job_types_summary.json`
Podsumowanie popularności typów zatrudnienia.

| Kolumna | Typ danych | Opis |
| :--- | :--- | :--- |
| `job_type` | String | Rodzaj umowy (np. full_time, part_time) |
| `count` | Integer | Łączna liczba ogłoszeń |