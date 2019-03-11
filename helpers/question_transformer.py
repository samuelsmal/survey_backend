# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

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
            match = re.match('^(\d{1,2})\. (.*)', l)
            cur_question['id'] = f"{question_type}_{match[1]}"
            cur_question['question'] = match[2].strip()
        if re.match('^    \d{1,2}', l):
            match = re.match('^    (\d{1,2})\. (.*)', l)
            cur_question['possible_answers'] += [{'id': match[1],
                                                  'answer': match[2].split('+')[0].strip()}]

    questions += [cur_question]
    
    return questions

# <codecell>

question_type = 'ct'
language = 'fr'
with open(f'../data/{question_type}_{language}.json', 'w') as f:
    json.dump(parse_questions(raw, 'ct'), f, ensure_ascii=False, indent='  ')

# <codecell>


