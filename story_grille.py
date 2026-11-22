from grille import Grille

g = Grille(5, 8)
print(g)
x = int(input("Entrez la colonne : "))
y = int(input("Entrez la ligne : "))
g.tirer(y, x)
print(g)