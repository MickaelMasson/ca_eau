"""Index wanted"""
import sys

# Fonctions utilisées
def keyword(arguments) :
    keyword = arguments[-1]
    return keyword

def find_keyword(arguments) :
    for i in range(len(arguments) - 1) :
        if arguments[i] == keyword(arguments) :
            index = i
            return index
    index = -1
    return index

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 2 :
        print("error")
        return False
    return True

# Partie 2 : Parsing
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    print(find_keyword(get_arguments()))

# Partie 4 : Affichage
display()
"""
Créez un programme qui affiche le premier index d’un élément recherché dans un tableau. 
Le tableau est constitué de tous les arguments sauf le dernier. 
L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé.


Exemples d’utilisation :
$> python exo.py Ceci est le monde qui contient Charlie un homme sympa Charlie
6


$> python exo.py test test test
0

$> python exo.py test boom
-1

Afficher error et quitter le programme en cas de problèmes d’arguments.


XXhXXm pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""