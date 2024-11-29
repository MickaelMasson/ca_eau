"""Prochain nombre premier"""
import sys

# Fonctions utilisées
def is_prime_number(number: int) -> bool :
    for i in range(2, number - 1) :
        if number % i == 0 :
            return False
    return True

def get_next_prime_number(number: int) -> int :
    new_number = number + 1
    
    while is_prime_number(new_number) is False :
        new_number += 1
    else : 
        return new_number

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool :
    if len(arguments) != number_of_argument :
        print("Error, vos arguments ne sont pas valide")
        return False
    return True

def is_digit(string: str) -> bool :
    for character in string :
        if not "0" <= character <= "9" :
            print(f"Error, '{string}' n'est pas un nombre entier positif")
            return False
    return True

def is_valid_number(number: int) -> bool :
    if number < 1 :
        print(f"Error, {number} n'est pas un nombre valide")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_next_prime_number() :
    arguments = get_arguments()
    number_of_argument_expected = 1
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    argument = arguments[0]
    if not is_digit(argument) :
        return
    number = int(argument)
    if not is_valid_number(number) :
        return
    print(get_next_prime_number(number))

# Partie 4 : Affichage
display_next_prime_number()
"""
Prochain nombre premier

Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.


Exemples d’utilisation :
$> python exo.py 14
17
$>

Afficher -1 si le paramètre est négatif ou mauvais.
"""