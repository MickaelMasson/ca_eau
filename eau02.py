"""Paramètres à l’envers"""
import sys

# Fonctions utilisées
def reversed_arguments(arguments) :
    reverse_arguments = []
    for i in range(len(arguments)-1, -1, -1) :
        reverse_arguments.append(arguments[i])
    return reverse_arguments

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 1 :
        print("erreur, vous devez saisir au moins un argument")
        return False
    return True

# Partie 2 : Parsing
def get_arguments ():
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_reverse_list () :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    print("\n".join(reversed_arguments(get_arguments())))

# Partie 4 : Affichage
display_reverse_list()

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