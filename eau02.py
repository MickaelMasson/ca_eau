"""Paramètres à l’envers"""
import sys

# Fonctions utilisées
def get_reverse_arguments(arguments: list) -> list :
    reverse_arguments = []
    for i in range(len(arguments)-1, -1, -1) :
        reverse_arguments.append(arguments[i])
    return reverse_arguments

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool :
    if len(arguments) < number_of_argument :
        print("Error, vos arguments ne sont pas valide")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_reversed_arguments() :
    arguments = get_arguments()
    min_number_of_argument_expected = 1
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return
    print("\n".join(get_reverse_arguments(arguments)))

# Partie 4 : Affichage
display_reversed_arguments()

"""

Créez un programme qui affiche ses arguments reçus à l’envers.


Exemples d’utilisation :
$> python exo.py “Suis” “Je” “Drôle”
Drôle
Je
Suis


$> python exo.py ha ho
ho
ha

$> python exo.py “Bonjour 36”
Bonjour 36

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""