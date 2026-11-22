from bateau import Bateau
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin


def test_init():
    bateau = Bateau(2, 3)
    assert bateau.ligne == 2
    assert bateau.colonne == 3
    assert bateau.longueur == 1
    assert bateau.vertical == False


def test_positions_horizontal():
    bateau = Bateau(2, 3, longueur=3)
    assert bateau.positions() == [(2, 3), (2, 4), (2, 5)]


def test_positions_vertical():
    bateau = Bateau(2, 3, longueur=3, vertical=True)
    assert bateau.positions() == [(2, 3), (3, 3), (4, 3)]


def test_coule():
    grille = Grille(3, 5)
    bateau = Bateau(1, 1, longueur=3)
    grille.ajoute(bateau)
    assert bateau.coulé(grille) == False
    grille.tirer(1, 1)
    grille.tirer(1, 2)
    grille.tirer(1, 3)
    assert bateau.coulé(grille) == True


def test_types_bateaux():
    grille = Grille(5, 5)
    porte_avion = PorteAvion(0, 0)
    croiseur = Croiseur(1, 0)
    torpilleur = Torpilleur(2, 0)
    sous_marin = SousMarin(3, 0)
    grille.ajoute(porte_avion)
    grille.ajoute(croiseur)
    grille.ajoute(torpilleur)
    grille.ajoute(sous_marin)
    assert grille.grille[0] == "🚢"
    assert grille.grille[5] == "⛴"
    assert grille.grille[10] == "🚣"
    assert grille.grille[15] == "🐟"