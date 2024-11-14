"""String dans string"""

# Fonctions utilisées

def comparer_arguments(liste_argument):
    argument_a = liste_argument[0]
    argument_b = liste_argument[1]
    if (argument_a in argument_b) or (argument_b in argument_a):
        reponse = True
    else:
        reponse = False
    return reponse


# Partie 1 : Gestion d'erreur

def check_input(arguments_input):
    try:
        if " " in arguments_input :
            liste_argument = arguments_input.split()
            argument_a = liste_argument[0]
            argument_b = liste_argument[1]
        else :
            print("error")
            exit()
            
    except ValueError:
        print("error ValueError")
    except UnboundLocalError:
        print("error UnboundLocalError")

    return ([argument_a, argument_b])


# Partie 2 : Parsing

arguments = input()


# Partie 3 : Résolution

if comparer_arguments(check_input(arguments)):
    print("true")

else :
    print("false")

# Partie 4 : Affichage

"""


1h pour faire cet exercice. 
Principal difficulté: 
- nommer les variables et les fonctions
- j'ai du sorti une liste plutot que 2 arguments dans check_input() 
  car j'avais une erreur comme quoi il me manquait l'argument b 
  en entrée de comparer_arguments(), j'ai donc du avoir une liste à
  l'entrée puis la séparer a nouveau
Ce que j'ai appris : 
- le exit() pour arrter le script 


Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.


Exemples d’utilisation :
$> python exo.py bonjour jour
true


$> python exo.py bonjour joure
false


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""