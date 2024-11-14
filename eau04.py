"""Prochain nombre premier"""

# Fonctions utilisées

def verifie_nombre_premier(valeur):
    for i in range(2, int(valeur) - 1) :
        resultat_division = int(valeur) / i 
        if int(resultat_division) * i == int(valeur) :
            nombre_entier = False
            break
    else :
        nombre_entier = True
    return nombre_entier # booleen


def nombre_entier_suivant(valeur):
    valeur = valeur +1
    while verifie_nombre_premier(valeur) is False:
        valeur += 1
    else: 
        entier_suivant = valeur
    return entier_suivant


# Partie 1 : Gestion d'erreur

def argument_autorise(argument) :
    try:
        if int(argument) > 0 and argument.isdigit :
            reponse = True
        else:
            reponse = False
            print(-1)
        return reponse
    except ValueError:
        print(-1)


# Partie 2 : Parsing
argument = input()


# Partie 3 : Résolution
if argument_autorise(argument) :
    print(nombre_entier_suivant(int(argument)))


# Partie 4 : Affichage

"""


1h30 pour faire cet exercice. 
Principal difficulté: 
- toujours la structure, bien différencier les 5 parties
- la derniere partie entre ésolution et affichage je vois pas trop comment le séparer dans ce cas
- la gestion des erreurs, esque definir un fonction qui vérifie 
  l'input est bien avec un try puis except

Ce que j'ai appris : 
- mieux compris le .isdigit qui revoit direct un booleen sans avoir besoin de faire un == ou autre
"""