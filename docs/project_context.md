# Kontekst projektu

## Opis problemu
Osoby szukające pracy są zmuszone do analizowania wielu ogłoszeń, aby znaleźć oferty dopasowane do swoich potrzeb.
Celem projektu jest stworzenie potoku danych, który automatycznie pobiera oferty pracy z API Arbeitnow,
przetwarza je i udostępnia w aplikacji analitycznej.
Aplikacja umożliwi filtrowanie i sortowanie ofert oraz analizowanie trendów na rynku pracy.

## Odbiorcy

Głównymi odbiorcami są osoby poszukujące pracy, w tym studenci szukający praktyk.
Potencjalnymi odbiorcami są również biura karier oraz doradcy zawodowi. 
Aplikacja ma ułatwiać wyszukiwanie ofert i wspierać podejmowanie decyzji dotyczących kariery zawodowej.

## Perspektywa biznesowa

Projekt ułatwia analizowanie ofert pracy, porównywanie dostępnych stanowisk i rozpoznawanie trendów. 

Jego wartość można oceniać na podstawie liczby przeanalizowanych ofert,
czasu potrzebnego na znalezienie odpowiednich ogłoszeń oraz użyteczności prezentowanych statystyk. 

Koszty utrzymania powinny być niewielkie, ponieważ projekt korzysta z publicznego API i narzędzi programistycznych,
a jego uruchomienie nie wymaga rozbudowanej infrastruktury.

## Perspektywa dziedzinowa
Dane dotyczą ofert pracy, pracodawców, lokalizacji, rodzajów zatrudnienia, możliwości pracy zdalnej i wymaganych umiejętności.
Ogłoszenia mogą zawierać niekompletne lub niespójne informacje, dlatego wymagają walidacji i czyszczenia.
Analizy muszą uwzględniać, że dostępne oferty nie reprezentują całego rynku pracy, a wyniki zależą od danych udostępnianych przez API.

## Perspektywa techniczna
Projekt wykorzystuje API Arbeitnow jako źródło danych oraz architekturę warstwową: raw, clean i serving.
Rozdzielenie pobierania, przetwarzania i udostępniania danych ułatwia skalowanie projektu oraz testowanie aplikacji.
Jakość zapewniają automatyczne testy danych, a powtarzalność dokumentacja. 
Za deklaracja zależności i wersjonowanie kodu odpowiada Git.
Przy większym wolumenie należałoby rozważyć automatyczne harmonogramowanie zadań. 

## Perspektywa prawna i etyczna
Dane będą pozyskiwane z API Arbeitnow, z uwzględnieniem warunków korzystania z serwisu i ewentualnych ograniczeń licencyjnych.
Ogłoszenia mogą zawierać dane osobowe, np. dane kontaktowe rekruterów, dlatego należy ograniczyć przetwarzanie do informacji potrzebnych w projekcie.
Za treść ogłoszeń odpowiadają ich autorzy, a jakość analiz zależy od jakości danych źródłowych.
Wyniki nie opisują całego rynek pracy, lecz jego wycinek, a analizy w aplikacji nie gwarantują znalezienie zatrudnienia.
