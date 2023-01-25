from turtle import *
from random import randint, choice

# Définition des fonction basique de dessin

def rectange(l, L):
    forward(l)
    left(90)
    forward(L)
    left(90)
    forward(l)
    left(90)
    forward(L)
    left(90)

def filled_rectange(l, L, fill_color = None):
    color("black", fill_color)
    down()
    begin_fill()
    forward(l)
    left(90)
    forward(L)
    left(90)
    forward(l)
    left(90)
    forward(L)
    left(90)
    end_fill()
    up()

# Définition des fonction pour dessiner un immeuble

def dessine_rez_de_chaussez(x, y, couleur):
    """Dessine le rez de chaussez d'un immeuble.

    Args:
        x (int): coordonnée x pour le début du dessin
        y (int): coordonnée y pour le début du dessin
        couleur (string): couleur du pinceau
    """

    # Initialise la position du pinceau
    goto(x, y)
    seth(0)
    
    # Dessine la facade
    filled_rectange(140, 60, couleur)

    is_door = False
    
    for i in [12, 55, 98]:

        if (randint(0,2)==0 and is_door==False) or (i==98 and is_door==False):
            
            # Dessine une porte
            is_door = True
            goto(x+i, y)
            filled_rectange(30, 45, "#B29057")
        else:
            
            # Dessine une fenêtre
            goto(x+i, y+15)
            filled_rectange(30, 30, "white")

def dessine_etage(x, y, couleur):
    """Dessine un étage d'un immeuble.

    Args:
        x (int): coordonnée x pour le début du dessin
        y (int): coordonnée y pour le début du dessin
        couleur (string): couleur du pinceau
    """

    nbr_etages = randint(0, 4)
    if nbr_etages == 0:
        return 0

    for etage in range(nbr_etages):

        # Initialise la position du pinceau
        goto(x, y+60*(etage+1))
        seth(0)

        # Dessine la facade
        filled_rectange(140, 60, couleur)

        # Dessine les fenetres aux trois emplacements
        for i in [12, 55, 98]:
            goto(x+i, y+60*(etage+1)+15)
            filled_rectange(30, 30, "white")

    return nbr_etages

def dessine_toit(x, y):
    """Dessine le toit d'un immeuble.

    Args:
        x (int): coordonnée x pour le début du dessin
        y (int): coordonnée y pour le début du dessin
    """

    # Initialise la position du pinceau
    goto(x-10, y)
    seth(0)

    # Initialise les paramètre du pinceau
    down()
    color("black")

    # Dessine le toit
    begin_fill()
    seth(0)
    fd(160)
    lt(167.32)
    fd(52)
    fd(30)
    lt(25.36)
    fd(82)
    end_fill()
    up()

def dessine_immeuble(x, y):
    """Dessine un immeuble.

    Args:
        x (int): coordonnée x pour le début du dessin
        y (int): coordonnée y pour le début du dessin
    """

    building_color = choice(["#8DA656", "#E8DA7C", "#D9A362", "#F26968", "#F2AA96", "#C279F2", "#CD9DFF", "#6F71E8", "#87C3FF", "#A3E7E8", "#7AD3A6", "#4D9E66"])

    dessine_rez_de_chaussez(x, y, building_color)
    nbr_etages = dessine_etage(x, y, building_color)
    dessine_toit(x, y + (nbr_etages+1)*60)

def dessine_rue(nbr_immeubles):
    speed(10)
    for i in range(nbr_immeubles):
        dessine_immeuble(i*160, 0)

dessine_rue(10)
done()