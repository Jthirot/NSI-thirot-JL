from random import randint,seed
from time import sleep


def creation_grille_vierge():
    ''' Cette fonction va créer un plateau de jeu vide. Les case vides sont représentées par par des "."
    
        IN: Rien
        OUT:la fonction renvoie une grille vierge
        
        C'est une liste, chaque élément étant lui même une liste de string :  ["-","-","-","-","-","-","-"] 
        C'est donc une liste de liste contentant 6 élément, chaqun d'eux étant une liste de 7 string, toutes égales à ".".
        
        Voila la grille vierege que l'on doit donc fabriquer :
            [ ["-","-","-","-","-","-","-"] , 
              ["-","-","-","-","-","-","-"] ,
              ...
              ["-","-","-","-","-","-","-"]  ]  
              
    '''

    grille_vierge = []
    # Pour chaque ligne
    for num_ligne in range(6):
        nouvelle_ligne = [] # on crée un nouveau tableau vide en mémoire
        for j in range(7): # On ajoute les sept éléments ".", séparémment.
            nouvelle_ligne.append("-")
            
        # On ajoute la nouvelle ligne à la grille
        grille_vierge.append(nouvelle_ligne)
    
    # Le travail est terminé, la variable globale grille est remplie, on quitte la procédure
    return grille_vierge


def affiche_grille(grille) -> None :
    ''' Cette fonction affiche la grille de jeu telle que ci-dessous
    IN: Rien
    OUT: La fonction renvoie une chaine de caractères contenant l'affichage comme ci-dessous : 
    
    Affichage souhaitée :
       0 1 2 3 4 5 6 
    0 |.|.|.|.|.|.|.|
    1 |.|.|.|.|.|.|.|
    2 |.|.|.|.|.|.|.|
    3 |.|.|.|.|.|.|.|
    4 |.|.|.|X|.|.|.|
    5 |O|X|.|X|O|X|O|
      ---------------
    '''
    
    # Initialisation :
    # créez une chaine affichage contenant la 1ere ligne
    # vous ajouterez \n en fin de ligne pour obtenir un retour à la ligne
    affichage = "   0 1 2 3 4 5 6\n"
    
    # Affichage des lignes
    for i in range(6): # Pour chaque ligne i
        # ajoutez le numéro de ligne plus un espace dans la chaine affichage
        affichage += str(i)+" "
        for j in range(7): # Pour chaque colonne j
            # ajoutez "|" plus la valeur de l'élément situé dans la case (ligne i, colonne j)
            affichage += "|"+ grille[i][j]
        # pour terminer la ligne, ajoutez un "|\n" dans affichage
        affichage += "|\n"
    # Affichage du trait en bas de la grille
    affichage += " "+"-"*15
    return affichage

def colonne_pleine(grille,indice_colonne) -> bool:
    '''
        IN: indice de la colonne à analyser (0 à 6)
        OUT: un booleen (True si la colonne est déjà pleine, False sinon)
    '''
    
    # il suffit de tester si l'élément à la ligne 0 de cette colonne est égal à '.'
    if grille[0][indice_colonne] != "-" : return True
    return False

def joue_jeton(grille, symboles, num_joueur, indice_colonne) -> None:
    ''' Place un jeton du joueur numéros num_joueur, dans la colonne indice_colonne.
    
        IN: num_joueur (int qui vaut 1 ou 2)
        OUT: la fonction renvoie la grille modifiée
    '''

    # Dans la colonne indice_colonne, en partant, du bas, on cherche la première case vide.
    # on suppose que la colonne n'est pas pleine, ce problème sera traité ailleur.
    
    for ligne in range(5,-1,-1) :
        if grille[ligne][indice_colonne] == '-' :
            grille[ligne][indice_colonne] = symboles[num_joueur]
            return grille
        
def demander_ou_jouer(grille,joueur) -> int:
    ''' Doit demander au joueur dans quel indice de colonne il souhaite jouer.
        Si l'indice n'est pas valable (non compris entre 0 et 6), ou bien s'il correspond à une colonne pleine, on lui indique
        que sa saisie est incorrecte et on lui renouvelle la question.
        Si l'utilisateur saisie 'q' (pour "Quitter"), la partie doit se terminer.
        IN: rien
        OUT: Renvoie un indice de colonne (int) valable (colonne non pleine) où l'on peut jouer.
        Si on entre 'q' la fonction renverra -1
    '''
    
    # on demande ou le joueur veux jouer.
    # on crée un massage (pour input) contenant l'affichage de la grille 
    # qu'on concatène avec la question (précédée d'un retour à la ligne):
    message = affiche_grille(grille)+"\nJOUEUR :"+str(joueur)+" dans quelle colonne jouez vous (0 à 6) ?"
    saisie = input(message)

    # on doit vérifier la saisie. On commence une boucle infinie
    # c'est une boucle while dont on ne peux sortir que losque l'on aura fait une saisie correcte
    # (dans ce cas, la fonction renvoie le nombre saisi)
    while True:
        
        # if faut que la longueur du texte entré soit égale à 1, et que 
        # ce texte soit un nombre 0-6, ou la lettre q
        
        if len(saisie)==1 and (saisie in "0123456q"):
            #La saisie est correct (1 seul caractère et il est autorisé)
            
            # on  traite le cas ou on a entré "q" :
            if saisie=="q" :
                return -1
                
            # On vérifie que la colonne n'est pas pleine
            # il faut convertir l'entrée en int, puis appeler colonne_pleine
            j = int(saisie)
            
            if colonne_pleine(grille,j):
                # on refait un input, en modifint un peu le message :
                saisie = input("ATTENTION, cette colonne est déjà pleine !\n"+message)
            else: #Sinon, il y a encore de la place 
                # On renvoie l'indice de la colonne choisie
                return j
        else:
            # La saisie est incorrecte, on refait un input en modifiant le message :
            saisie = input("SAISIE INCORRECTE\n"+message)

def quatre_jetons_en_ligne(grille,symboles, num_joueur) -> bool:
    '''
        IN: 
            grille : une liste de listes modélisant le plateau
            symboles : dictionnaires définissant les jetons des 2 joueurs
            num_joueur; Numéros du joueur à détecter (1 ou 2)
        OUT: booleen (True si 4 jetons alignés trouvés en ligne, False sinon)
    '''
    
    # définition du jeton à trouver
    jeton = symboles[num_joueur]
    chaine_a_trouver = jeton * 4
    
    for ligne in range(6):
        ligne_txt = "".join(grille[ligne])
        if chaine_a_trouver in ligne_txt :
            return True

    # Si on arrive ici, c'est qu'aucun alignement de 4 jetons n'a été trouvé en ligne
    return False

def quatre_jetons_en_colonne(grille,symboles,num_joueur):
    '''
        IN: 
            grille : une liste de listes modélisant le plateau
            symboles : dictionnaires définissant les jetons des 2 joueurs
            num_joueur; Numéros du joueur à détecter (1 ou 2)
        OUT: booleen (True si 4 jetons alignés trouvés en colonne, False sinon)
    '''
    
    # définition du jeton à trouver
    jeton = symboles[num_joueur]
    chaine_a_trouver = jeton * 4
    for colonne in range(7):
        colonne = [grille[i][colonne] for i in range(6)]
        colonne_txt = "".join(colonne)
        if chaine_a_trouver in colonne_txt :
            return True

    # Si on arrive ici, c'est qu'aucun alignement de 4 jetons n'a été trouvé en ligne
    return False

def quatre_jetons_diagonal_1(grille,symboles, num_joueur) -> bool:
    '''
        IN: 
            grille : une liste de listes modélisant le plateau
            symboles : dictionnaires définissant les jetons des 2 joueurs
            num_joueur; Numéros du joueur à détecter (1 ou 2)
        OUT: booleen (True si 4 jetons alignés trouvé en diagonale, False sinon)

        Recherche d'une victoire sur les diagonales descendantes vers la droite:
    '''

    jeton = symboles[num_joueur]

    diagonales = [ (2,0,4) , (1,0,5) , (0,0,6) , (0,1,6) , (0,2,5) , (0,3,4)]

    for diagonale  in diagonales :
        ligne,colonne,n = diagonale

        diag = [ grille[ligne+k][colonne+k] for k in range(n) ]
        if jeton * 4 in "".join(diag)  :
            print("VICTOIRE EN DIAGONALE DE " + jeton)
            return True
    
    # Si on arrive ici, aucune diagonale n'a été trouvée, on renvoie False
    return False

def quatre_jetons_diagonal_2(grille,symboles, num_joueur) -> bool:
    '''
        IN: 
            grille : une liste de listes modélisant le plateau
            symboles : dictionnaires définissant les jetons des 2 joueurs
            num_joueur; Numéros du joueur à détecter (1 ou 2)
        OUT: booleen (True si 4 jetons alignés trouvé en diagonale, False sinon)

        Recherche d'une victoire sur les diagonales descendantes vers la gauche:
    '''

    jeton = symboles[num_joueur]

    diagonales = [ (0,3,4) , (0,4,5) , (0,5,6) , (0,6,6) , (1,6,5) , (2,6,4)]

    for diagonale  in diagonales :
        ligne,colonne,n = diagonale
        diag = [ grille[ligne+k][colonne-k] for k in range(n) ]
        if jeton * 4 in "".join(diag)  :
            print("VICTOIRE EN DIAGONALE DE " + jeton)
            return True
    
    # Si on arrive ici, aucune diagonale n'a été trouvée, on renvoie False
    return False

def grille_pleine(grille) -> bool:
    '''
        IN: 
            grille : une liste de listes modélisant le plateau

        OUT: booleen (True si 4 jetons alignés trouvé en diagonale, False sinon)

        Recherche d'une victoire sur les diagonales descendantes vers la gauche:
    '''

    for col in range(7) :
        if colonne_pleine(grille,col) : return True
    
    # Si on arrive ici, aucune diagonale n'a été trouvée, on renvoie False
    return False



def choix_colonne_auto(grille) :
    colonnes = []
    for col in range(7) :
        if not colonne_pleine(grille,col) :
            colonnes.append(col)
            
    print(colonnes)

    return colonnes[ randint(0,len(colonnes)-1 )]


def victoire(grille,symboles,joueur) :
    if quatre_jetons_en_ligne(grille,symboles,joueur) :return True
    if quatre_jetons_en_colonne(grille,symboles,joueur) :return True
    if quatre_jetons_diagonal_1(grille,symboles,joueur) :return True
    if quatre_jetons_diagonal_2(grille,symboles,joueur) :return True

    return False

def jeu(num_ordi) :
    grille = creation_grille_vierge()
    symboles = {1:"x",2:"o"}
    joueur = 1
    cont = True
    
    while cont :
        if joueur != num_ordi :
            n = demander_ou_jouer(grille,joueur)
        else :
            n = choix_colonne_auto(grille)
        if n != -1 :
            # jouer le coup (modifier la grille) :
            grille = joue_jeton(grille,symboles,joueur,n)
            
            if victoire(grille,symboles,joueur) :
                if joueur == num_ordi :
                    print("\nFIN DE PARTIE : Vous avez perdu\n\nPlateau final :")
                else :
                    print("\nFIN DE PARTIE : Vous avez gagné\n\nPlateau final :")

                print(affiche_grille(grille))
                cont = False
            if grille_pleine(grille) :
                print("\nFIN DE PARTIE : partie nulle,\n\nPlateau final :")
                print(affiche_grille(grille))
                cont = False

            # changer de joueur :
            if joueur == 1 :
                joueur = 2
            else :
                joueur = 1
        else :
            # il faut arrêter la boucle infinie :
            cont = False

            
seed()
num_ordi = int( input("qui joue en premier ?\n1: ordinateur\n2: vous"))
jeu(num_ordi)
