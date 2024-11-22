"""Majuscule"""
import sys

# Fonctions utilisées
def is_alpha(letter) :
    if letter.isalpha() :
        return True
    else :
        return False

def get_title_upper(arguments) :
    argument = arguments[0]
    new_string = ""
    last_letter_is_space = True
    for i in range(len(argument)) :
        letter = argument[i]
        if is_alpha(letter) :
            if last_letter_is_space :
                new_string = new_string + letter.upper()
                last_letter_is_space = False
            else :
                new_string = new_string + letter.lower()
                last_letter_is_space = False
        else :        
            if letter == " " or letter == "\n" or letter == "\t" :
                new_string = new_string + letter
                last_letter_is_space = True
            else :
                new_string = new_string + letter
                last_letter_is_space = False
    return new_string

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) != 1 :
        print("error")
        return False
    return True
    
# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_title_string() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    print(get_title_upper(get_arguments()))

# Partie 4 : Affichage
display_title_string()
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