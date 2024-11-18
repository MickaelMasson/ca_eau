"""Combinaisons de 3 chiffres"""

# Fonctions utilisées
def check_single_number(number) :
    hundred = number[0]
    ten = number[1]
    unit = number[2]
    answer = hundred != ten and hundred != unit and ten != unit
    return answer

def arrange_ascending_order(number) :
    hundred = int(number[0])
    ten = int(number[1])
    unit = int(number[2])
    combination_list = [hundred, ten, unit]
    combination_list.sort()
    combination = "".join(str(figure) for figure in combination_list)
    return combination

# Partie 1 : Gestion d'erreur

# Partie 2 : Parsing

# Partie 3 : Résolution
numbers = [str(number).zfill(3) for number in range(1000)]
combination_list = []
used_combination_list = []

for number in numbers :
    if check_single_number(number) and (arrange_ascending_order(number) not in used_combination_list) :
        combination_list.append(number)
        used_combination_list.append(arrange_ascending_order(number))

# Partie 4 : Affichage
print(", ".join(combination_list))

"""
3h30 pour faire la v1 de cet exercice. 
1h30 pour la v2
Principal difficulté: 
- j'ai fais l'erreur ligne 13 d'avoir mit les arguments entre[] la answer de la fonction n'était pas True mais [True]
  Ce qui me renvoyais toujours dans False l39. j'ai passé enormément de temps a faire des print() des fonctions 
  et des résultats 
Ce que j'ai appris : 
- la version 1 est sans les fonction et je ne comprenais pas comment suivre la trame de Harry expliqué dans la video. 
  j'ai continuer le cours et j'ai appris les fonctions et comment les appeler.
- zfill
- quand une fonction renvoie un booleen pas besoin de mettre if == True juste le rappel de la fonction suffit.




premier_chiffre = 0
deuxieme_chiffre = 0
troisieme_chiffre = 0
combination_list = []
used_combination_list = []

for i in premiere_liste :
    for i in deuxieme_liste :
        for i in troisieme_liste:
            if premier_chiffre != deuxieme_chiffre and premier_chiffre != troisieme_chiffre and deuxieme_chiffre != troisieme_chiffre :
                combination_list_desordre = [premier_chiffre, deuxieme_chiffre, troisieme_chiffre]
                combination_list_croissant = sorted(combination_list_desordre)
                if combination_list_croissant not in used_combination_list :
                    combination_list.append(f"{premier_chiffre}{deuxieme_chiffre}{troisieme_chiffre}")
                    used_combination_list.append(combination_list_croissant)
                    troisieme_chiffre += 1
                else : 
                    troisieme_chiffre += 1
            else :
                troisieme_chiffre += 1
        troisieme_chiffre = 0    
        deuxieme_chiffre += 1
    premier_chiffre += 1
    deuxieme_chiffre = 0



# Partie 1 : Gestion d'erreur

# Partie 2 : Parsing

# Partie 3 : Résolution

# Partie 4 : Affichage
print(", ".join(combination_list))

"""
"""
##### 1ere version
# Fonctions utilisées

premiere_liste = list(range(10))
deuxieme_liste = list(range(10))
troisieme_liste = list(range(10))
premier_chiffre = 0
deuxieme_chiffre = 0
troisieme_chiffre = 0
combination_list = []
used_combination_list = []

for i in premiere_liste :
    for i in deuxieme_liste :
        for i in troisieme_liste:
            if premier_chiffre != deuxieme_chiffre and premier_chiffre != troisieme_chiffre and deuxieme_chiffre != troisieme_chiffre :
                combination_list_desordre = [premier_chiffre, deuxieme_chiffre, troisieme_chiffre]
                combination_list_croissant = sorted(combination_list_desordre)
                if combination_list_croissant not in used_combination_list :
                    combination_list.append(f"{premier_chiffre}{deuxieme_chiffre}{troisieme_chiffre}")
                    used_combination_list.append(combination_list_croissant)
                    troisieme_chiffre += 1
                else : 
                    troisieme_chiffre += 1
            else :
                troisieme_chiffre += 1
        troisieme_chiffre = 0    
        deuxieme_chiffre += 1
    premier_chiffre += 1
    deuxieme_chiffre = 0



# Partie 1 : Gestion d'erreur

# Partie 2 : Parsing

# Partie 3 : Résolution

# Partie 4 : Affichage
print(", ".join(combination_list))
"""


"""
Créez un programme qui affiche toutes les différentes combinaisons possibles de trois chiffres dans l’ordre croissant, dans l’ordre croissant. La répétition est volontaire.

Exemples d’utilisation :
$> python exo.py
012, 013, 014, 015, 016, 017, 018, 019, 023, 024, ... , 789
$>

987 n’est pas là parce que 789 est présent.

020 n’est pas là parce que 0 apparaît deux fois.

021 n’est pas là parce que 012 est présent.

000 n’est pas là parce que cette combination ne comporte pas exclusivement des chiffres différents les uns des autres.

######################################

3h30m pour faire la v1 de cet exercice. 
Principal difficulté: 
- Je me suis grandement compliqué a utilisé 3 range, une pour les unité, 
  une pour les ten et la derniere pour les hundreds
Ce que j'ai appris : 
- 
"""