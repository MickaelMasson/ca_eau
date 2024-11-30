"""Par ordre Ascii"""
import sys

# Fonctions utilisées
def sort_ascii_order(arguments: list[str]) -> list[str]:
    ascii_arguments = []
    for ascii_argument in arguments :
        ascii_sub_list = []
        for ascii_character in ascii_argument :
            ascii_sub_list.append(ord(ascii_character))
        ascii_arguments.append(ascii_sub_list)

    for i in range(len(ascii_arguments)) :
        min = i
        for j in range(i + 1, len(ascii_arguments)) :
            if ascii_arguments[j] < ascii_arguments[min] :
                min = j
        ascii_arguments[min], ascii_arguments[i] = ascii_arguments[i], ascii_arguments[min]

    new_arguments = []
    for ascii_argument in ascii_arguments :
        new_sub_arguments = []
        for ascii_character in ascii_argument :
            new_sub_arguments.append(chr(ascii_character))
        new_sub_arguments = "".join(new_sub_arguments)
        new_arguments.append(new_sub_arguments)

    ascii_order_list = list(map(str.title, new_arguments))
    return ascii_order_list

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool :
    if len(arguments) < number_of_argument :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True

# Partie 2 : Parsing
def get_arguments()-> list :
    arguments = sys.argv[1:]
    #arguments = ["mickael", "Matthieu", "marie", "david", "Alfred", "margot", "MARIE"]
    return arguments

# Partie 3 : Résolution
def display_sort_ascii() :
    arguments = get_arguments()
    min_number_of_argument_expected = 2
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return
    lower_arguments = list(map(str.lower, arguments))
    print(" ".join(sort_ascii_order(lower_arguments)))

# Partie 4 : Affichage
display_sort_ascii()
"""
Créez un programme qui trie les éléments donnés en argument par ordre ASCII.

Exemples d’utilisation :
$> python exo.py Alfred Momo Gilbert
Alfred Gilbert Momo

$> python exo.py A Z E R T Y
A E R T Y Z

Afficher error et quitter le programme en cas de problèmes d’arguments.


XXhXXm pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""