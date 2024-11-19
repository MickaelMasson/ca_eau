"""String dans string"""
import sys
# Fonctions utilisées
def compare_arguments(arguments):
    first_argument = arguments[0]
    second_argument = arguments[1]
    if (first_argument in second_argument) or (second_argument in first_argument):
        awnser = True
    else:
        awnser = False
    return awnser

# Partie 1 : Gestion d'erreur
def check_arguments(arguments_input):
    if len(arguments) != 2 :
        print("Error, vous devez saisir 2 arguments")
        sys.exit()

# Partie 2 : Parsing
arguments = sys.argv[1:]

# Partie 3 : Résolution
check_arguments(arguments)
is_corresponding = compare_arguments(arguments)

# Partie 4 : Affichage
print(is_corresponding)
"""


1h pour faire cet exercice. 
Principal difficulté: 
- nommer les variables et les fonctions
- j'ai du sorti une liste plutot que 2 arguments dans check_arguments() 
  car j'avais une erreur comme quoi il me manquait l'argument b 
  en entrée de compare_arguments(), j'ai donc du avoir une liste à
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