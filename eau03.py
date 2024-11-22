"""Suite de Fibonacci"""
import sys

# Fonctions utilisées
def calculate_fibonacci(arguments) :
    index = int(arguments[0])
    fibonacci_list = [0, 1]
    for i in range(1, index) :
        result = fibonacci_list[-1] + fibonacci_list[-2]   
        fibonacci_list.append(result)
    return result

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) != 1 :
        print("-1")
        return False
    return True

def is_digit(arguments) :
    argument = arguments[0]
    if not argument.isdigit() :
        print("-1")
        return False
    return True

# Partie 2 : Parsing
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_result() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    if not is_digit(get_arguments()) :
        return
    print(calculate_fibonacci(get_arguments()))

# Partie 4 : Affichage
display_result()
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