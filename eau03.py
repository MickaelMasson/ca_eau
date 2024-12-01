"""Suite de Fibonacci"""
import sys

# Fonctions utilisées
def get_fibonacci(index_number: int) -> int:
    fibonacci_list = [0, 1]
    for _i in range(1, index_number) :
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    result_fibonacci = fibonacci_list[-1]
    return result_fibonacci

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool :
    if len(arguments) != number_of_argument :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True

def is_digit(string: str) -> bool:
    for character in string :
        if not "0" <= character <= "9" :
            print(f"Error, '{string}' n'est pas un nombre entier positif")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list:
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_fibonacci() :
    arguments = get_arguments()
    number_of_argument_expected = 1
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    argument = arguments[0]
    if not is_digit(argument) :
        return
    index_number = int(argument)
    print(get_fibonacci(index_number))

# Partie 4 : Affichage
display_fibonacci()
"""


1h pour faire cet exercice. 
Principal difficulté: 
- la gestion des erreur, je n'arrive pas a regrouper les erreurs dans la partie 1
Ce que j'ai appris : 
- 

Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.

Exemples d’utilisation :
$> python exo.py 3
2
$>

Afficher -1 si le paramètre est négatif ou mauvais.

"""