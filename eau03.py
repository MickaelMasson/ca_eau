"""Suite de Fibonacci"""

# Fonctions utilisées
def suite_fibonacci(nombre) :
    liste_fibonacci = [0, 1]
    for i in range(nombre - 1) :
        resultat = liste_fibonacci[-1] + liste_fibonacci[-2]   
        liste_fibonacci.append(resultat)
    return resultat

def argument_conforme(valeur) :
    if int(valeur) > 1 :
        resultat_conformite = valeur
    else :
        resultat_conformite = -1
    return resultat_conformite


# Partie 1 : Gestion d'erreur


# Partie 2 : Parsing
argument = input()

# Partie 3 : Résolution

try :
    if argument_conforme(int(argument)) != -1 :
        print(suite_fibonacci(int(argument)))
    else:
        print(-1)

except ValueError :
    print(-1)


# Partie 4 : Affichage

"""


1h pour faire cet exercice. 
Principal difficulté: 
- la gestion des erreur, je n'arrive pas a regrouper les erreurs dans la partie 1
Ce que j'ai appris : 
- 

Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.

Exemples d’utilisation :
$> python exo.py 3
2
$>

Afficher -1 si le paramètre est négatif ou mauvais.

"""