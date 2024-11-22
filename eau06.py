"""Majuscule sur deux"""
import sys

# Fonctions utilisées
def is_alpha(letter) :
    if letter.isalpha() :
        return True
    else :
        return False

def get_alter_upper_lower(arguments) :
    argument = arguments[0]
    new_string = ""
    last_letter_is_upper = False
    for i in range(len(argument)) :
        letter = argument[i]
        if is_alpha(letter) :
            if last_letter_is_upper :
                new_string = new_string + letter.lower()
                last_letter_is_upper = False
            else :
                new_string = new_string + letter.upper()
                last_letter_is_upper = True
        else :        
            new_string = new_string + letter
    return new_string

# Partie 1 : Gestion d'erreur
def is_valid_number_arguments (arguments) :
    if len(arguments) != 1 :
        print("Error, vous devez saisir une seule chaine de caractère")
        return False
    return True

def is_digit_argument (arguments) :
    argument = arguments[0]
    if argument.isdigit() :
        print("Error, vous devez saisir une seule chaine de caractère avec a-z/A-Z")
        return False
    return True
    
# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_new_string() :
    if not is_valid_number_arguments(get_arguments()) :
        return
    if not is_digit_argument(get_arguments()) :
        return
    print(get_alter_upper_lower(get_arguments()))

# Partie 4 : Affichage
display_new_string()

"""Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. 
Seule les lettres (A-Z, a-z) sont prises en compte.

Exemples d’utilisation :
$> python exo.py “Hello world !”
HeLlO wOrLd !

$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments."""