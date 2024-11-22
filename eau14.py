"""Par ordre Ascii"""
import sys

# Fonctions utilisées
def sort_ascii(arguments) :
    for i in range(len(arguments)) :
        min = i
        for j in range(i + 1, len(arguments)) :
            if ord(arguments[j][0]) < ord(arguments[min][0]) :
                min = j
        arguments[min], arguments[i] = arguments[i], arguments[min]
    string_ascending_ascii_order = " ".join(map(str, arguments))
    return string_ascending_ascii_order


# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 2 :
        print("Vous devez saisir au moins deux valeurs")
        return False
    return True
    
def is_alpha(arguments):
    for argument in arguments :
        if not argument.isalpha() :
            print("Vous devez saisir des arguments composés de lettres a-z / A-Z")
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
    if not is_alpha(get_arguments()) :
        return
    print(sort_ascii(get_arguments()))
# Partie 4 : Affichage
display()
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