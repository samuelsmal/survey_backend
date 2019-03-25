# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

# fr 01
raw = """1. plaine / montagne
    1. haut / petit
    2. bas / haut +
    3. herbe / eau
    4. je ne sais pas
2. présent / passé
    1. sécurité / insécurité
    2. aujourd’hui / futur
    3. pendant / avant +
    4. je ne sais pas
3. pot / sabot
    1. feu / pied
    2. potier / sabotier +
    3. potier / savetier
    4. je ne sais pas
4. VIDE est à PLEIN ce que SOIREE est à…
    1. Temps
    2. Fin
    3. Réveil
    4. Heure
    5. Matinée +
    6. Je ne sais pas
5. PEINTRE est à PINCEAU ce que SCRIBE est à 
    1. Crayon +
    2. Page
    3. Livre
    4. Mot
    5. Papier
    6. Je ne sais pas
6. POMME est à FRUIT ce que POMMIER est à ..
    1. Récolte
    2. Tronc
    3. Feuille
    4. Grappe
    5. Arbre +
    6. Je ne sais pas
7. CHEMISE est à TISSU ce que PNEU est à ....
    1. Caoutchouc +
    2. Goudron
    3. Conduite
    4. Route
    5. Voiture
    6. Je ne sais pas
8. OBSCURE est à NUIT ce que CLAIR est à …
    1. Soleil
    2. Ombre
    3. Lampe
    4. Réveil
    5. Jour +
    6. Je ne sais pas
9. POISON est à MORT ce que INFRACTION est à..
    1. Amande
    2. Transgression
    3. Violation
    4. Sanction +
    5. Rupture
    6. Je ne sais pas
10. … est à bateau ce qu’essence est à …
    1. Mer … route
    2. Voile … pompe
    3. Vent … voiture +
    4. Je ne sais pas
11. ORNITHOLOGUE est à … ce que … est à FRUITS
    1. Bijou / Fructologue
    2. Cétacé / Fruitier
    3. Oiseau / Pomologue +
    4. Dinosaure / Mycologue
    5. Mammifère / Sinologue
    6. Je ne sais pas
12. BANAL est à .. ce que SAGE est à..
    1. Sympathique/Magnifique
    2. Ordinaire/Turbulent
    3. Rare/Prudent
    4. Extraordinaire/Dissipé +
    5. Original/Savant 
    6. Je ne sais pas
13. GOYAVE / … , POIRES / …
    1. Fruit / Sirop
    2. Rose / Vin
    3. Herbacé / Fruitier
    4. Voyage / Espoir +
    5. Local / Tropical 
    6. Je ne sais pas
14. TANGENT est à TOUCHER ce que SÉCANT est à…
    1. Éloigner
    2. Correspondre
    3. Couper +
    4. Joindre
    5. Assembler
    6. Je ne sais pas
15. PRENDRE est à … ce que … est à LAVER
    1. Donner / Repasser
    2. Vendre / Donner
    3. Vouloir / Arranger
    4. Offrir / Lessiver
    5. Saisir / Nettoyer +
    6. Je ne sais pas
16. … est à modeste ce que plébéien est à …
    1. modique / tyran
    2. vantard / impopulaire +
    3. fleur / champ
    4. je ne sais pas
17. bicyclette / voiture
    1. tricycle / voiture de course
    2. draisienne / fardier +
    3. pédalier / klaxon
    4. je ne sais pas
18. CONFIRMATION est à ACCORD ce que CONNIVENCE est à ..
    1. Enchantement
    2. Imagination
    3. Abstinence
    4. Collusion +
    5. Prévalence
    6. Je ne sais pas
19. PHILATÉLISTE / TIMBRE , … / …
    1. Fibulanomiste / Billet
    2. Colombophile / Inspecteur
    3. Erpétolophile / Maladie
    4. Apertophile / Boisson
    5. Mycophile / Champignon +
    6. Je ne sais pas
"""

# <codecell>

# fr 02
raw="""1. année / mois
    a. roman / chapitre +
    b. bissextile / été
    c. pierre / pont
    d. je ne sais pas
2. auteur / rédacteur
    a. roman / éditorial +
    b. largeur / imprimeur
    c. livre / volume
    d. je ne sais pas
3. phrase / gamme
    a. livre / piano
    b. mot / note +
    c. discours / sonate
    d. je ne sais pas
4. CARRÉ est à RECTANGLE ce que CERCLE est à ..
    a. Sphère 
    b. Courbe
    c. Diamètre
    d. Ellipse +
    e. Rayon
    f. Je ne sais pas
5. ANNULAIRE est à MAIN ce que ONGLE est à ..
    a. Doigt +
    b. Vernis
    c. Peau
    d. Coupe 
    e. Poil
    f. Je ne sais pas
6. POULE est à COQ ce que JUMENT est à ...
    a. Poulain
    b. Âne
    c. Ferme 
    d. Pâture
    e. Etalon +
    f. Je ne sais pas
7. GRAMME est à MASSE ce que HEURE est à …
    a. Montre
    b. Temps +
    c. Minute
    d. Semaine
    e. Saison
    f. Je ne sais pas
8.  BEAU est à AUBE ce que CHIEN est à ..
    a. Réveil
    b. Aboie
    c. Chine +
    d. Maître
    e. Ami
    f. Je ne sais pas
9. REMPART est à PROTECTION ce que THÉÂTRE est à …
    a. Public
    b. Pièce 
    c. Divertissement +
    d. Comédie
    e. Acteur
    f. Je ne sais pas 
10. … est à craie ce que toile est à …
    a. pastel / godets
    b. tableau / pinceau +
    c. pinceau / gouache
    d. je ne sais pas
11. BRANCHE est à … ce que … est à PEIGNE
    a. Poisson / Manche
    b. Activité / Pointe
    c. Chemin / Cheveu
    d. Division / Brossage
    e. Lunette / Dent +
    f. Je ne sais pas
12. PEAU est à .. ce que CERVEAU est à..
    a. Urologue/Cardiologue
    b. Dermatologue/Urologue
    c. Pneumologue/Cardiologue
    d. Dermatologue/ Neurologue +
    e. Gastro-entérologue/Neurologue
    f. Je ne sais pas
13. HABITER / RÉSIDER , … / …
    a. Distraire / Emmener
    b. Habiter / Changer
    c. Offrir / Donner +
    d. Sécher / Repasser
    e. Manger / Courir
    f. Je ne sais pas
14. INCISION est à BISTOURI ce que SILLON est à 
    a. Tranchée
    b. Terre 
    c. Charrue +
    d. Rigole
    e. Champs
    f. Je ne sais pas
15. OLIVIER est à … ce que … est à PAIX
    a. Arbre / Raison 
    b. Huile / Travail
    c. Prénom / Guerre
    d. Longévité / Colombe +
    e. Joie / Traité
    f. Je ne sais pas
16. … est à ambassadeur ce qu’opercule est à …
    a. ambassade / monticule 
    b. poste / poisson
    c. plénipotentiaire / couvercle +
    d. je ne sais pas
17. persévérance / avarice
    a. pugnacité / bonté
    b. acharnement / dilapider
    c. versatilité / générosité +
    d. je ne sais pas
18. RIGOUREUX est à INDULGENT ce que PLANTUREUX est à..
    a. Chétif +
    b. Chauvin
    c. Charnu
    d. Cholérique 
    e. Chaleureux
    f. Je ne sais pas
19. DISPERSION / DISSIPATION , … / …
    a. Augmentation / Diminution
    b. Propension / Inclination +
    c. Accumulation / Digestion
    d. Création / Gestion
    e. Communion / Fonction
    f. Je ne sais pas
"""

# <codecell>

# fr
raw="""1. animal / cage
    a. homme / jardin
    b. homme / prison +
    c. homme / clotûre
    d. je ne sais pas
2. parents / enfants
    a. famille / école
    b. enseignants / élèves +
    c. cousins / cousines
    d. je ne sais pas
3. muscat / conférence
    a. apéritif / imitation
    b. raisin / public +
    c. raisin / poire 
    d. je ne sais pas
4. ENVOYÉ est à REÇU ce que LANCÉ est à…
    a. Perdu
    b. Jeté
    c. Attrapé +
    d. Lu
    e. Cassé
    f. Je ne sais pas
5. RAISIN est à VIN ce que BLÉ est à…
    a. Orge
    b. Pain +
    c. Alcool
    d. Fruit
    e. Terre
    f. Je ne sais pas 
6. PETIT est à GRAND ce que BIENVEILLANT est à …
    a. Maladroit
    b. Entreprenant
    c. Téméraire
    d. Hostile +
    e. Robuste
    f. Je ne sais pas
7. AIMER est à MAIRE ce que CHINE est à …
    a. Pays
    b. Chien +
    c. Est
    d. Soleil
    e. Ciel
    f. Je ne sais pas
8. LETTRE est à MOT ce que PHRASE est à …
    a. Verbe
    b. Interrogation
    c. Paragraphe +
    d. Expression
    e. Livre
    f. Je ne sais pas
9. CARPE est à MUET ce que TAUPE est à ..
    a. Bavard
    b. Rusé
    c. Myope +
    d. Doux
    e. Têtu
    f. Je ne sais pas
10. ARTIFICIEL est à … ce que … est à PROFOND
    a. Plante / Mer
    b. Réalité / Fabriqué
    c. Factice / Personnel
    d. Naturel / Superficiel +
    e. Ile / Océan
    f. Je ne sais pas
11. CUISINER est à.. ce que LAVER est à
    a. Préparer/Acheter
    b. Regarder /Changer
    c. Servir/sécher +
    d. Gagner/Arrêter
    e. Cuire/Arranger
    f. Je ne sais pas
12. NOUER est à .. ce que GAGNER est à..
    a. Lier/Perdre
    b. Attacher/Triompher +
    c. Défaire/Encaisser
    d. CHavirer/Percevoir
    e. Noeud/Perte
    f. Je ne sais pas
13. GOLF / DEBOUT , … / …
    a. Ski / Tailleur
    b. Tennis / Genou
    c. Cheval / Califourchon +
    d. Natation / Assis 
    e. Escrime / Allongé
    f. Je ne sais pas
14. HARICOT est à … ce que … est à POIRES
    a. Vert / Pomme
    b. Chariot / Espoir +
    c. Boîtes / Conserve
    d. Légume / Dessert 
    e. Fin / Molle
    f. Je ne sais pas
15. EMPATHIE est à .. ce que ANIMOSITÉ est à…
    a. Maladroit/Joie
    b. Égoïsme/Haine
    c. Narcissisme/Antipathie
    d. Amour/Grossier
    e. Compassion/Hostilité +
    f. Je ne sais pas
16. … est à voix ce qu’orthophoniste est à …
    a. direction / rigueur
    b. timbre / patient
    c. phoniatre / diction +
    d. je ne sais pas
17. enclume / métacarpe
    a. forgeron / doigt
    b. oreille / paume +
    c. fer / poisson
    d. je ne sais pas
18. ÉCOLOGISTE est à ENVIRONNEMENT ce que ENTOMOLOGISTE est à ..
    a. Maladie
    b. Virus
    c. Biologie
    d. Humain
    e. Insecte +
    f. Je ne sais pas 
19. VERSATILE / CONSTANT , … / …
    a. Initial / Primaire
    b. Principal / Primordial
    c. Pragmatique / Théorique +
    d. Amical / Cordial
    e. Abrupte / Raide
    f. Je ne sais pas
"""

# <codecell>

# fr
raw="""1. vacances / détente
    a. été / hiver
    b. travail / occupation +
    c. soleil / sport
    d. je ne sais pas
2. géologue / dermatologue
    a. conférencier / médecin
    b. pierre / peau +
    c. géographie / spécialiste
    d. je ne sais pas
3. pilote / navigateur
    a. voiture / marin
    b. jet / trimaran +
    c. journal / carte
    d. je ne sais pas
4. CERVEAU est à TÊTE ce que COEUR est à ..
    a. Vie
    b. Thorax +
    c. Poumon
    d. Sang
    e. Respiration
    f. Je ne sais pas
5. FLORE est à VÉGÉTALES ce que FAUNE est à ..
    a. Plantes
    b. Floraux
    c. Campagnes
    d. Animales +
    e. Nourritures
    f. Je ne sais pas
6. KILO est à MILLE ce que HECTO est à …
    a. Cent +
    b. Millier 
    c. Dix
    d. Million
    e. Mille 
    f. Je ne sais pas
7. BANDAGE est à BLESSURE ce que FICELLE est à …
    a. Emballer
    b. Ciseaux
    c. Coupure
    d. Paquet +
    e. Corde
    f. Je ne sais pas
8. PNEU est à VÉLO ce que CORDE est à ..
    a. Linge
    b. Arc +
    c. Ficelle
    d. Sauter
    e. Cou
    f. Je ne sais pas
9. CRAYON est à ÉCRIRE ce que MÈTRE est à ..
    a. Enseigner
    b. Mesurer +
    c. Positionner
    d. Diriger
    e. Disposer
    f. Je ne sais pas
10. PEDIATRE est à … ce que … est à PIED
    a. Main / Pédicure
    b. Homologue / Jambe 
    c. Enfant / Podologue +
    d. Médecin / Humain
    e. Spécialiste / Course
    f. Je ne sais pas
11. BALISER est à .. ce que RUINER est à …
    a. Sablier/Uriner +
    b. Protéger/ Construire 
    c. Peur/Jeux
    d. Flipper/essayer
    e. Jouer/Réunir
    f. Je ne sais pas 
12. BIEN-ÊTRE est à … ce que ORDRE est à ..
    a. Mauvais/Difficulté
    b. Souffrance/Anarchie +
    c. Illusion/Rangement
    d. Repos/Théocratie
    e. Soin/Chemin
    f. Je ne sais pas
13. ÉCRIVAIN / ROMAN , … / …
    a. Chanteur / Musique
    b. Musicien / Parole
    c. Interprète / Partition
    d. Chorégraphe / Chanson
    e. Compositeur / Mélodie +
    f. Je ne sais pas
14. BELLIQUEUX est à … ce que … est à PACIFIQUE
    a. Doux / Calme
    b. Paisible / Violent +
    c. Dangereux / Effrayant
    d. Corsé / Scabreux
    e. Agité / Éloigné
    f. Je ne sais pas
15. LIVIDE est à .. ce que CHARNU est à ..
    a. Exsangue /Pulpeux +
    b. Vivant/ Potelé
    c. Habitable/Agréable
    d. Complet/Plaisant
    e. Inoccupé/Tranchant
    f. Je ne sais pas
16. … est à claustrophobie ce que rougie est à …
    a. clôture / timidité
    b. ascenseur / éreutophobie +
    c. peur / angoisse
    d. je ne sais pas
17. plume / laine
    a. oiseau / tricot
    b. duvet / bourre +
    c. chapeau / brin
    d. je ne sais pas
18. ATHÉE est à CROYANCE ce que INDIGENT est à ..
    a. Argent +
    b. Dignité
    c. Chef
    d. Ambition 
    e. Origine
    f. Je ne sais pas 
19. PERFIDE / INSIDIEUX , … / ....
    a. Pittoresque / Original +
    b. Grand / Minuscule
    c. Joueur / Arbitre
    d. Ciel / Nuage
    e. Eau / Bouteille
    f. Je ne sais pas
"""

# <codecell>

# it 1
raw="""1. pianura : montagna
    a. alto : piccolo
    b. basso : alto +
    c. erba : acqua
    d. non lo so
2. presente : passato
    a. sicurezza : insicurezza
    b. oggi : futuro
    c. mentre : prima +
    d. non lo so
3. vaso : scarpa ***
    a. acqua : piede
    b. vasaio : calzolaio +
    c. vasaio : ciabattino
    d. non lo so
4. VUOTO sta a PIENO come SERA sta a …
    a. Tempo
    b. Fine
    c. Sveglia
    d. Ora
    e. Mattina +
    f. Non lo so
5. PITTORE sta a PENNELLO come SCRIBA sta a …
    a. Matita +
    b. Pagina
    c. Libro
    d. Parola
    e. Carta
    f. Non lo so
6. MELA sta a FRUTTO come MELO sta a…
    a. Raccolta
    b. Tronco
    c. Foglia
    d. Grappolo
    e. Albero +
    f. Non lo so
7. CAMICIA sta a TESSUTO come PNEUMATICO sta a …
    a. Gomma
    b. Catrame
    c. Guida
    d. Strada
    e. Macchina
    f. Non lo so
8. OSCURO sta a NOTTE come CHIARO sta a …
    a. Sole
    b. Ombra
    c. Lampada
    d. Sveglia
    e. Giorno +
    f. Non lo so
9. VELENO sta a MORTE come REATO sta a …
    a. Pane
    b. Trasgressione
    c. Violazione
    d. Pena +
    e. Rottura
    f. Non lo so
10.  ___ sta a BARCA come BENZINA sta a ___
    a. MARE … STRADA
    b. VELA … POMPA
    c. VENTO … MACCHINA +
    d. Non lo so
11. ORNITOLOGO sta a ___ come ___ sta a FRUTTA
    a. GIOIELLO … FRUTTOLOGO
    b. CETACEI … ORTOFRUTTICOLO
    c. UCCELLI … POMOLOGO +
    d. DINOSAURI … MICOLOGO
    e. MAMMIFERI … SINOLOGO
    f. Non  lo so
12. BANALE sta a ___ come SAGGIO sta a ___
    a. SIMPATICO … MAGNIFICO
    b. ORDINARIO … TURBOLENTO
    c. RARO … PRUDENTE
    d. STRAORDINARIO … DISSIPATO +
    e. ORIGINALE … SAGGIO
    f. Non lo so
13.  Intraducibile
14. TANGENTE sta a TOCCARE come SECANTE sta a …
    a. Allontanare
    b. Corrispondere
    c. Tagliare +
    d. Unire
    e. Assemblare
    f. Non lo so
15. PRENDERE sta a ___ come ___ sta a LAVARE
    a. DARE … STIRARE
    b. VENDERE … DARE
    c. VOLERE … SISTEMARE
    d. OFFIRE … RASSETTARE
    e. AFFERRARE … PULIRE +
    f. Non lo so
16.  ___ sta a MODESTO	 come PLEBEO sta a ___
    a. MODICO … TIRANNO
    b. VANITOSO … NOBILE +
    c. FIORE … CAMPO
    d. Non lo so
18. CONFERMA sta a ACCORDO come CONNIVENZA/COMPLICITÀ sta a …
    a. INCANTO
    b. IMMAGINAZIONE
    c. ASTINENZA
    d. COLLUSIONE +
    e. PREVALENZA
    f. Non lo so
19. FILATELICO sta a TIMBRO come ___ sta a ___
    a. FIBULANOMISTA … BANCONOTA
    b. COLOMBOFILO … ISPETTORE
    c. ERPETOFILO … MALATTIA
    d. FILATELICO … LETTERE
    e. MICOFILO … FUNGHO +++
    f. Non lo so
"""

# <codecell>

# it 2
raw="""1. ANNO sta a MESE come 
    a. ROMANZO sta a CAPITOLO +
    b. BISESTILE sta a ESTATE
    c. PIETRA sta a PONTE
    d. Non lo so
2. AUTORE sta a REDATTORE come
    a. ROMANZO sta a EDITORIALE +
    b. ORAFO sta a TIPOGRAFO
    c. LIBRO sta a VOLUME
    d. Non lo so
3. FRASE sta a ___ come  SCALA sta a ___ 
    a. LIBRO ... PIANO
    b. PAROLA ... NOTA +
    c. DISCORSO … SONATA
    d. Non lo so
4. QUADRATO sta a RETTANGOLO come CERCHIO sta a 
    a. SFERA
    b. CURVA
    c. DIAMETRO
    d. ELLISSE +
    e. RAGGIO
    f. Non lo so
5. ANULARE sta a MANO come UNGHIA sta a 
    a. DITO +
    b. SMALTO
    c. PELLE
    d. TAGLIO
    e. PELO
    f. Non lo so
6. GALLINA sta a GALLO come GIUMENTA sta a
    a. PULEDRO
    b. ASINO
    c. FATTORIA
    d. PASCOLO
    e. STALLONE +
    f. Non lo so
7. GRAMMO sta a MASSA come ORA sta a
    a. OROLOGIO
    b. TEMPO +
    c. MINUTO
    d. SETTIMANA
    e. STAGIONE
    f. Non lo so
8. Anagramma
9. FORTEZZA sta a DIFESA come TEATRO sta a …
    a. PUBBLICO
    b. SPETTACOLO
    c. INTRATTENIMENTO +
    d. COMMEDIA
    e. ATTORE
    f. Non lo so
10. ___ sta a GESSO come TELA sta a ___
    a. PASTELLO … BICCHIERE
    b. LAVAGNA … PENNELLO +
    c. PENNELLO … TEMPERA
    d. Non lo so
11. GAMBA sta a ___ come ___ sta a PETTINE
    a. FIORE … MANICO
    b. ATTIVITÀ … PUNTA
    c. CAMMINO … CAPELLO
    d. CORSA … SPAZZOLATURA
    e. TAVOLO … DENTE +
    f. Non lo so
12. PELLE sta a ___ come CERVELLO sta a ___
    a. UROLOGO … CARDIOLOGIO
    b. DERMATOLOGO … UROLOGO
    c. PNEUMOLOGO … CARDIOLOGO
    d. DERMATOLOGO … NEUROLOGO +
    e. GINECOLOGO … NEUROLOGO
    f. Non lo so
13. ABITARE sta a RISIEDERE come 
    a. DISTRARRE sta a ACCOMPAGNARE
    b. ABITARE sta a CAMBIARE
    c. OFFRIRE sta a DONARE +
    d. ASCIUGARE sta a STIRARE
    e. MANGIARE sta a CORRERE
    f. Non lo so
14. INCISIONE sta a BISTURI come SOLCO sta a 
    a. TRINCEA
    b. TERRA
    c. ARATRO +
    d. CANALE
    e. CAMPO
    f. Non lo so
15. ULIVO sta a ___ come ___ sta a PACE
    a. ALBERO … RAGIONE
    b. OLIO … LAVORO
    c. PIANTA … GUERRA
    d. SAPIENZA … COLOMBA + 
    e. GIOIA … TRATTATO
    f. Non lo so
16. ___ sta a AMBASCIATORE come CAPPUCCIO sta a ___
    a. AMBASCIATA … COLLINA
    b. RUOLO … PESCE
    c. PLENIPOTENZIARIO … COPERCHIO +
    d. Non lo so
17. PERSEVERANZA / AVARIZIA
    a. TENACIA / BONTÀ
    b. ACCANIMENTO / DILAPIDARE
    c. VERSATILITÀ / GENEROSITÀ +
    d. Non lo so
18. RIGOROSO sta a INDULGENTE come GIUNONICO sta a
    a. GRACILE +
    b. SCIOVINISTA
    c. CORPOSO
    d. IRASCIBILE
    e. CALOROSO
    f. Non lo so
19. DISPERSIONE sta a DISSIPAZIONE come 
    a. AUMENTO sta a DIMINUZIONE
    b. PROPENSIONE sta a INCLINAZIONE +
    c. ACCUMULAZIONE sta a DIGESTIONE
    d. CREAZIONE sta a GESTIONE
    e. COMUNIONE sta a FUNZIONE
    f. Non lo so 
"""

# <codecell>

# it 3
raw = """1. animale / gabbia
    a. uomo /giardino jardin
    b. uomo / prigione +
    c. uomo / chiusura
    d. non lo so
2. genitori / bambini
    a. famiglia / scuola
    b. professori /allievi +
    c. cugini / cugine
    d. non lo so
3. moscato / conferenza
    a. aperitivo / imitazione
    b. uva / pubblico +
    c. uva / pera 
    d. non lo so
4. MANDATO sta a RICEVUTO come LANCIATO sta a …
    a. Perso
    b. Buttato
    c. Preso +
    d. Letto
    e. Rotto
    f. non lo so
5. UVA sta a VINO come GRANO sta a…
    a. Orzo
    b. Pane +
    c. Alcol
    d. Frutta
    e. Terra
    f. Non lo so 
6. PICCOLO sta a GRANDE come BENEVOLO sta a …
    a. Maldestro
    b. Intraprendente
    c. Temerario
    d. Ostile +
    e. Robusto
    f. Non lo so
8. LETTERA sta a PAROLA come FRASE sta a …
    a. Verbo
    b. Interrogazione
    c. Paragrafo +
    d. Espressione
    e. Libro
    f. Non lo so
9. PESCE sta a MUTO come TALPA sta a ..
    a. Chiacchierone
    b. Furbo
    c. Miope +
    d. Dolce
    e. Testardo
    f. NOn lo so
10. ARTIFICIALE sta a … come … sta a PROFONDO
    a. Pianta /Mare
    b. Realtà / Fabbricato
    c. Fittizio / Personale
    d. Naturale / Superficiale +
    e. Isola / Oceano
    f. NOn lo so
11. CUCINARE sta a… come LAVARE sta a...
    a. Preparare / Comprare
    b. Guardare / Cambiare
    c. Servire / Asciugare +
    d. Vincere/ Smettere
    e. Cuocere/Aggiustare
    f. Non lo so
12. ANNODARE sta a… come VINCERE sta a...
    a. Legare/Perdere
    b. Legare / Trionfare +
    c. Smontare/Incassare
    d. Capovolgere/Percepire
    e. Nodo/Perdita
    f. Non lo so
13. GOLF / IN PIEDI, .../ …
    a. Sci / accovacciato
    b. Tennis / Ginocchio
    c. Cavallo /  a cavalcioni
    d. Nuoto / Seduto 
    e. Scherma/ Allungato
    f. Je ne sais pas
15. EMPATIA sta a .. come ANIMOSITA sta a…
    a. Maldestro/Goia
    b. Egoismo/Odio
    c. Narcisismo/Antipatia
    d. Amore/Scortese
    e. Compassione/Ostilità +
    f. Non lo so
16. … sta a voce come ortofonista sta a…
    a. direttore / rigore
    b. timbro / paziente
    c. foniatra / dizione +
    d. non lo so
17. incudine / metacarpo
    a. fabbro / dito
    b. orecchio / palmo +
    c. ferro / pesce
    d. non lo so
18. ECOLOGISTA sta a  AMBIENTE come ENTOMOLOGO sta a ..
    a. Malattia
    b. Virus
    c. Biologia
    d. Umano
    e. Insetto +
    f. Non lo so
19. VERSATILE / COSTANTE , … / …
    a. Iniziale / Primario
    b. Principale / Primordiale
    c. Pragmatico / Teoretico +
    d. Amicale / Cordiale
    e. Ripida / Rigido
    f. Non lo so
"""

# <codecell>

# it 4
raw = """1. vacanze / riposo
    a. estate / inverno
    b. lavoro / attività +
    c. sole / sport
    d. non lo so
2. geologo / dermatologo
    a. docente / medico
    b. pietra / pelle +
    c. geografia / specialista
    d. non lo so
3. pilota / navigatore
    a. macchina / marinaio
    b. jet / trimarano +
    c. giornale / carta
    d. non lo so
4. CERVELLO sta a TESTA come CUORE sta a...
    a. Vita
    b. Torace +
    c. Polmone
    d. Sangue
    e. Respirazione
    f. Non lo so
5. FLORA sta a VEGETALI come FAUNA sta a  ..
    a. Piante
    b. Floreali
    c. Campagna
    d. Animali +
    e. Cibo
    f. Non lo so
6. CHILO sta a MILLE come ETTO sta a…
    a. Cento +
    b. Migliaia
    c. Dieci
    d. Millione
    e. Mille 
    f. Non lo so
7. BENDA sta a FERITA come  SPAGO sta a ...
    a. Impacchetare
    b. Forbici
    c. Taglio
    d. Paquetto +
    e. Corda
    f. Non lo so
8. RUOTA sta a BICI come CORDA sta a
    a. Panno
    b. Arco +
    c. Spago
    d. Saltare
    e. Collo
    f. Non lo so
9. MATITA sta a SCRIVERE come METRO sta a 
    a. INSEGNARE
    b. MISURARE +
    c. POSIZIONARE
    d. DIRIGERE
    e. DISPORRE
    f. non lo so
10. PEDIATRA  sta a ___ come ___ sta a PIEDE
    a. MANO … PEDICURE
    b. OMOLOGO … GAMBA
    c. BAMBINO … PODOLOGO +
    d. MEDICO … UMANO
    e. SPECIALISTA … CORSA
    f. Non lo so
11. Anagramma
12. BENESSERE sta a ___ come ORDINE sta a ___
    a. NEGATIVO … DIFFICOLTÀ
    b. SOFFERENZA … ANARCHIA +
    c. ILLUSIONE … STIVAGGIO
    d. RIPOSO … TEOCRAZIA
    e. CURA … CAMMINO
    f. Non lo so
13. SCRITTORE sta a ROMANZO come 
    a. CANTANTE sta a MUSICA
    b. MUSICISTA sta a PAROLA
    c. INTERPRETE sta a PARTIZIONE
    d. COREOGRAFO sta a CANZONE
    e. COMPOSITORE sta a MELODIA +
    f. Non lo so
14. BELLICOSO sta a … come .. sta a PACIFICO
    a. Dolce / Calmo
    b. Tranquillo / Violente +
    c. Pericoloso / Spaventoso
    d. Forte / Rischioso
    e. Agitato / Lontano 
    f. Non lo so
15. LIVIDO sta a … come CARNOSO sta a ...
    a. Esangue/ Grassoccio +
    b. Vivo/ Paffuto
    c. Abitabile/ Piacevole
    d. Completo/Gradevole
    e. Disocupato/Tagliente
    f. Non lo so
16. … sta a claustrofobico come arrossito sta a  …
    a. chisusura / timidezza
    b. ascensore/ eritrofobia+
    c. paura / angoscia
    d. non lo so 
17. piuma / lana
    a. uccello / tricot
    b. piumino / bourre +
    c. cappello / brin
    d. je ne sais pas
18. ATEO sta a CREDENZA come INDIGENTE sta a ..
    a. SOLDI +
    b. Dignità
    c. Capo
    d. Ambizione 
    e. Origine
    f. Non lo so 
19. INFIDO / INSIDIOSO , … / ....
    a. Pittoresco / Originale +
    b. Grande / Minuscolo
    c. Giocatore / Arbitro
    d. Cielo / Nuvola
    e. Acqua / Bottiglia
    f. Non lo so
"""

# <codecell>

import re
import json

def parse_questions(raw, question_type):
    questions = []

    def get_raw_question():
        return {'id': None, 'question': None, 'possible_answers': []}


    cur_question = None

    for l in raw.split('\n'):
        if re.match('^\d{1,2}', l):
            if cur_question is not None:
                questions += [cur_question]
            cur_question = get_raw_question()
            match = re.match('^(\d{1,2}|\w{1,2})\. (.*)', l)
            cur_question['id'] = f"{question_type}_{match[1]}"
            cur_question['question'] = match[2].strip()
        if re.match('^\s+\d{1,2}', l):
            match = re.match('^\s+(\d{1,2}|\w{1,2})\. (.*)', l)
            cur_question['possible_answers'] += [{'id': match[1],
                                                  'answer': match[2].split('+')[0].strip()}]

    questions += [cur_question]
    
    return questions

# <codecell>

question_type = 'ct'
language = 'fr'
_id = 2
with open(f'../data/{question_type}_{language}_{_id:0>2}.json', 'w') as f:
    print(parse_questions(raw, 'ct'))
    #json.dump(parse_questions(raw, 'ct'), f, ensure_ascii=False, indent='  ')

# <codecell>

a = [1, 3, 4, 2]

# <codecell>

ls ../data/

# <codecell>


