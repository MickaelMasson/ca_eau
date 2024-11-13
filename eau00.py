"""Combinaisons de 3 chiffres"""

##### 2eme version
# Fonctions utilisées

##  Vérifier si chaque chiffre est unique dans le nombre
#       nombre doit etre un str
#       la reponse est un booleen
def verifie_chiffre_unique(nombre) :
    centaine = nombre[0]
    dixaine = nombre[1]
    unite = nombre[2]
    reponse = centaine != dixaine and centaine != unite and dixaine != unite
    return reponse


##  Ranger chaque chiffre par ordre croissant
#       nombre doit etre un str
#       combinaison est un str("123")
def combinaison_ordre_croissant(nombre) :
    centaine = int(nombre[0])
    dixaine = int(nombre[1])
    unite = int(nombre[2])
    combinaison_liste = [centaine, dixaine, unite]
    combinaison_liste.sort()
    combinaison = "".join(str(e) for e in combinaison_liste)
    return combinaison

# Partie 1 : Gestion d'erreur

# Partie 2 : Parsing

# Partie 3 : Résolution
nombres = [str(i).zfill(3) for i in range(1000)]
liste_combinaisons = []
liste_combinaisons_utilise = []

for i in nombres :
    if verifie_chiffre_unique(i) and (combinaison_ordre_croissant(i) not in liste_combinaisons_utilise) :
        liste_combinaisons.append(i)
        liste_combinaisons_utilise.append(combinaison_ordre_croissant(i))

# Partie 4 : Affichage
print(", ".join(liste_combinaisons))

"""
3h30 pour faire la v1 de cet exercice. 
1h30 pour la v2
Principal difficulté: 
- j'ai fais l'erreur ligne 13 d'avoir mit les arguments entre[] la reponse de la fonction n'était pas True mais [True]
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
liste_combinaisons = []
liste_combinaisons_utilise = []

for i in premiere_liste :
    for i in deuxieme_liste :
        for i in troisieme_liste:
            if premier_chiffre != deuxieme_chiffre and premier_chiffre != troisieme_chiffre and deuxieme_chiffre != troisieme_chiffre :
                liste_combinaisons_desordre = [premier_chiffre, deuxieme_chiffre, troisieme_chiffre]
                liste_combinaisons_croissant = sorted(liste_combinaisons_desordre)
                if liste_combinaisons_croissant not in liste_combinaisons_utilise :
                    liste_combinaisons.append(f"{premier_chiffre}{deuxieme_chiffre}{troisieme_chiffre}")
                    liste_combinaisons_utilise.append(liste_combinaisons_croissant)
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
print(", ".join(liste_combinaisons))

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
liste_combinaisons = []
liste_combinaisons_utilise = []

for i in premiere_liste :
    for i in deuxieme_liste :
        for i in troisieme_liste:
            if premier_chiffre != deuxieme_chiffre and premier_chiffre != troisieme_chiffre and deuxieme_chiffre != troisieme_chiffre :
                liste_combinaisons_desordre = [premier_chiffre, deuxieme_chiffre, troisieme_chiffre]
                liste_combinaisons_croissant = sorted(liste_combinaisons_desordre)
                if liste_combinaisons_croissant not in liste_combinaisons_utilise :
                    liste_combinaisons.append(f"{premier_chiffre}{deuxieme_chiffre}{troisieme_chiffre}")
                    liste_combinaisons_utilise.append(liste_combinaisons_croissant)
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
print(", ".join(liste_combinaisons))
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

000 n’est pas là parce que cette combinaison ne comporte pas exclusivement des chiffres différents les uns des autres.

######################################

3h30m pour faire la v1 de cet exercice. 
Principal difficulté: 
- Je me suis grandement compliqué a utilisé 3 range, une pour les unité, 
  une pour les dixaine et la derniere pour les centaines
Ce que j'ai appris : 
- 
"""