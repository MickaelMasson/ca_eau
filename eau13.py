"""Tri par sélection"""
import sys

# Fonctions utilisées
def sort_selection(arguments) :
    numbers = list(map(int, arguments))
    for i in range(len(numbers)) :
        min = i
        for j in range(i + 1, len(numbers)) :
            if numbers[j] < numbers[min] :
                min = j
        numbers[min], numbers[i] = numbers[i], numbers[min]
    string_ascending_order = " ".join(map(str, numbers))
    return string_ascending_order

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 3 :
        print("Error, vous dezvez saisir au moins 2 arguments")
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
def display() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    if not is_digit(get_arguments()) :
        return
    print(sort_selection(get_arguments()))

# Partie 4 : Affichage
display()
"""
Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri par sélection.

Vous utiliserez une fonction de cette forme (selon votre langage) :
my_select_sort(array) {
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

"""