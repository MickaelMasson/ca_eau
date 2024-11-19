"""Prochain nombre premier"""
import sys

# Fonctions utilisées
def check_prime_number(number):
    number = int(number)
    for i in range(2, number - 1) :
        if number % i == 0 :
            nombre_entier = False
            break
    else :
        nombre_entier = True
    return nombre_entier # booleen

def calculate_next_prime_number(number):
    number = number +1
    
    while check_prime_number(number) is False:
        number += 1
    else: 
        next_prime_number = number
    return next_prime_number

# Partie 1 : Gestion d'erreur
def check_arguments(arguments) :
    error = -1

    if len(arguments) != 1 :
        print(error)
        sys.exit()
    
    argument = arguments[0]

    if not argument.isdigit() :
        print(error)
        sys.exit()

    number = int(argument)

    if number < 1 :
        print(error)
        sys.exit()

# Partie 2 : Parsing
arguments = sys.argv[1:]

# Partie 3 : Résolution
check_arguments(arguments)
number = int(arguments[0])
next_prime_number = calculate_next_prime_number(number)

# Partie 4 : Affichage
print(next_prime_number)

"""
Prochain nombre premier

Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.


Exemples d’utilisation :
$> python exo.py 14
17
$>

Afficher -1 si le paramètre est négatif ou mauvais.
"""