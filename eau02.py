"""Paramètres à l’envers"""
import sys

# Fonctions utilisées
def reverse_arguments(arguments) :
    reverse_arguments = []
    for i in range(len(arguments)-1, -1, -1) :
        reverse_arguments.append(arguments[i])
    return reverse_arguments

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments) :
    if len(arguments) < 2 :
        return print("Error, vous devez saisir au moins deux arguments")
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_reversed_list () :
    arguments = get_arguments()
    if not is_valid_arguments(arguments) :
        return
    print("\n".join(reverse_arguments(arguments)))

# Partie 4 : Affichage
display_reversed_list()

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