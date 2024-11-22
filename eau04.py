"""Prochain nombre premier"""
import sys

# Fonctions utilisées
def is_prime_number(number) :
    for i in range(2, number - 1) :
        if number % i == 0 :
            return False
    return True

def calculate_next_prime_number(arguments) :
    number = int(arguments[0])
    number = number + 1
    
    while is_prime_number(number) is False :
        number += 1
    else : 
        return number

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) != 1 :
        print(-1)
        return False
    return True
    
def is_digit(arguments) :
    argument = arguments[0]
    if not argument.isdigit() :
        print(-1)
        return False
    return True

def is_valid_number(arguments) :
    number = int(arguments[0])
    if number < 1 :
        print(-1)
        return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_next_prime_number() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    if not is_digit(get_arguments()) :
        return
    if not is_valid_number(get_arguments()) :
        return
    print(calculate_next_prime_number(get_arguments()))

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