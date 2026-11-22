class Grille:

    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.vide = "∿"
        self.grille = [self.vide] * (lignes * colonnes)

    def tirer(self, ligne, colonne, touche="x"):
        indice = ligne * self.colonnes + colonne
        self.grille[indice] = touche

    def __str__(self):
        resultat = ""

        for ligne in range(self.lignes):
            debut = ligne * self.colonnes
            fin = debut + self.colonnes
            resultat += "".join(self.grille[debut:fin]) + "\n"
        return resultat.rstrip("\n")

    def ajoute(self, bateau):
        positions = bateau.positions()

        for ligne, colonne in positions:
            if ligne < 0 or ligne >= self.lignes:
                return
            if colonne < 0 or colonne >= self.colonnes:
                return

        for ligne, colonne in positions:
            indice = ligne * self.colonnes + colonne
            self.grille[indice] = bateau.marque
