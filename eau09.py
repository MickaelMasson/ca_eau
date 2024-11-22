"""Entre min et max"""
import sys

# Fonctions utilisées
def values_list(arguments) :
    start_of_list = int(arguments[0])
    end_of_list = int(arguments[1])
    values_list = []
    for i in range(start_of_list, end_of_list) :
        values_list.append(str(i))
    values = " ".join(values_list)
    return values
    

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) != 2 :
        print("error, vous devez saisir 2 arguments")
        return False
    return True
    
def is_digit(arguments) :
    for argument in arguments :
        if not argument.lstrip("-").isdigit() :
            print("vos arguments doivent être des nombrre entiers")
            return False
    return True

def is_ascending_order(arguments) :
    if arguments[0] < arguments[1] :
        print("vos arguments doivent être dans l'ordre croissants")
        return True
    return False

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
    if not is_ascending_order(get_arguments()) :
        return
    print(values_list(get_arguments()))

# Partie 4 : Affichage
display()
"""
Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.


Exemples d’utilisation :
$> python exo.py 20 25
20 21 22 23 24


$> python exo.py 25 20
20 21 22 23 24

$> python exo.py hello
error

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""