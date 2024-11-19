"""Paramètres à l’envers"""
import sys

# Fonctions utilisées

# Partie 1 : Gestion d'erreur

def check_several_arrguments(arguments) :
    if len(arguments) < 1 :
        print("erreur, vous devez saisir plusieurs arguments")
        sys.exit()
      
# Partie 2 : Parsing
arguments = sys.argv[1:]


# Partie 3 : Résolution
check_several_arrguments(arguments)

for i in arguments[::-1] :
    print(i, end=" ")
print("\n")

# Partie 4 : Affichage

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