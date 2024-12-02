"""Chiffres only"""
import sys

# Fonctions utilisées
def is_digit(string: str) -> bool:
    for character in string :
        if not "0" <= character <= "9" :
            return False
    return True

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) != number_of_argument :
        print("Error, vos arguments ne sont pas valide")
        return False
    return True

# Partie 2 : Parsing
def get_arguments()-> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_is_digit() :
    arguments = get_arguments()
    number_of_argument_expected = 1
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    argument = arguments[0]
    print(is_digit(argument))
    
# Partie 4 : Affichage
display_is_digit()
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