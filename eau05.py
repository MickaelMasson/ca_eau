"""String dans string"""
import sys
# Fonctions utilisées
def is_string_in_string(arguments):
    first_argument = arguments[0]
    second_argument = arguments[1]
    if (first_argument in second_argument) or (second_argument in first_argument):
        return True
    else:
        return False

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments):
    if len(arguments) != 2 :
        print("Error, vous devez saisir 2 arguments")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_is_corresponding() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    print(is_string_in_string(get_arguments()))

# Partie 4 : Affichage
display_is_corresponding()
"""


1h pour faire cet exercice. 
Principal difficulté: 
- nommer les variables et les fonctions
- j'ai du sorti une liste plutot que 2 arguments dans is_valid_number_of_arguments() 
  car j'avais une erreur comme quoi il me manquait l'argument b 
  en entrée de is_string_in_string(), j'ai donc du avoir une liste à
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