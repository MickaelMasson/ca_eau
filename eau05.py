"""String dans string"""
import sys
# Fonctions utilisées
def is_string_in_string(first_string: str, second_string: str) -> bool :
    if len(first_string) > len(second_string) :
        main_string = first_string
        sub_string = second_string
    else:
        main_string = second_string
        sub_string = first_string
        
    for i in range(len(main_string) - len(sub_string) + 1) :
        if main_string[i:i + len(sub_string)] == sub_string :
            return True
    return False

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool :
    if len(arguments) != number_of_argument :
        print(f"Error, Vous devez saisir {number_of_argument} arguments")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_is_corresponding() :
    arguments = get_arguments()
    number_of_argument_expected = 2
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    first_string = arguments[0]
    second_string = arguments[1]
    print(is_string_in_string(first_string, second_string))

# Partie 4 : Affichage
display_is_corresponding()
"""
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