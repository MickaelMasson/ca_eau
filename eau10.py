"""Index wanted"""
import sys

# Fonctions utilisées
def get_index_wanted(search_base:list , index: str) -> str:
    for i in range(len(search_base)) :
        if search_base[i] == index :
            index_wanted = str(i)
            return index_wanted
    index_wanted = "Error, -1"
    return index_wanted

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) < number_of_argument :
        print("Error, le nombe d'arguments n'est pas valide")
        return False
    return True

# Partie 2 : Parsing
def get_arguments()-> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_index_wanted() :
    arguments = get_arguments()
    min_number_of_argument_expected = 2
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return
    index = arguments[-1]
    search_base = arguments[:-1]
    print(get_index_wanted(search_base, index))

# Partie 4 : Affichage
display_index_wanted()
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