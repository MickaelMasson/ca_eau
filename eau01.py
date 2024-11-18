"""Combinaisons de 2 numbers"""

# Fonctions utilisées
def diplay_combinations() :
    combination_list = []

    for i in range(100) :
        i = str(i).zfill(2)
        for j in range(100) :
            j = str(j).zfill(2)
            if i < j :
                combination_list.append(f"{i} {j}")
    
    print(", ".join(combination_list))

# Partie 1 : Gestion d'erreur

# Partie 2 : Parsing

# Partie 3 : Résolution

# Partie 4 : Affichage
diplay_combinations()

"""
Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.


Exemples d’utilisation :
$> python exo.py
00 01, 00 02, 00 03, 00 04, ... , 00 99, 01 02, ... , 97 99, 98 99
$>

"""