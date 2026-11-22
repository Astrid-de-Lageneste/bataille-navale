from bateau import Bateau

# Cas 1 : les deux bateaux se chevauchent

b1 = Bateau(2, 3, longueur=3)
b2 = Bateau(2, 5, longueur=3)

positions_b1 = b1.positions()
positions_b2 = b2.positions()

chevauchement = False

for position in positions_b1:
    if position in positions_b2:
        chevauchement = True

print("Les bateaux se chevauchent :", chevauchement)


# Cas 2 : les deux bateaux ne se chevauchent pas

b1 = Bateau(2, 3, longueur=3)
b2 = Bateau(3, 3, longueur=3, vertical=True)

positions_b1 = b1.positions()
positions_b2 = b2.positions()

chevauchement = False

for position in positions_b1:
    if position in positions_b2:
        chevauchement = True

print("Les bateaux se chevauchent :", chevauchement)