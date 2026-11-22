from grille import Grille
from bateau import Bateau


def test_init():
    grille = Grille()
    assert grille is not None


def test_init():
    grille = Grille(3, 4)
    assert grille.lignes == 3
    assert grille.colonnes == 4
    assert grille.vide == "∿"
    assert grille.grille == ["∿", "∿", "∿", "∿", "∿", "∿", "∿", "∿", "∿", "∿", "∿", "∿"]


def test_tirer():
    grille = Grille(3, 4)
    grille.tirer(1, 2)
    assert grille.grille[6] == "x"


def test_str():
    g = Grille(5, 8)
    assert str(g) == ("∿∿∿∿∿∿∿∿\n" "∿∿∿∿∿∿∿∿\n" "∿∿∿∿∿∿∿∿\n" "∿∿∿∿∿∿∿∿\n" "∿∿∿∿∿∿∿∿")
    g.tirer(2, 3)
    assert str(g) == ("∿∿∿∿∿∿∿∿\n" "∿∿∿∿∿∿∿∿\n" "∿∿∿x∿∿∿∿\n" "∿∿∿∿∿∿∿∿\n" "∿∿∿∿∿∿∿∿")


def test_ajoute_bateau_horizontal():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=False))
    assert g.grille == ["∿", "∿", "∿", "⛵", "⛵", "∿"]


def test_ajoute_bateau_vertical_trop_long():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=True))
    assert g.grille == ["∿", "∿", "∿", "∿", "∿", "∿"]
    g.ajoute(Bateau(1, 0, longueur=4, vertical=True))
    assert g.grille == ["∿", "∿", "∿", "∿", "∿", "∿"]