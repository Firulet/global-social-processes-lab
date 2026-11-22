"""Global Social Processes | Influence, Persuasion and SITT - educational lab."""
import random
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from content import CIALDINI, SITT, CASES, FREQUENCIES, MODELS
from activities import render_dialogues, render_debate, render_export, _field, _lab_state

st.set_page_config(page_title="Global Social Processes | Influence Lab", page_icon="🌍", layout="wide")
st.markdown('''<style>
.block-container{max-width:1160px;padding-top:1.35rem}
.hero{background:linear-gradient(110deg,#115e69,#1c4564);border-radius:16px;padding:23px 28px;color:white;margin-bottom:18px}
.hero h1{color:white;margin:0;font-size:2.0rem}.hero p{color:#e0f2f3;margin:8px 0 0}
.note{border-left:4px solid #15959a;padding:.65rem .95rem;border-radius:8px;background:rgba(25,127,138,.09);margin:12px 0}
.kicker{text-transform:uppercase;letter-spacing:1px;font-weight:700;color:#178a92;font-size:.8rem}
[data-testid="stMetric"]{border:1px solid rgba(128,128,128,.25);border-radius:12px;padding:10px}
</style>''', unsafe_allow_html=True)

lang=st.sidebar.radio("🌐 Language / Język",["Polski","English"],horizontal=True)
pl=lang=="Polski"
def L(p,e):return p if pl else e
def catname(key):
    c=next(x for x in SITT if x[0]==key)
    return c[1] if pl else c[2]
def rulename(key):
    c=next(x for x in CIALDINI if x[0]==key)
    return c[1] if pl else c[2]
def note(p,e):st.markdown('<div class="note">'+L(p,e)+'</div>',unsafe_allow_html=True)
def title(p,e):st.subheader(L(p,e))
def h(p,e):st.markdown('#### '+L(p,e))

SECTIONS=[('start','Wprowadzenie','Start'),('cialdini','6 zasad Cialdiniego','Cialdini: 6 principles'),('sitt','Taksonomia SITT: 9 kategorii','SITT: 9 categories'),('code','Kodowanie dialogów','Code the dialogues'),('dialogues','Dłuższe dialogi: analiza perswazji','Long dialogues: persuasion analysis'),('rewrite','Eksperyment z komunikatem','Message experiment'),('global','Globalne procesy społeczne','Global social processes'),('data','Co pokazują dane SITT?','Explore SITT findings'),('models','Czy AI rozpoznaje wpływ?','Can AI detect influence?'),('debate','Dyskusje teoretyczne','Theory and debate'),('final','Projekt badawczy','Research design challenge')]
chosen=st.sidebar.radio(L('Wybierz część laboratorium','Choose a lab section'),[x[0] for x in SECTIONS],format_func=lambda k:next((x[1] if pl else x[2]) for x in SECTIONS if x[0]==k))
st.sidebar.caption(L('Bez kont, bez Google Sheets i bez przesyłania odpowiedzi na serwer.','No account, no Google Sheets, no answer submission.'))
st.markdown('<div class="hero"><div style="font-size:.8rem;letter-spacing:2px">INTRODUCTION TO GLOBAL SOCIAL PROCESSES</div><h1>'+L('Wpływ społeczny, perswazja i manipulacja','Social Influence, Persuasion and Manipulation')+'</h1><p>'+L('Interaktywne laboratorium teoretyczne oparte na artykule Unraveling SITT','An interactive theory lab based on the paper Unraveling SITT')+'</p></div>',unsafe_allow_html=True)

if chosen=='start':
    title('Na czym polega to laboratorium?','What is this laboratory about?')
    note('<b>Podstawa naukowa:</b> Unraveling SITT: Social Influence Technique Taxonomy and Detection with LLMs (2025). Artykuł wyróżnia 9 kategorii i 58 technik; wykorzystuje 746 dialogów.','<b>Research source:</b> Unraveling SITT: Social Influence Technique Taxonomy and Detection with LLMs (2025). The paper describes 9 categories and 58 techniques, using 746 dialogues.')
    st.write(L('Będziemy badać, jak komunikaty i normy mogą oddziaływać na decyzje w transnarodowych sieciach, mediach, organizacjach i kampaniach społecznych. Nie każdy wpływ jest manipulacją.','We will explore how messages and norms can shape decisions across transnational networks, media, organizations and social campaigns. Not every form of influence is manipulation.'))
    c1,c2,c3=st.columns(3)
    c1.metric(L('Kategorii SITT','SITT categories'),9);c2.metric(L('Technik SITT','SITT techniques'),58);c3.metric(L('Dialogów w badaniu','Study dialogues'),746)
    h('Trzy pojęcia — nie są synonimami','Three concepts — not synonyms')
    for a,b,c in [('Wpływ społeczny','Social influence','Szeroki proces, w którym inni kształtują postawy lub zachowania.|A broad process in which others shape attitudes or behaviours.'),('Perswazja','Persuasion','Próba przekonania odbiorcy, często jawna i oparta na argumentach.|An attempt to persuade someone, often transparent and argument-based.'),('Manipulacja','Manipulation','Wpływ wykorzystujący ukryte lub wprowadzające w błąd mechanizmy, które mogą podważać autonomię.|Influence using covert or deceptive means that may undermine autonomy.')]:
        with st.expander(a if pl else b,expanded=True):st.write(c.split('|')[0] if pl else c.split('|')[1])
    st.info(L('Przykłady dialogów w ćwiczeniach napisano specjalnie na zajęcia; nie są cytatami z korpusu SITT ani zweryfikowanymi etykietami ekspertów.','Classroom dialogues are newly authored, not quotes from the SITT corpus or expert-validated labels.'))

elif chosen=='cialdini':
    title('Sześć klasycznych zasad wpływu według Cialdiniego','Six classic Cialdini principles of influence')
    note('To <b>model teoretyczny</b>, a nie sześć kategorii z artykułu SITT. SITT ma dziewięć kategorii i obejmuje szerszy repertuar technik.','This is a <b>theoretical framework</b>, not the six categories of SITT. SITT has nine categories and a broader repertoire of techniques.')
    for k,npl,nen,dpl,den,epl,een in CIALDINI:
        with st.expander(('🔹 '+npl) if pl else ('🔹 '+nen),expanded=k=='reciprocity'):
            st.write(dpl if pl else den)
            st.markdown('**'+L('Przykład (autorski):','Illustrative example:')+'**')
            st.info(epl if pl else een)
            st.caption(L('Zastanów się: jaka prośba jest zawarta w komunikacie? Czy możesz stwierdzić, że odbiorca jej uległ?','Think: what is being requested? Does the message prove that the recipient complied?'))
    h('Ćwiczenie — rozpoznaj zasadę','Exercise — identify the principle')
    idx=st.selectbox(L('Wybierz przykład','Choose an example'),range(len(CIALDINI)),format_func=lambda i:f'{i+1}. '+(CIALDINI[i][5] if pl else CIALDINI[i][6]))
    guess=st.selectbox(L('Zasada','Principle'),['—']+[x[0] for x in CIALDINI],format_func=lambda x:'—' if x=='—' else rulename(x),key='c_g')
    if st.button(L('Sprawdź i wyjaśnij','Check and explain'),key='c_btn'):
        st.success(L('Zgodne z kluczem dydaktycznym.','Matches the teaching key.')) if guess==CIALDINI[idx][0] else st.warning(L('Wróć do definicji i porównaj mechanizm.','Review the definition and compare the mechanism.'))
        st.write(CIALDINI[idx][3] if pl else CIALDINI[idx][4])

elif chosen=='sitt':
    title('Dziewięć kategorii i 58 technik SITT','Nine SITT categories and 58 techniques')
    st.write(L('SITT stanowi osobną taksonomię wpływu społecznego: nazwy kategorii pochodzą z tabeli 1 artykułu. Jedna wypowiedź może zawierać kilka kategorii jednocześnie.','SITT is a distinct taxonomy of influence: category labels come from Table 1 of the paper. A message may contain multiple categories at once.'))
    for i,(key,a,b,dp,de) in enumerate(SITT,1):
        with st.expander(f'{i}. {a if pl else b}',expanded=i<=2):
            st.write(dp if pl else de)
            example=next((c for c in CASES if key in c[5]),None)
            if example: st.info((example[3] if pl else example[4]))
    h('SITT a sześć zasad Cialdiniego','SITT versus Cialdini')
    st.write(L('Przykład: niedostępność to zasada Cialdiniego, ale w SITT technika „Unavailability” przypisana jest do kategorii „Context modification”. Oznacza to, że podobne idee mogą należeć do różnych systemów klasyfikacji.','Example: scarcity is a Cialdini principle; in SITT, the “Unavailability” technique belongs to “Context modification”. Similar ideas can be classified differently across taxonomies.'))

elif chosen=='dialogues':
    render_dialogues(pl, CIALDINI, SITT)

elif chosen=='code':
    title('Pracownia kodowania: wybierz dowody w tekście','Coding studio: identify the evidence in a message')
    note('Klucz kodowy określa <b>definicje, kryteria włączenia i wyłączenia oraz zasady rozstrzygania sporów</b>. Tu porównujesz ocenę z pomocniczym kluczem autorskich przykładów, nie z oryginalnymi etykietami SITT.','A codebook provides <b>definitions, inclusion/exclusion criteria and disagreement rules</b>. Here you compare against a teaching key for new examples, not original SITT annotations.')
    if 'caseidx' not in st.session_state:st.session_state.caseidx=0
    left,right=st.columns([3,1])
    idx=left.selectbox(L('Wybierz tekst','Choose a message'),range(len(CASES)),index=st.session_state.caseidx,format_func=lambda i:f'{CASES[i][0]} · '+(CASES[i][1] if pl else CASES[i][2]))
    c=CASES[idx]
    st.markdown('### '+(c[3] if pl else c[4]))
    selections=st.multiselect(L('Wskaż możliwe kategorie SITT (0, 1 lub kilka)','Select SITT categories (zero, one or several)'),[x[0] for x in SITT],format_func=catname,key='codes')
    evidence=st.text_area(L('Które słowa są dowodem? Jak wyjaśnisz swoją decyzję?','Which words are evidence? How would you justify your decision?'),height=85,key='evidence')
    _lab_state()[f'case_{c[0]}_labels']=selections
    _lab_state()[f'case_{c[0]}_evidence']=evidence
    no_context=st.checkbox(L('Zbyt mało kontekstu, aby rozstrzygnąć intencję nadawcy','Insufficient context to judge the speaker’s intentions'),value=False,key='c_uncertain')
    if st.button(L('Pokaż interpretację przykładową','Show an example interpretation')):
        correct=set(c[5]); selected=set(selections)
        st.metric(L('Zgodność zbiorów — Jaccard (pomocniczo)','Set overlap — Jaccard (illustrative)'),f'{len(selected&correct)/len(selected|correct) if selected|correct else 1:.2f}')
        st.write('**'+L('Możliwe kategorie:','Possible categories:')+'**',', '.join(catname(k) for k in correct) or L('brak','none'))
        st.info(c[7] if pl else c[8])
        st.caption(L('To nie jest miara zgodności między ekspertami i nie dowodzi prawidłowości samej taksonomii.','This is not an inter-rater reliability estimate or a validation of the taxonomy.'))
    st.divider()
    h('Dwa sposoby patrzenia na ten sam tekst','Two frameworks applied to the same text')
    st.write(L('Czy w tym przykładzie da się również wskazać zasadę Cialdiniego? Czasami nie, ponieważ SITT jest szersza.','Can a Cialdini principle also be identified? Sometimes not: SITT covers a wider set of mechanisms.'))
    if st.button(L('Pokaż propozycję mapowania','Show suggested mapping')):
        st.write(', '.join(rulename(k) for k in c[6]) if c[6] else L('Brak oczywistego odpowiednika w sześciu zasadach.','No obvious equivalent among the six principles.'))

elif chosen=='rewrite':
    title('Eksperyment teoretyczny: co zmienia forma komunikatu?','Theory experiment: how does message design change?')
    h('Wybierz strategię przekazu','Choose a communication strategy')
    topic=st.selectbox(L('Temat','Topic'),[0,1,2],format_func=lambda i:[L('Udział w webinarze o migracjach','Attend a migration webinar'),L('Wsparcie kampanii klimatycznej','Support a climate campaign'),L('Zapis do programu wymiany','Join an exchange programme')][i])
    method=st.selectbox(L('Rodzaj komunikatu','Message framing'),['neutral','norms','authority','emotions','scarcity','reciprocity'])
    texts={
    'neutral':[('Webinar o migracjach odbędzie się w piątek.','The migration webinar will take place on Friday.'),('Kampania klimatyczna przyjmuje zgłoszenia.','The climate campaign is accepting participants.'),('Rekrutacja do programu wymiany jest otwarta.','Applications for the exchange programme are open.')],
    'norms':[('Większość studentów już wybrała webinar o migracjach.','Most students have already chosen the migration webinar.'),('Wiele osób z naszego roku wspiera tę kampanię.','Many students from our year support this campaign.'),('Twoi rówieśnicy zgłaszają się do wymiany.','Your peers are signing up for the exchange.')],
    'authority':[('Ekspertka ds. migracji rekomenduje ten webinar.','A migration expert recommends this webinar.'),('Naukowcy wspierają działania tej kampanii.','Researchers support this campaign.'),('Koordynator akademicki rekomenduje ten program wymiany.','The academic coordinator recommends this exchange programme.')],
    'emotions':[('Nie przegap okazji zrozumienia problemów ludzi zmuszonych do migracji.','Do not miss a chance to understand the challenges faced by displaced people.'),('Nie odkładaj działania, jeśli martwisz się o przyszłość klimatu.','Do not postpone action if you worry about the climate future.'),('Możesz żałować, jeśli ominie cię okazja do wymiany.','You may regret missing the chance to go on exchange.')],
    'scarcity':[('Na webinar pozostały trzy wolne miejsca.','Only three webinar places remain.'),('Zgłoszenia do kampanii kończą się dzisiaj.','Campaign registration closes today.'),('Nabór do wymiany kończy się za godzinę.','Exchange applications close in one hour.')],
    'reciprocity':[('Dostaliście już darmowy poradnik; wesprzyjcie teraz nasz webinar.','You have received a free guide; now support our webinar.'),('Przesłaliśmy bezpłatny raport; pomóżcie naszej kampanii.','We shared a free report; please help our campaign.'),('Dostaliście bezpłatne konsultacje; zgłoście się do wymiany.','You received a free consultation; apply for the exchange.')]
    }
    base=texts['neutral'][topic][0 if pl else 1];changed=texts[method][topic][0 if pl else 1]
    c1,c2=st.columns(2)
    c1.markdown('**'+L('Komunikat neutralny','Neutral message')+'**');c1.info(base)
    c2.markdown('**'+L('Komunikat zmieniony','Modified message')+'**');c2.success(changed)
    st.caption(L('Wszystkie komunikaty są fikcyjne; nie mierzymy tutaj rzeczywistej skuteczności perswazji.','All messages are invented; persuasion effectiveness is not measured here.'))
    _field('experiment_interpretation',L('Co zmieniło się w mechanizmie wpływu? Co należałoby zbadać empirycznie?','What influence mechanism changed? What would need empirical testing?'),height=115)
    with st.expander(L('Wskazówka interpretacyjna','Interpretation hint')):
        st.write(L('Zaobserwuj różnicę w odwołaniu do norm, autorytetu, emocji, ograniczonej dostępności lub wzajemności. Bez eksperymentu nie znamy skutku dla zachowania.','Notice the appeal to norms, expertise, emotion, scarcity or reciprocity. Without an experiment we cannot know its behavioural effect.'))

elif chosen=='global':
    title('Od mikrokomunikatu do globalnego procesu','From micro-messages to global social processes')
    st.write(L('Jedna wiadomość to poziom mikro. Kiedy podobne wzorce rozpowszechniają się między platformami, instytucjami i państwami, powstają pytania o procesy makro.','A single message is micro-level. When communication patterns spread across platforms, institutions and countries, they raise macro-level questions.'))
    import matplotlib.patches as patches
    fig,ax=plt.subplots(figsize=(10,3.0));fig.patch.set_alpha(0);ax.set_facecolor('none');ax.set_xlim(0,10);ax.set_ylim(0,3);ax.axis('off')
    xs=[1.2,4,6.8,9];labels=(["Nadawca","Platforma","Instytucje","Odbiorcy"] if pl else ["Sender","Platform","Institutions","Audiences"])
    for i,(x,lab) in enumerate(zip(xs,labels)):
        ax.add_patch(patches.FancyBboxPatch((x-.82,1.04),1.65,.95,boxstyle='round,pad=.12',fc=['#126d77','#2b7799','#5174a7','#178878'][i],ec='none'))
        ax.text(x,1.52,lab,color='white',weight='bold',ha='center',va='center',fontsize=10)
        if i: ax.annotate('',xy=(x-.89,1.5),xytext=(xs[i-1]+.9,1.5),arrowprops={'arrowstyle':'->','lw':2,'color':'#7a8c98'})
    st.pyplot(fig,clear_figure=True)
    choices=[('transnational','Transnarodowy aktywizm','Transnational activism','Jak hasło kampanii zmienia znaczenie po przetłumaczeniu i rozpowszechnieniu w różnych krajach?','How can a campaign slogan change meaning when translated and circulated across countries?'),('migration','Migracje i solidarność','Migration and solidarity','Czy apel do emocji mobilizuje wsparcie, czy wzmacnia stereotypy?','Does an emotional appeal mobilize support or reinforce stereotypes?'),('climate','Globalne ruchy klimatyczne','Global climate movements','Kiedy odwołanie do norm wspólnoty wspiera kooperację, a kiedy wyklucza?','When do community norms foster cooperation, and when do they exclude?'),('digital','Platformizacja komunikacji','Platformized communication','W jaki sposób algorytmy rekomendacyjne zmieniają widoczność różnych przekazów?','How do recommender algorithms change the visibility of messages?')]
    theme=st.selectbox(L('Temat badawczy','Research theme'),range(len(choices)),format_func=lambda i:choices[i][1] if pl else choices[i][2])
    st.info(choices[theme][3] if pl else choices[theme][4])
    st.write(L('Rozróżnij: nadawcę, kanał, odbiorców, kontekst instytucjonalny i możliwe konsekwencje.','Distinguish the sender, channel, audiences, institutional context and possible consequences.'))
    _field('global_hypothesis',L('Napisz hipotezę, możliwe zmienne i ograniczenia','Write a hypothesis, possible variables and limitations'),height=160)
    with st.expander(L('Co jest trudne metodologicznie?','What is methodologically difficult?')):
        st.write(L('Rozpowszechnienie komunikatu nie oznacza automatycznie zmiany postaw. Selekcja odbiorców, tłumaczenie, instytucje i algorytmy mogą zmieniać zarówno ekspozycję, jak i interpretację.','Message circulation does not automatically mean attitude change. Audience selection, translation, institutions and algorithms can alter exposure and interpretation.'))

elif chosen=='data':
    title('Oryginalne wyniki artykułu SITT','Empirical findings reported in SITT')
    note('Poniższe liczby pochodzą z tabel i wykresów artykułu, a nie z nowych symulacji. Liczebności kategorii nie sumują się do 746, ponieważ dialog może otrzymać więcej niż jedną kategorię.','The numbers below are reported in the paper, not newly simulated. Category counts do not sum to 746 because dialogues may have multiple labels.')
    frame=pd.DataFrame(FREQUENCIES,columns=['Category','Count'])
    st.bar_chart(frame.set_index('Category')['Count'],height=310)
    st.caption(L('Źródło: Figure 1 w SITT. Dane zbiorcze; w aplikacji nie udostępniamy oryginalnych dialogów.','Source: SITT Figure 1. Aggregate counts; original dialogues are not included in the app.'))
    selected=st.selectbox(L('Zbadaj wybraną kategorię','Explore one category'),[x[0] for x in FREQUENCIES])
    count=dict(FREQUENCIES)[selected]
    st.metric(L('Dialogów z etykietą','Dialogues with this label'),count)
    st.metric(L('Udział w 746 dialogach (możliwe nakładanie etykiet)','Share of 746 dialogues (labels overlap)'),f'{100*count/746:.1f}%')
    h('Co można wywnioskować?','What can we conclude?')
    st.write(L('Najwięcej tekstów oznaczono odwołaniem do emocji. Nie oznacza to, że emocje były najskuteczniejsze; zbiór powstał z określonych źródeł, w tym części wygenerowanej syntetycznie.','Emotional appeals received the most labels. This does not mean they were the most effective; the corpus used selected sources, including a synthetically generated portion.'))
    _field('sitt_data_limits',L('Jakie zagrożenia dla uogólnienia wyników widzisz?','What threatens generalization of the findings?'),height=100)

elif chosen=='models':
    title('Jak dobrze modele językowe rozpoznawały SITT?','How well did language models detect SITT?')
    st.write(L('W artykule porównano modele na kategoriach i szczegółowych technikach. Pokazujemy wyniki F1 dla wersji polskiej. To wyniki historycznych wersji modeli testowanych w badaniu, nie ich aktualne osiągnięcia.','The paper compared models on broad categories and detailed techniques. These are Polish-language F1 scores of historical model versions, not current model performance.'))
    df=pd.DataFrame(MODELS,columns=['Model','Categories F1','Techniques F1'])
    st.bar_chart(df.set_index('Model'),height=310)
    metric=st.selectbox(L('Co porównujesz?','What do you compare?'),['Categories F1','Techniques F1'])
    st.metric(L('Najwyższy wynik','Highest score'),df.loc[df[metric].idxmax(),'Model']+' · '+f"{df[metric].max():.2f}")
    h('Interpretacja','Interpretation')
    st.write(L('F1 łączy precyzję (precision) i czułość (recall). Wynik 0,45 nie oznacza 45% poprawnych dialogów. Jest to zagregowana miara jakości klasyfikacji wieloetykietowej.','F1 combines precision and recall. An F1 of 0.45 does not mean 45% of dialogues were classified correctly; it is an aggregated multilabel classification measure.'))
    with st.expander(L('Zobacz wzór i przykład','See the formula and example')):
        st.latex(r'Precision=\frac{TP}{TP+FP},\quad Recall=\frac{TP}{TP+FN}')
        st.latex(r'F1=\frac{2\cdot Precision\cdot Recall}{Precision+Recall}')
        st.write(L('Przykład: TP=6, FP=2, FN=4. Precision=6/8=0,75; recall=6/10=0,60; F1≈0,667. To wyłącznie przykład obliczeniowy.','Example: TP=6, FP=2, FN=4. Precision=6/8=.75; recall=6/10=.60; F1≈.667. This is an arithmetic illustration only.'))
    _field('model_interpretation',L('Dlaczego klasyfikacja subtelnych technik może być trudniejsza niż szerokich kategorii?','Why might subtle techniques be harder to identify than broad categories?'),height=110)

elif chosen=='debate':
    render_debate(pl)

else:
    title('Zaprojektuj własne badanie porównawcze','Design your own comparative research')
    st.write(L('Wyobraź sobie, że badający komunikację społeczną zespół porównuje komunikaty o zmianach klimatycznych, migracji lub technologii AI w dwóch krajach. Wybierz problem, przygotuj kodowanie i zaproponuj metodę weryfikacji.','Imagine a research team comparing climate, migration or AI communication in two countries. Choose a question, develop a coding strategy and propose validation methods.'))
    theme=st.selectbox(L('Dziedzina','Domain'),[L('Klimat','Climate'),L('Migracje','Migration'),L('AI i edukacja','AI and education')])
    countries=st.multiselect(L('Porównywane kraje (przykład)','Comparison countries (example)'),['Poland','Spain','Germany','France','Lithuania'],default=['Poland','Spain'])
    labels=st.multiselect(L('Kategorie SITT','SITT categories'),[x[0] for x in SITT],format_func=catname,default=['emotions','norms'])
    _lab_state()['final_countries']=countries
    _lab_state()['final_labels']=labels
    sample=st.slider(L('Planowana liczba wiadomości na kraj','Planned messages per country'),20,400,100,20)
    _lab_state()['final_n_per_country']=str(sample)
    st.metric(L('Łączna planowana próba','Total planned sample'),sample*len(countries))
    _field('final_hypothesis',L('Pytanie i hipoteza badawcza','Research question and hypothesis'),height=100)
    _field('final_codebook',L('Reguły kodowania: definicje, przykłady i niejednoznaczności','Coding rules: definitions, examples and ambiguities'),height=105)
    _field('final_validation',L('Jak sprawdzisz zgodność kodowania i porównywalność językową?','How will you test coding agreement and language comparability?'),height=100)
    if st.button(L('Pokaż listę kontroli jakości','Show quality checklist')):
        st.info(L('Zapewnij zgodność próbek i jednostek analizy; dwoje niezależnych anotatorów dla części tekstów; wspólny codebook; procedurę rozstrzygania sporów; ostrożne wnioski o intencji i skuteczności.','Ensure comparable sampling and units; two independent annotators for a subset; a shared codebook; disagreement resolution; and cautious claims about intent and effects.'))

render_export(pl)
st.divider()
st.caption(L('Podstawa: Mieleszczenko-Kowszewicz i in., „Unraveling SITT” (2025), arXiv:2506.00061. Ćwiczenia i komunikaty są autorskie, z wyjątkiem wyraźnie oznaczonych zagregowanych wyników publikacji. Aplikacja nie przesyła odpowiedzi do zewnętrznego serwera ani ich nie zapisuje.','Source: Mieleszczenko-Kowszewicz et al., “Unraveling SITT” (2025), arXiv:2506.00061. Classroom cases are newly written; only explicitly labeled aggregate findings come from the paper. No answers are submitted or stored.'))
