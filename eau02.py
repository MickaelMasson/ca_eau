"""Paramètres à l’envers"""
import sys

# Fonctions utilisées
def reversed_arguments(arguments) :
    reverse_arguments = []
    for i in range(len(arguments)-1, -1, -1) :
        reverse_arguments.append(arguments[i])
    return reverse_arguments

def display_arguments(arguments) :
    for i in arguments : 
        print(i)

# Partie 1 : Gestion d'erreur
def check_number_of_arguments(arguments) :
    if len(arguments) < 1 :
        print("erreur, vous devez saisir au moins un argument")
        sys.exit()      

# Partie 2 : Parsing
arguments = sys.argv[1:]

# Partie 3 : Résolution
check_number_of_arguments(arguments)
reverse_arguments = reversed_arguments(arguments)

# Partie 4 : Affichage
display_arguments(reverse_arguments)

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