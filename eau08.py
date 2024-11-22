"""Chiffres only"""
import sys

# Fonctions utilisées
def is_digit(arguments) :
    argument = arguments[0]
    for i in argument :
        if not i in "0123456789" :
            return False
    return True

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) != 1 :
        print("error")
        return False
    return True

# Partie 2 : Parsing
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return 
    print(is_digit(get_arguments()))
# Partie 4 : Affichage
display()
"""
Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres.

Exemples d’utilisation :
$> python exo.py “4445353”
true


$> python exo.py 42
true

$> python exo.py “Bonjour 36”
false

Afficher error et quitter le programme en cas de problèmes d’arguments.


XXhXXm pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""