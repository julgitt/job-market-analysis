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
