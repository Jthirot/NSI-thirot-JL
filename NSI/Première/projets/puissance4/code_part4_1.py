from module_part4 import *
from p5 import *


def preload() :
    global FLECHE_JAUNE,FLECHE_ROUGE
    # on définie la variable fleche_jaune qui contiendra un objet image
    FLECHE_JAUNE = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/06-18/15-34-01/flehce_jaune.jpg")
    FLECHE_ROUGE = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/06-18/15-19-31/flehce_rouge.jpg")

def setup() :
    createCanvas(300, 400) # on crée une fenêtre de 100x100 pixels
    background("#ivory")  # on choisi une couleur pour le fond

def image_cliquee(x,y) :
    """
    IN : x et y : coordonnées du clic
    OUT :
        - si on a cliqué dans la zone des images : la fonction renvoie le numéro de l'image cliquée
        - Sinon : elle renvoie -1
    """
    global LARGE,HAUT,DECAL_X,DECAL_Y,NB_IMAGES
    
    if DECAL_X <= x <= DECAL_X + NB_IMAGES * LARGE and DECAL_Y <= y <= DECAL_Y + HAUT :
        return int(x-DECAL_X)//LARGE
    return -1

def clic() :
    global CLIC_EN_COURS
    global JOUEUR,GRILLE
   
    if mouseIsPressed :
        if not CLIC_EN_COURS :          # si un clic n'est pas deja en cours
            CLIC_EN_COURS = True        # alors on met clic_en_cours à True pour bloquer d'autre exécution
            num = image_cliquee(mouseX,mouseY)
            if num >= 0 :
                GRILLE = joue_jeton(GRILLE,JOUEUR,num)
                JOUEUR = 3 - JOUEUR
    else :
        CLIC_EN_COURS = False           # le bouton est relaché, on remet clic_en_cours à False

def affiche_grille(x,y) :
    """
    Dession une grille constituée de 7 lignes, contenant chacune 7 carrés.
    La couleur des carrés est (0,0,200), leur taille est indiquée par la variable globale LARGE.
    Le premier carré est déssiné aux coordonnées x,y reçues en paramètres.
    """
    global LARGE,HAUT
    
    for ligne in range(6) :
        for colonne in range(7) :
            fill(0,0,200)
            square(x+colonne*LARGE, y+ligne*LARGE, LARGE)
            pion(x+colonne*LARGE , y+ligne*LARGE, ligne, colonne)
    
def pion(x,y,i,j) :
    global GRILLE,LARGE
    centre_x = x + LARGE//2
    centre_y = y + LARGE//2
    if GRILLE[i][j] == 0 : color="white"
    elif GRILLE[i][j] == 1 : color="red"
    else : color="yellow"
    
    fill(color)
    circle(centre_x,centre_y,LARGE * 3 //4,)
    
def draw() :
    global LARGE,DECAL_X,DECAL_Y,NB_IMAGES
    global FLECHE_JAUNE,FLECHE_ROUGE,JOUEUR
    
    if JOUEUR == 1 :
        fleche = FLECHE_ROUGE
    else :
        fleche = FLECHE_JAUNE
        
    for i in range(NB_IMAGES) :
        # on dessine l'image
        image(fleche, DECAL_X + i*LARGE,DECAL_Y)
        
    affiche_grille(DECAL_X,DECAL_Y+56)
    
    clic()
    
####################################################
###                PROGRAMME PRINCIPAL          ####
####################################################

# initialisation de la grille
GRILLE = creation_grille_vierge()

# largeur/hauteur des images :
LARGE = 40
HAUT = 56
NB_IMAGES = 7

# position des images 
DECAL_X = 10
DECAL_Y = 40

# lancement :
JOUEUR = 1
CLIC_EN_COURS = False

run()