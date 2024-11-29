"""Majuscule sur deux"""
import sys

# Fonctions utilisées
def is_alpha(character: str) -> bool :
    if not "a" <= character <= "z" and not "A" <= character <= "Z" :
        return False
    return True

def get_alter_upper_lower(argument: str) -> str :
    new_string = ""
    last_character_is_upper = False
    for character in argument :
        if is_alpha(character) and last_character_is_upper :
            new_string = new_string + character
            last_character_is_upper = False
        elif is_alpha(character) :
            new_string = new_string + character.upper()
            last_character_is_upper = True
        else :        
            new_string = new_string + character
    return new_string

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) != number_of_argument :
        print("Error, vos arguments ne sont pas valide")
        return False
    return True

def is_only_digit(string: str) -> bool:
    for character in string :
        if not "0" <= character <= "9" :
            return False
    print(f"Error, l'argument attendu ne peut pas etre un nombre")    
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_alter_upper_lower() :
    arguments = get_arguments()
    number_of_argument_expected = 1
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    argument = arguments[0]
    if is_only_digit(argument) :
        return
    print(get_alter_upper_lower(argument))

# Partie 4 : Affichage
display_alter_upper_lower()

"""Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. 
Seule les lettres (A-Z, a-z) sont prises en compte.

Exemples d’utilisation :
$> python exo.py “Hello world !”
HeLlO wOrLd !

$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments."""