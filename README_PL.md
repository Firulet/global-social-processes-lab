# Global Social Processes: SITT and Cialdini — interactive laboratory

Samodzielna, dwujęzyczna aplikacja Streamlit do teoretycznej analizy wpływu społecznego na podstawie artykułu **Unraveling SITT: Social Influence Technique Taxonomy and Detection with LLMs** (2025).

## Co zawiera
- 6 klasycznych zasad Cialdiniego (z objaśnieniami i autorskimi przykładami)
- 9 szerokich kategorii SITT (według tabeli 1 publikacji)
- 24 nowe, autorskie komunikaty do kodowania (nie są oryginalnymi dialogami SITT)
- Wieloetykietowe kodowanie, uzasadnianie decyzji i pomocniczy wskaźnik Jaccarda
- Symulator zmiany strategii przekazu (fikcyjne teksty, **bez** pomiaru skuteczności)
- Globalne procesy: migracje, klimat, komunikacja platformowa, aktywizm
- Wykresy zagregowanych wyników z publikacji oraz porównanie historycznych wyników modeli
- Debaty i projekt badawczy

## Instalacja
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Publikacja w Streamlit Community Cloud
1. Na GitHubie utwórz **osobne** repozytorium, np. `global-social-processes-lab`.
2. Wgraj `app.py`, `content.py`, `requirements.txt` i `.streamlit/config.toml` (zachowaj ścieżkę katalogu).
3. W https://share.streamlit.io wybierz Create app → istniejące repozytorium, gałąź `main`, główny plik `app.py`.
4. Kliknij Deploy. W tej aplikacji nie ma Google Sheets ani logowania.

## Co pochodzi z badań, a co jest symulacją?
**Dane empiryczne z artykułu:** 746 dialogów, 9 kategorii, 58 technik, liczebności kategorii z Figure 1, wyniki F1 modeli dla polskich tekstów z Table 3. **Nie udostępniamy pełnego korpusu w aplikacji.**

**Autorskie materiały dydaktyczne:** wszystkie 24 dialogi do kodowania, reguły pomocniczego klucza, scenariusze dyskusji i generator przekształconych przekazów. Nie stanowią anotacji eksperckich ani potwierdzonej skuteczności technik.

## Ważne ograniczenia
- Cialdini (sześć klasycznych zasad) i SITT (dziewięć kategorii) to różne schematy.
- Dopasowanie tekstu do kategorii nie dowodzi, że nadawca zamierzał manipulować, że odbiorca uległ wpływowi ani że tekst narusza normy etyczne.
- Porównanie Jaccarda w aplikacji mierzy zgodność zestawu wyborów z **autorskim kluczem dydaktycznym**, nie zgodność między anotatorami.
- Wyniki modeli dotyczą wersji zbadanych w publikacji, a nie najnowszych modeli.
- Wpisy w polach tekstowych pozostają w bieżącej sesji Streamlit. Aplikacja nie zapisuje ich trwale.

Źródło: https://arxiv.org/abs/2506.00061 (Mieleszczenko-Kowszewicz i in., 2025). Zbiór opisany w artykule: https://github.com/social-influence/sitt-dataset/
