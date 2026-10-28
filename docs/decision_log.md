# Rejestr decyzji projektowych

## Wybór źródła danych

**Decyzja:**  
Wybór API Arbeitnow jako głównego źródła danych o ofertach pracy.

**Rozważane alternatywy:**
- **Arbeitnow Job Board API** – umożliwia pobieranie ofert pracy za pośrednictwem API.
- **Stack Overflow Developer Survey** – zbiór danych dotyczących programistów, ich doświadczenia, technologii i sytuacji zawodowej. 
  Dane są udostępniane w formie corocznego badania.

**Uzasadnienie:**
API Arbeitnow wybrano ze względu na zgodność z celem projektu, którym jest analiza ofert pracy.
Umożliwia ono pobieranie dynamicznie zmieniających się danych ze źródła.

Stack Overflow Developer Survey rozważano ze względu na dużą liczbę odpowiedzi i globalny charakter badania.
Odrzucono je jako główne źródło, ponieważ dane są publikowane okresowo, zwykle raz w roku, i mają postać statycznego zbioru.
Lepiej nadają się do analizy opinii i charakterystyki osób pracujących w branży niż do bieżącego monitorowania ofert pracy.

**Konsekwencje decyzji:**
- Możliwość zautomatyzowania pobierania danych.
- Konieczność obsługi błędów komunikacji z API.
- Zakres analiz będzie ograniczony do informacji udostępnianych przez wybrane API.
- Wyniki będą zależne od aktualności, kompletności i jakości danych źródłowych.
- 
## Wybór sposobu przechowywania danych (Pliki JSON vs. Baza danych)

**Decyzja:**  
Wykorzystanie plików JSON rozdzielonych na warstwy `raw`, `clean` i `serving` zamiast bazy danych.

**Uzasadnienie:**
API Arbeitnow zwraca dane w formacie JSON, zatem przechowując je w tej samej formie, unikamy konieczności mapowania danych.
Nie ma też potrzeby konfigurowania zewnętrznej bazy danych, dzięki czemu cały setup jest bardzo prosty do odtworzenia.
Przy obecnym zakresie projektu oraz skali danych zapis do plików JSON jest w pełni wystarczający.

**Konsekwencje decyzji:**
- Brak konieczności instalacji i konfiguracji serwera bazy danych. Środowisko projektu jest proste do odtworzenia.
- Przejrzystość danych - łatwy podgląd plików na każdym etapie potoku(`raw`, `clean` i `serving`).
- Przy ewentualnym wzroście wolumenu danych w przyszłości konieczne byłaby przejście na dedykowaną bazę danych.