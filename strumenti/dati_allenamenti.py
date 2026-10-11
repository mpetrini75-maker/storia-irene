"""Le domande degli allenamenti di Storia di Irene (prima opzione = quella giusta: l'app le mescola).
Ogni mattoncino: 3 livelli x 5 per domande, vero/falso e abbina. Solo contenuti delle slide della prof."""


def Q(q, *opts):
    return {"q": q, "opts": list(opts)}


def V(q, v, perche):
    return {"q": q, "v": v, "perche": perche}


def A(*coppie):
    return [{"l": l, "r": r} for l, r in coppie]


MATTONCINI = {
    "cesare": {
        "num": 1, "titolo": "Giulio Cesare e la fine della repubblica",
        "quiz": [
            [Q("Chi formava il primo triumvirato?", "Cesare, Pompeo e Crasso", "Cesare, Bruto e Cicerone", "Pompeo, Crasso e Cleopatra"),
             Q("In che anno nasce il primo triumvirato?", "60 a.C.", "44 a.C.", "52 a.C."),
             Q("Che cosa vuol dire triumvirato?", "alleanza di tre uomini", "guerra fra tre città", "tre consoli eletti"),
             Q("Che cosa porta Cesare all'alleanza?", "i voti della plebe", "l'esercito", "i cavalieri"),
             Q("Chi prova a fermare i triumviri e finisce in esilio?", "Cicerone", "Bruto", "Vercingetorige")],
            [Q("Quale terra conquista Cesare tra il 58 e il 52 a.C.?", "la Gallia", "l'Egitto", "la Grecia"),
             Q("Chi era Vercingetorige?", "il capo dei Galli ribelli", "un senatore romano", "il re d'Egitto"),
             Q("Quale città cade nel 52 a.C.?", "Alesia", "Farsalo", "Munda"),
             Q("Come muore Crasso?", "combattendo contro i Parti", "pugnalato in Senato", "in un naufragio"),
             Q("Fin dove arriva Cesare a nord?", "in Britannia", "in Russia", "in Svezia")],
            [Q("Quale fiume attraversa Cesare con l'esercito?", "il Rubicone", "il Po", "il Tevere"),
             Q("Dove Cesare sconfigge Pompeo nel 48 a.C.?", "a Farsalo, in Grecia", "ad Alesia, in Gallia", "a Roma"),
             Q("Dove scappa Pompeo, e lì viene ucciso?", "in Egitto", "in Spagna", "in Britannia"),
             Q("Chi organizza la congiura contro Cesare?", "Bruto e Cassio Longino", "Pompeo e Crasso", "Cicerone e Cleopatra"),
             Q("Quando muore Cesare?", "il 15 marzo 44 a.C.", "il 1 gennaio 60 a.C.", "nel 52 a.C. ad Alesia")],
        ],
        "vf": [
            [V("Cesare era un capo dei popolari.", True, "Il gruppo che difendeva la plebe."),
             V("Il triumvirato era un'alleanza di tre uomini.", True, "Cesare, Pompeo e Crasso."),
             V("Pompeo portava all'alleanza i voti della plebe.", False, "Pompeo portava l'esercito; i voti della plebe li portava Cesare."),
             V("Grazie all'alleanza Cesare diventa console.", True, "Console nel 59 a.C."),
             V("Cicerone entra nel triumvirato.", False, "Cicerone li ostacola e viene esiliato.")],
            [V("Nel 60 a.C. Cesare era il più forte dei tre.", False, "Era il più debole: non aveva vittorie né un esercito fedele."),
             V("Cesare chiede la Gallia per poter fare la guerra.", True, "Così si costruisce un esercito fedele."),
             V("Vercingetorige era un generale romano.", False, "Era il capo dei Galli ribelli."),
             V("La Gallia è più o meno l'attuale Francia.", True, "Guarda la carta in arancione."),
             V("Nel 52 a.C. Cesare è diventato il più forte.", True, "Ha la Gallia e Crasso è morto.")],
            [V("Attraversare il Rubicone con l'esercito era vietato.", True, "Per questo inizia la guerra civile."),
             V("Una guerra civile è una guerra contro un popolo straniero.", False, "È una guerra tra cittadini dello stesso Stato."),
             V("Cesare si fa incoronare re.", False, "Non si fa re: prende tutte le cariche della repubblica."),
             V("Cesare porta i senatori da 600 a 900.", True, "Mette in Senato persone fedeli a lui."),
             V("Cesare dà la cittadinanza alla Pianura Padana.", True, "Cioè alla Gallia Cisalpina.")],
        ],
        "abbina": [
            A(("Cesare", "i voti della plebe"), ("Pompeo", "l'esercito"), ("Crasso", "i cavalieri"),
              ("Cicerone", "esiliato"), ("Triumvirato", "alleanza di tre")),
            A(("Gallia", "conquistata 58-52 a.C."), ("Vercingetorige", "capo dei Galli"), ("Alesia", "si arrende nel 52"),
              ("Britannia", "l'attuale Inghilterra"), ("Parti", "uccidono Crasso")),
            A(("Rubicone", "inizio della guerra civile"), ("Farsalo", "Pompeo sconfitto"), ("Cleopatra", "regina d'Egitto"),
              ("Idi di marzo", "15 marzo"), ("Bruto", "congiurato")),
        ],
    },
}

MATTONCINI["pax-romana"] = {
    "num": 2, "titolo": "La pax romana e la società imperiale",
    "quiz": [
        [Q("Che cos'è la pax romana?", "un lungo periodo di pace nell'Impero", "una guerra contro i barbari", "una legge di Cesare"),
         Q("Fino a quando dura la pax romana?", "fino alla fine del II secolo d.C.", "fino al 44 a.C.", "fino all'anno 1000"),
         Q("Quali tre cose crescono grazie alla pace?", "commerci, città e agricoltura", "guerre, tasse e schiavi", "scuole, chiese e porti"),
         Q("Quante monete si usano nell'Impero?", "una sola", "una per ogni provincia", "nessuna, si fa baratto"),
         Q("Che cosa manca sui mari durante la pax romana?", "i pirati", "le navi", "i porti")],
        [Q("Quale attrezzo nuovo si diffonde in agricoltura?", "la falce", "il trattore", "l'aratro elettrico"),
         Q("Chi lavora tanto nei campi?", "gli schiavi", "i senatori", "i soldati"),
         Q("Quanti abitanti ha Roma?", "un milione", "diecimila", "dieci milioni"),
         Q("Quali città italiane fondano i Romani in questo periodo?", "Torino e Aosta", "Milano e Napoli", "Venezia e Firenze"),
         Q("Che cosa sono le colonie?", "città nuove fondate dai Romani", "isole del Mediterraneo", "campi di grano")],
        [Q("Chi abita nella domus?", "le famiglie ricche", "la plebe", "gli schiavi soli"),
         Q("Che cos'è il peristilio?", "il giardino della domus", "la cucina", "la porta d'ingresso"),
         Q("Dove vive la plebe?", "nelle insulae", "nelle domus", "nelle ville al mare"),
         Q("Quanto deve avere un senatore?", "un milione di sesterzi", "400.000 sesterzi", "cento sesterzi"),
         Q("Da dove vengono i soldi dei cavalieri?", "dai commerci", "dalla guerra", "dal Senato")],
    ],
    "vf": [
        [V("Durante la pax romana dentro l'Impero non ci sono guerre.", True, "È un lungo periodo di pace."),
         V("Nell'Impero ogni regione ha la sua moneta.", False, "C'è una sola moneta per tutto l'Impero."),
         V("Le strade romane funzionano bene.", True, "Un sistema di strade efficiente aiuta i commerci."),
         V("Un mercante può andare dalla Siria alla Britannia restando nello stesso Stato.", True, "È tutto Impero romano."),
         V("Durante la pax romana i pirati sono dappertutto.", False, "Non ci sono pirati né briganti.")],
        [V("Roma arriva a un milione di abitanti.", True, "Alessandria e Antiochia a 250.000."),
         V("Torino e Aosta sono fondate dai Romani.", True, "Come Strasburgo, Vienna e Belgrado."),
         V("L'agricoltura va male perché ci sono troppe guerre.", False, "Va bene proprio perché non ci sono guerre."),
         V("Le città crescono grazie ai soldi dei commerci.", True, "Più ricchezza, città più grandi."),
         V("Nei campi lavorano molti schiavi.", True, "C'è tanta mano d'opera schiavile.")],
        [V("La domus è il palazzo dei poveri.", False, "La domus è la casa dei ricchi; i poveri vivono nelle insulae."),
         V("Nell'atrio il padrone riceve i clienti.", True, "Si entra dal vestibolo."),
         V("Nelle insulae scoppiano spesso incendi.", True, "Sono fatte in gran parte di legno."),
         V("Il titolo di senatore passa ai figli.", True, "È ereditario; quello di cavaliere no."),
         V("I senatori guadagnano soprattutto con i commerci.", False, "I senatori guadagnano dalla terra; i cavalieri dai commerci.")],
    ],
    "abbina": [
        A(("Pax romana", "lungo periodo di pace"), ("Commerci", "una sola moneta"), ("Città", "Roma: un milione"),
          ("Agricoltura", "la falce"), ("Mare", "niente pirati")),
        A(("Torino", "fondata dai Romani"), ("Colonia", "città nuova"), ("Alessandria", "250.000 abitanti"),
          ("Strade", "sistema efficiente"), ("Siria e Britannia", "nello stesso Stato")),
        A(("Domus", "casa dei ricchi"), ("Insula", "palazzo dei poveri"), ("Peristilio", "giardino"),
          ("Senatori", "1 milione di sesterzi"), ("Cavalieri", "400.000 sesterzi")),
    ],
}
