"""Combinaisons de 2 nombres"""

# Fonctions utilisées

##  Vérifier si chaque nombre est unique dans la combinaison
#       nombre doit etre une liste
#       la reponse est un booleen
def verifie_nombre_unique(combinaison) :
    premier_nombre = combinaison[0]
    deuxieme_nombre = combinaison[1]
    reponse = premier_nombre != deuxieme_nombre
    return reponse

##  Ranger les nombres par ordre croissant
#       nombres doit etre une liste
#       combinaison est un str("00 01")
def combinaison_ordre_croissant(nombres) :
    premier_nombre = int(nombres[0])
    deuxieme_nombre = int(nombres[1])
    combinaison_liste = [premier_nombre, deuxieme_nombre]
    combinaison_liste.sort()
    combinaison = " ".join(str(e) for e in combinaison_liste)
    return combinaison
# Partie 1 : Gestion d'erreur

# Partie 2 : Parsing

# Partie 3 : Résolution
nombre_0_99 = [str(i).zfill(2) for i in range(100)]

liste_combinaisons = []
liste_combinaisons_utilise = []

for i in nombre_0_99 :
    for y in nombre_0_99 :
        if verifie_nombre_unique([i, y]) and (combinaison_ordre_croissant([i, y]) not in liste_combinaisons_utilise) :
            liste_combinaisons.append(f"{i} {y}")
            liste_combinaisons_utilise.append(combinaison_ordre_croissant([i, y]))

# Partie 4 : Affichage
print(", ".join(liste_combinaisons))

"""


40m pour faire cet exercice. 
Principal difficulté: 
- pas vraiment, le seul détail qui n'a pas fonctionné au premier essaie a la ligne 37 
  ou j'insérais une liste ([i, y]) dans une autre liste et la fonction join ne fonctonnais pas pour l'affichage
Ce que j'ai appris : 
- pas dans cet exercice, c'était très similaire au premier.

Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.


Exemples d’utilisation :
$> python exo.py
00 01, 00 02, 00 03, 00 04, ... , 00 99, 01 02, ... , 97 99, 98 99
$>


"""