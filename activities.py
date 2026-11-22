"""Additional classroom tasks and individual downloads (ephemeral Streamlit session)."""
import json
from datetime import datetime, timezone
from html import escape
import streamlit as st
from dialogues import DIALOGUES

DEBATES = [
("Czy perswazja zawsze jest manipulacją?", "Is persuasion always manipulation?",
 "Jawna zachęta do udziału w kampanii może przekazywać prawdziwe informacje i umożliwiać odmowę.","An open invitation to support a campaign can communicate true evidence and permit refusal.",
 "Ten sam apel może wywierać ukrytą presję, przemilczać koszty lub wykorzystywać strach.","The same appeal can conceal pressure or costs or exploit fear.",
 "Porównanie treści komunikatów, stopnia przejrzystości, możliwości odmowy i wywiady z odbiorcami.","Compare message transparency, opt-out options and interviews with recipients."),
("Czy argument ekspercki zawsze jest wiarygodny?", "Is an expert appeal always reliable?",
 "Eksperckie rekomendacje mogą streszczać wiedzę naukową dostępną odbiorcy.","Expert advice can make scientific knowledge accessible to audiences.",
 "Autorytet bywa poza swoją dziedziną, a cytat może pomijać niepewność badań.","An authority may speak beyond their expertise and quotes may omit uncertainty.",
 "Sprawdzenie specjalizacji, jakości badań, źródeł finansowania i niezależnych replikacji.","Examine expertise, study quality, funding and independent replication."),
("Czy normy społeczne wspierają solidarność?", "Do social norms promote solidarity?",
 "Pokazywanie powszechnego zaangażowania może ułatwić wspólne działanie.","Showing widespread participation may facilitate collective action.",
 "Deklarowana większość może zniechęcać mniejszości i wykluczać odmiennych odbiorców.","Claims about the majority may discourage or exclude minorities.",
 "Badanie reakcji różnych grup oraz porównanie przekazów zawierających i niezawierających norm.","Compare audience groups and messages with versus without norm appeals."),
("Czy apel do lęku może być etyczny?", "Can fear appeals be ethical?",
 "Komunikat o realnym zagrożeniu może pomóc w podjęciu działań ochronnych.","A message about a genuine threat may support protective decisions.",
 "Przesadny strach bez wskazania rozwiązań może szkodzić lub ograniczać refleksję.","Exaggerated fear without actionable guidance may cause harm or undermine reflection.",
 "Weryfikacja skali ryzyka, dostępnych działań i zrozumienia komunikatu przez odbiorców.","Check risk estimates, available actions and audience comprehension."),
("Czy reguły wpływu działają tak samo w różnych krajach?", "Do influence principles work the same across countries?",
 "Niektóre mechanizmy mogą być rozpoznawalne w wielu społeczeństwach.","Some mechanisms may be recognizable across multiple societies.",
 "Język, normy, zaufanie do instytucji i historia mogą zmieniać interpretacje.","Language, norms, institutional trust and history can change interpretations.",
 "Porównywalny schemat próby, tłumaczenie zwrotne i zgodność osób kodujących.","Use comparable samples, back-translation and intercoder checks."),
("Czy AI powinno automatycznie wykrywać manipulację?", "Should AI automatically detect manipulation?",
 "Modele mogą pomóc badaczom przesiewać duże zbiory i wskazywać potencjalne przypadki.","Models may help screen large corpora and flag possible cases.",
 "Błędne etykiety mogą stygmatyzować rozmówców; bez kontekstu łatwo pomylić ostrzeżenie z manipulacją.","False labels can stigmatize speakers; context-free systems may mistake warnings for manipulation.",
 "Wyniki precision/recall, kontrola ekspercka, kontekst i analiza skutków błędów.","Measure precision/recall, expert review, context and consequences of errors.")]

def _lab_state():
    if "student_notes" not in st.session_state:
        st.session_state.student_notes={}
    return st.session_state.student_notes

def _field(name, label, height=100, hint=""):
    vals=_lab_state()
    with st.container():
        value=st.text_area(label, value=vals.get(name,""), height=height, help=hint, key="w_"+name)
    vals[name]=value
    return value

def _select(name, choices, label, format_func=None):
    v=st.multiselect(label,choices,default=_lab_state().get(name,[]),format_func=format_func,key="w_"+name)
    _lab_state()[name]=v
    return v

def render_dialogues(pl, CIALDINI, SITT):
    st.subheader("Pracownia długich dialogów — co naprawdę wpływa na odbiorcę?" if pl else "Long-dialogue studio — what is influencing the audience?")
    st.write("Przeczytaj całą rozmowę, a nie tylko ostatnie zdanie. Wskaż mechanizmy, fragmenty dowodowe, możliwe alternatywne wyjaśnienia. Są to fikcyjne sytuacje dydaktyczne, nie dialogi oryginalnego korpusu SITT." if pl else "Read the entire conversation, not only the last sentence. Identify mechanisms, textual evidence and alternative interpretations. These fictional teaching cases are not dialogues from the original SITT corpus.")
    st.caption("12 dialogów · 6 zasad Cialdiniego · 9 kategorii SITT · możliwe kilka etykiet · opcja 'brak'" if pl else "12 dialogues · 6 Cialdini principles · 9 SITT categories · multiple labels or none")
    pick=st.selectbox("Wybierz dialog" if pl else "Choose a dialogue",range(len(DIALOGUES)),format_func=lambda i:f"{DIALOGUES[i][0]} · {DIALOGUES[i][1] if pl else DIALOGUES[i][2]}")
    d=DIALOGUES[pick]; prefix=f"dialog_{d[0]}"
    st.markdown("#### "+(d[1] if pl else d[2]))
    st.info(d[3] if pl else d[4])
    rnames={x[0]:x[1] if pl else x[2] for x in CIALDINI}
    snames={x[0]:x[1] if pl else x[2] for x in SITT}
    a,b=st.columns(2)
    with a:
        chosen_c=_select(prefix+"_cial",list(rnames),"Które zasady Cialdiniego widzisz? (można wybrać kilka lub żadnej)" if pl else "Which Cialdini principles appear? (several or none)",lambda k:rnames[k])
    with b:
        chosen_s=_select(prefix+"_sitt",list(snames),"Które kategorie SITT widzisz?" if pl else "Which SITT categories appear?",lambda k:snames[k])
    _field(prefix+"_evidence","Zacytuj krótkie fragmenty, które uzasadniają Twoje etykiety." if pl else "Quote short phrases that support your labels.",90)
    _field(prefix+"_limits","Czy to na pewno manipulacja? Co jeszcze trzeba byłoby wiedzieć?" if pl else "Is this necessarily manipulation? What else would you need to know?",90)
    st.markdown("**"+("Pytanie do dyskusji" if pl else "Discussion question")+":** "+(d[9] if pl else d[10]))
    with st.expander("Pokaż proponowaną interpretację (po zakończeniu własnej analizy)" if pl else "Reveal a suggested interpretation (after your own analysis)"):
        st.write("**Cialdini:** "+(", ".join(rnames[x] for x in d[5]) or ("Brak wyraźnej zasady" if pl else "No clear principle")))
        st.write("**SITT:** "+(", ".join(snames[x] for x in d[6]) or ("Brak wyraźnej kategorii" if pl else "No clear category")))
        st.write(d[7] if pl else d[8])
        st.caption("Klucz dydaktyczny: nie są to zweryfikowane oryginalne anotacje ekspertów." if pl else "Illustrative teaching key, not original verified expert annotations.")
    st.divider()
    st.markdown("#### "+("Porównaj dwie wersje przekazu" if pl else "Compare two messages"))
    st.write("Zapisz neutralną wersję jednego zdania z dialogu, potem wersję wykorzystującą inny mechanizm wpływu. Porównaj różnicę w treści i możliwe konsekwencje etyczne." if pl else "Rewrite one line neutrally, then with a different influence mechanism. Compare the wording and ethical implications.")
    _field(prefix+"_neutral","Wersja neutralna" if pl else "Neutral version",75)
    _field(prefix+"_changed","Wersja zmieniona i uzasadnienie" if pl else "Modified version and explanation",95)

def render_debate(pl):
    st.subheader("Debaty socjologiczne — dwa stanowiska i dowody" if pl else "Sociological debates — two positions and evidence")
    st.write("Wybierz temat. W polu A napisz argument ZA jedną interpretacją (2–4 zdania). W polu B napisz racjonalny argument PRZECIW albo ograniczenie stanowiska A (2–4 zdania). Nie chodzi o dwie osoby: możesz napisać oba stanowiska samodzielnie." if pl else "Choose a topic. In A, write 2–4 sentences supporting one position. In B, write 2–4 sentences challenging A or highlighting its limitations. These are two positions, not necessarily two different people; you can write both yourself.")
    i=st.selectbox("Problem badawczy" if pl else "Research issue",range(len(DEBATES)),format_func=lambda j:DEBATES[j][0] if pl else DEBATES[j][1])
    d=DEBATES[i]; key=f"debate_{i}"
    c1,c2=st.columns(2)
    with c1:
        st.markdown("**A — "+("Stanowisko popierające" if pl else "Supporting position")+"**")
        st.caption("Przykład: "+d[2] if pl else "Example: "+d[3])
        _field(key+"_a","Twój argument A" if pl else "Your argument A",155)
    with c2:
        st.markdown("**B — "+("Kontrargument lub zastrzeżenie" if pl else "Counterargument or qualification")+"**")
        st.caption("Przykład: "+d[4] if pl else "Example: "+d[5])
        _field(key+"_b","Twój kontrargument B" if pl else "Your counterargument B",155)
    st.caption(("Jakie dane mogłyby rozstrzygnąć ten spór? Przykład: " + d[6]) if pl else ("What evidence could clarify the disagreement? Example: " + d[7]))
    _field(key+"_evidence","Dane i sposób ich zebrania" if pl else "Evidence and how to collect it",110)
    _field(key+"_conclusion","Własny wniosek: kiedy A, a kiedy B jest bardziej przekonujące?" if pl else "Your conclusion: when is A or B more convincing?",100)
    with st.expander("Dodatkowe pytania do dyskusji" if pl else "Additional discussion prompts"):
        for q in (("Jakie założenia przyjmują obie strony?", "Czy obie strony posługują się tą samą definicją perswazji?", "Jakie dane mogłyby przeczyć Twojej własnej opinii?", "Czy w innym kraju argumentacja mogłaby wyglądać inaczej?") if pl else ("What assumptions does each side make?", "Do both positions use the same definition of persuasion?", "What evidence might challenge your own view?", "Would these arguments differ in another country?")):
            st.write("• "+q)

def render_export(pl):
    st.divider()
    st.subheader("Pobierz swoje notatki" if pl else "Download your notes")
    st.write("Odpowiedzi z nowych dialogów i debat są zachowywane tymczasowo w bieżącej sesji. Pobierz własny plik na komputer, zanim zamkniesz kartę. Aplikacja nie zapisuje pracy w Google Sheets ani w trwałej bazie danych." if pl else "Your new dialogue and debate answers are held temporarily in this session. Download your own file before closing the tab. The app does not save work to Google Sheets or a permanent database.")
    notes=_lab_state()
    name=st.text_input("Nazwa pliku / identyfikator (opcjonalnie)" if pl else "File identifier (optional)",value="my-sitt-work",key="download_name")
    clean="".join(c for c in name if c.isascii() and (c.isalnum() or c in "-_"))[:50] or "my-sitt-work"
    active={k:v for k,v in notes.items() if v not in ([],"",None)}
    lines=["# Global Social Processes — personal lab notes", "", "Teaching cases: original fictional dialogues, inspired by SITT taxonomy.", ""]
    for k,v in sorted(active.items()):
        lines += ["## "+k.replace("_"," "), "", ", ".join(v) if isinstance(v,list) else str(v), ""]
    if not active:lines.append("No saved notes yet. Complete a dialogue or debate first.")
    st.download_button("⬇️ "+("Pobierz odpowiedzi jako plik .md" if pl else "Download answers as .md"),"\n".join(lines).encode("utf-8"),file_name=clean+".md",mime="text/markdown",use_container_width=True)
    st.download_button("⬇️ "+("Pobierz dane jako .json" if pl else "Download as .json"),json.dumps({"project":"Global Social Processes SITT Lab","notes":active},ensure_ascii=False,indent=2).encode("utf-8"),file_name=clean+".json",mime="application/json",use_container_width=True)
    st.caption("Plik zapisze się na Twoim urządzeniu. To nie jest funkcja wysyłania pracy prowadzącej." if pl else "The file is downloaded to your device. This does not submit the work to your instructor.")
