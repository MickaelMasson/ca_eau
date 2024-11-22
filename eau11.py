"""Différence minimum absolue"""
import sys

# Fonctions utilisées
def get_ascending_order(arguments) :
    numbers = [int(argument) for argument in arguments]
    numbers_ascending_order = sorted(numbers)
    return numbers_ascending_order

def get_min_difference(numbers) :
    min_difference = numbers[1] - numbers[0] 
    for i in range(len(numbers) -1) :
        if numbers[i + 1] - numbers[i] < min_difference :
            min_difference = numbers[i + 1] - numbers[i]
    return min_difference

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 2 :
        print("Error, vous devez saisir deux valeus minimum")
        return False
    return True
    
def is_digit(arguments) :
    for argument in arguments :
        if not argument.lstrip("-").isdigit() :
            print("Error, tous vos arguments doivent être des nombrre entiers")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display():
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    if not is_digit(get_arguments()) :
        return
    print(get_min_difference(get_ascending_order(get_arguments())))

# Partie 4 : Affichage
display()
"""
Créez un programme qui affiche la différence minimum absolue entre deux éléments 
d’un tableau constitué uniquement de nombres. Nombres négatifs acceptés.

Exemples d’utilisation :
$> python exo.py 5 1 19 21
2

$> python exo.py 20 5 1 19 21
1

$> python exo.py -8 -6 4
2

Afficher error et quitter le programme en cas de problèmes d’arguments.


XXhXXm pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""