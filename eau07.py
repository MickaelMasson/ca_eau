"""Majuscule"""
import sys

# Fonctions utilisées
def is_alpha(character: str) -> bool :
    if not "a" <= character <= "z" and not "A" <= character <= "Z" :
        return False
    return True

def get_title_upper(argument: str) -> str :
    argument = argument.lower()
    new_string = ""
    last_character_is_space = True
    for character in argument :
        if is_alpha(character) and last_character_is_space :
            new_string = new_string + character.upper()
            last_character_is_space = False
        elif character == " " or character == "\n" or character == "\t" :
            new_string = new_string + character
            last_character_is_space = True
        else :
            new_string = new_string + character
            last_character_is_space = False
    return new_string

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool :
    if len(arguments) != number_of_argument :
        print("Error, vos arguments ne sont pas valide")
        return False
    return True

def is_only_digit(string: str) -> bool:
    for character in string :
        if not "0" <= character <= "9" :
            return False
    print("Error, l'argument attendu ne peut pas etre un nombre")    
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_title_upper() :
    arguments = get_arguments()
    number_of_argument_expected = 1
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    argument = arguments[0]
    if is_only_digit(argument) :
        return
    print(get_title_upper(argument))

# Partie 4 : Affichage
display_title_upper()
"""
Créez un programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères. 
Les autres lettres devront être en minuscules. Les mots ne sont délimités que par un espace, 
une tabulation ou un retour à la ligne.


Exemples d’utilisation :
$> python exo.py “bonjour mathilde, comment vas-tu ?!”
Bonjour Mathilde, Comment Vas-tu ?!


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.


XXhXXm pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""