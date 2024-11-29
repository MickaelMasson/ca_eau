"""Entre min et max"""
import sys

# Fonctions utilisées
def get_consecutive_number(first_number: int, second_number: int) -> list :
    consecutive_number = []
    if first_number < second_number :
        for i in range(first_number, second_number) :
            consecutive_number.append(str(i))
    else:
        for i in range(first_number, second_number, -1) :
            consecutive_number.append(str(i))
    return consecutive_number

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool :
    if len(arguments) != number_of_argument :
        print("Error, vos arguments ne sont pas valide")
        return False
    return True

def is_digit(string: str) -> bool :
    string = string.lstrip("-")
    for character in string :
        if not "0" <= character <= "9" :
            print(f"Error, '{string}' n'est pas un nombre entier positif")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_consecutive_number() :
    arguments = get_arguments()
    number_of_argument_expected = 2
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    for argument in arguments :
        if not is_digit(argument) :
            return
    first_number = int(arguments[0])
    second_number = int(arguments[1])
    consecutive_number = get_consecutive_number(first_number, second_number)
    print(" ".join(consecutive_number))

# Partie 4 : Affichage
display_consecutive_number()
"""
Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.


Exemples d’utilisation :
$> python exo.py 20 25
20 21 22 23 24


$> python exo.py 25 20
20 21 22 23 24

$> python exo.py hello
error

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""