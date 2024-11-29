"""Différence minimum absolue"""
import sys

# Fonctions utilisées
def get_min_difference(numbers: list) -> int:
    min_difference = 0
    i = 1
    for first_number in numbers :
        for second_number in numbers[i:] :
            if first_number > second_number :
                if (first_number - second_number) < min_difference or min_difference == 0 :
                    min_difference = (first_number - second_number)
            else:
                if (second_number - first_number) < min_difference or min_difference == 0 :
                    min_difference = (second_number - first_number)
        i += 1
    return min_difference

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) < number_of_argument :
        print("Error, vos arguments ne sont pas valide")
        return False
    return True

def is_digit(string: str) -> bool:
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
def display_min_difference():
    arguments = get_arguments()
    min_number_of_argument_expected = 2
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return
    for argument in arguments :
        if not is_digit(argument) :
            return
    numbers = list(map(int, arguments))
    print(get_min_difference(numbers))

# Partie 4 : Affichage
display_min_difference()
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