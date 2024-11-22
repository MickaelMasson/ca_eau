"""Combinaisons de 3 chiffres"""

# Fonctions utilisées
def get_combination() :
    combination = []
    for i in range(10) :
        for j in range(i + 1, 10) :
            for k in range(j + 1, 10) :
                combination.append(f"{i}{j}{k}")
    return combination
             
# Partie 1 : Gestion d'erreur

# Partie 2 : Parsing

# Partie 3 : Résolution
def display_combination() :
    print(", ".join(get_combination()))

# Partie 4 : Affichage
display_combination()
"""
Créez un programme qui affiche toutes les différentes combinaisons possibles 
de trois chiffres dans l’ordre croissant, dans l’ordre croissant. 
La répétition est volontaire.

Exemples d’utilisation :
$> python exo.py
012, 013, 014, 015, 016, 017, 018, 019, 023, 024, ... , 789
$>

987 n’est pas là parce que 789 est présent.

020 n’est pas là parce que 0 apparaît deux fois.

021 n’est pas là parce que 012 est présent.

000 n’est pas là parce que cette combination ne comporte pas exclusivement des chiffres différents les uns des autres."""