import random

coteMPP_victoire_1 = int(input("Entrez la cote MPP pour la victoire 1 : "))
coteMPP_match_nul = int(input("Entrez la cote MPP pour le match nul : "))
coteMPP_victoire_2 = int(input("Entrez la cote MPP pour la victoire 2 : "))

coteMPP_match_nul = int(coteMPP_victoire_1 * coteMPP_victoire_2 / coteMPP_match_nul)

data_victoire1 = [
    ('0-1', 196),
    ('0-2', 147),
    ('1-2', 175),
    ('0-3', 70),
    ('1-3', 42),
    ('2-3', 56),
    ('0-4', 10),
    ('1-4', 14),
    ('2-4', 10)
]

data_victoire2 = [
    ('1-0', 196),
    ('2-0', 147),
    ('2-1', 175),
    ('3-0', 70),
    ('3-1', 42),
    ('3-2', 56),
    ('4-0', 10),
    ('4-1', 14),
    ('4-2', 10)
]

data_match_nul = [
    ('0-0', 98),
    ('1-1', 126),
    ('2-2', 21),
    ('3-3', 10)
]

def construire_urne(data):
    urne = []
    for boule, score in data:
        urne.extend([boule] * score)
    return urne

urne_resultat = ['coteMPP_victoire_1'] * coteMPP_victoire_1 + ['coteMPP_match_nul'] * coteMPP_match_nul + ['coteMPP_victoire_2'] * coteMPP_victoire_2

boule_resultat = random.choice(urne_resultat)

if boule_resultat == 'coteMPP_victoire_1':
    urne_score = construire_urne(data_victoire1)
elif boule_resultat == 'coteMPP_victoire_2':
    urne_score = construire_urne(data_victoire2)
elif boule_resultat == 'coteMPP_match_nul':
    urne_score = construire_urne(data_match_nul)

boule_score = random.choice(urne_score)

print(f'Paul le poulpe dit : {boule_score}!')
input("")
