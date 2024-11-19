"""Suite de Fibonacci"""
import sys

# Fonctions utilisées
def calculate_fibonacci(index) :
    fibonacci_list = [0, 1]
    for i in range(1, index) :
        result = fibonacci_list[-1] + fibonacci_list[-2]   
        fibonacci_list.append(result)
    return result


# Partie 1 : Gestion d'erreur
def check_arguments(arguments) :
    error = ("-1")

    if len(arguments) != 1 :
        print(error)
        sys.exit()
    
    argument = arguments[0]

    if not argument.isdigit() :
        print(error)
        sys.exit()

# Partie 2 : Parsing
arguments = sys.argv[1:]

# Partie 3 : Résolution
check_arguments(arguments)
number = int(arguments[0])
result_fibonacci = calculate_fibonacci(number)

# Partie 4 : Affichage
print(result_fibonacci)
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