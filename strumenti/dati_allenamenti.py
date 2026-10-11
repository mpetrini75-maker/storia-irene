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
