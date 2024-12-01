"""
"""

# Fonctions utilisées

# Partie 1 : Gestion d'erreur
def is_valid_agruments(arguments: list, index_number: int) -> bool :
    if not len(arguments) > index_number :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True

def is_digit(string: str) -> bool:
    for character in string :
        if not "0" <= character <= "9" :
            print(f"Error, '{string}' n'est pas un nombre entier positif")
            return False
    return True

def is_positive_or_negative_digit(string: str) -> bool :
    string = string.lstrip("-")
    for character in string :
        if not "0" <= character <= "9" :
            print(f"Error, '{string}' n'est pas un nombre entier positif")
            return False
    return True

def is_positive_number(number: int) -> bool :
    if number < 0 :
        print(f"Error, '{number}' n'est pas un nombre valide, vous devez saisir un nombre posittif")
        return False
    return True

def is_alpha(letter: str) -> bool :
    if not "a" <= letter <= "z" and not "A" <= letter <= "Z" :
        print(f"Error, '{letter}' n'est pas un caractère Alpha")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution

# Partie 4 : Affichage
print("J'ai terminé l'épreuve de l'Eau et c'était enrichissant.")
"""


XXhXXm pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""