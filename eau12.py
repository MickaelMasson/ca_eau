"""Tri à bulle"""
import sys

# Fonctions utilisées
def get_bubble_sort(numbers: list[int]) -> list[int] :
    for i in range(len(numbers) - 1) :
        for j in range(len(numbers) - 1) :
            if numbers[j] > numbers[j + 1] :
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

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
def display_bubble_sort() :
    arguments = get_arguments()
    min_number_of_argument_expected = 3
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return
    for argument in arguments :
        if not is_digit(argument) :
            return
    numbers = list(map(int, arguments))
    print(" ".join(map(str, get_bubble_sort(numbers))))
# Partie 4 : Affichage

display_bubble_sort()
"""
Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri à bulle.

Vous utiliserez une fonction de cette forme (selon votre langage) :
my_bubble_sort(array) {
	# votre algorithme
	return (new_array)
}


Exemples d’utilisation :
$> python exo.py 6 5 4 3 2 1
1 2 3 4 5 6


$> python exo.py test test test
error

Afficher error et quitter le programme en cas de problèmes d’arguments.


Wikipedia vous présentera une belle description de cet algorithme de tri.


XXhXXm pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""