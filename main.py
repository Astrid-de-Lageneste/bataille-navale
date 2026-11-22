import random
from termcolor import colored

from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

grille = Grille(8, 10)

bateaux = [PorteAvion(0, 0), Croiseur(0, 0), Torpilleur(0, 0), SousMarin(0, 0)]

for bateau in bateaux:
    placements_possibles = []
    for ligne in range(grille.lignes):
        for colonne in range(grille.colonnes):
            for vertical in [False, True]:
                bateau.ligne = ligne
                bateau.colonne = colonne
                bateau.vertical = vertical
                positions = bateau.positions()
                dans_grille = True
                for l, c in positions:
                    if l < 0 or l >= grille.lignes or c < 0 or c >= grille.colonnes:
                        dans_grille = False
                sans_chevauchement = True
                if dans_grille:
                    for l, c in positions:
                        indice = l * grille.colonnes + c
                        if grille.grille[indice] != grille.vide:
                            sans_chevauchement = False
                if dans_grille and sans_chevauchement:
                    placements_possibles.append((ligne, colonne, vertical))
    ligne, colonne, vertical = random.choice(placements_possibles)
    bateau.ligne = ligne
    bateau.colonne = colonne
    bateau.vertical = vertical


coups = 0

while len(bateaux) > 0:
    print(grille)
    ligne = int(input("Ligne : "))
    colonne = int(input("Colonne : "))
    coups += 1

    touche = False
    for bateau in bateaux:
        if (ligne, colonne) in bateau.positions():
            touche = True
            grille.tirer(ligne, colonne, "💣")
            print(colored("Touché !", "red"))
            if bateau.coulé(grille):
                print(colored(bateau.message, "green"))
                for l, c in bateau.positions():
                    indice = l * grille.colonnes + c
                    grille.grille[indice] = bateau.marque
                bateaux.remove(bateau)
            break

    if not touche:
        grille.tirer(ligne, colonne)
        print(colored("Plouf dans l'eau !", "blue"))


print(grille)
print("Bravo ! Vous avez détruit tous les bateaux.")
print("Nombre de coups :", coups)