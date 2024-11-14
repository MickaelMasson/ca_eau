"""Paramètres à l’envers"""

# Fonctions utilisées

## separe les arguments

def separe_arguments(string_argument) :
    try :
        if '"' in string_argument :
            liste_argument = string_argument.strip('"').split('" "')

        elif '"' not in string_argument :
            liste_argument = string_argument.split()
    except ValueError :
        print("valuesError")
    return liste_argument
   

## récupère le dernier argument de la liste et le supprime

def liste_a_l_envers(liste_arguments) :
    nouvelle_liste = []
    for i in range(len(liste_arguments)) :
        dernier_argument_liste = liste_arguments[-1]
        nouvelle_liste.append(dernier_argument_liste)
        liste_arguments = liste_arguments[:-1]
    return nouvelle_liste


# Partie 1 : Gestion d'erreur

# Partie 2 : Parsing
arguments_utilisateur = input()


# Partie 3 : Résolution
liste_a_l_envers = liste_a_l_envers(separe_arguments(arguments_utilisateur))


# Partie 4 : Affichage
print("\n".join(liste_a_l_envers))
"""


1h05 pour faire cet exercice. 
Principal difficulté: 
- la fonction strip pour retirer des caractères en partant 
  du début et de la fin de la string.
- la gestion des erreurs, je ne vois pas quels serais les 
  erreurs et comment les regrouper dans la partie 1
Ce que j'ai appris : 
- 

Créez un programme qui affiche ses arguments reçus à l’envers.


Exemples d’utilisation :
$> python exo.py “Suis” “Je” “Drôle”
Drôle
Je
Suis


$> python exo.py ha ho
ho
ha

$> python exo.py “Bonjour 36”
Bonjour 36

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""