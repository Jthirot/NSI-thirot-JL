def creation_grille_vierge():
    '''  Cette fonction va créer un plateau de jeu vide. 
    Les case vides sont représentées par la valeur 0.

    IN: Rien

    OUT:la fonction renvoie une liste de liste représentant la grille vierge. **e**

    C'est une liste de listes :

    6 lignes contenant chacun 7 valeurs. Initialement toutes les valeurs sont nulles, losqu'un joueur joue, la valeur d'un élément sera mise égale à 1 ou 2.

    Voila la grille vierge que renvoie la fonction :
        [ [0,0,0,0,0,0,0] , 
          [0,0,0,0,0,0,0] ,
          [0,0,0,0,0,0,0] ,
          [0,0,0,0,0,0,0] ,
          [0,0,0,0,0,0,0] ,
          [0,0,0,0,0,0,0]]   
    '''

    grille_vierge = []
    # Pour chaque ligne
    for num_ligne in range(6):
        nouvelle_ligne = [] # on crée un nouveau tableau vide en mémoire
        for j in range(7): # On ajoute les sept éléments ".", séparémment.
            nouvelle_ligne.append(0)
            
        # On ajoute la nouvelle ligne à la grille
        grille_vierge.append(nouvelle_ligne)
    
    # Le travail est terminé, la variable globale grille est remplie, on quitte la procédure
    return grille_vierge

def joue_jeton(grille, num_joueur, indice_colonne) -> None:
    ''' Place un jeton du joueur numéros num_joueur, dans la colonne indice_colonne.
    
        IN: num_joueur (int qui vaut 1 ou 2)
        OUT: la fonction renvoie la grille modifiée
    '''

    # Dans la colonne indice_colonne, en partant, du bas, on cherche la première case vide.
    # on suppose que la colonne n'est pas pleine, ce problème sera traité ailleur.
    
    for ligne in range(5,-1,-1) :
        if grille[ligne][indice_colonne] == 0 :
            grille[ligne][indice_colonne] = num_joueur
            return grille
        
                    
def colonne_pleine(grille,indice_colonne) -> bool:
    '''
        IN: indice de la colonne à analyser (0 à 6)
        OUT: un booleen (True si la colonne est déjà pleine, False sinon)
    '''
    
    # il suffit de tester si l'élément à la ligne 0 de cette colonne est égal à '.'
    if grille[0][indice_colonne] != 0: return True
    return False

def grille_pleine(grille) -> bool:
    '''
        IN: la grille
        OUT: un booleen (True si la grille est pleine, False sinon)
    '''
    return [colonne_pleine(grille,i) for i in range(7) ] == [True for i in range(7)] 


def quatre_jetons_en_ligne(grille, num_joueur) -> bool:
    '''
        IN: 
            grille : une liste de listes modélisant le plateau
            symboles : dictionnaires définissant les jetons des 2 joueurs
            num_joueur; Numéros du joueur à détecter (1 ou 2)
        OUT: booleen (True si 4 jetons alignés trouvés en ligne, False sinon)
    '''
    
    # définition du jeton à trouver
    jeton = str(num_joueur)
    chaine_a_trouver = jeton * 4
    for ligne in grille :
        ligne_txt = [str(ligne[i]) for i in range(7)]
        ligne_txt = "".join(ligne_txt)
        if chaine_a_trouver in ligne_txt :
            return True

    # Si on arrive ici, c'est qu'aucun alignement de 4 jetons n'a été trouvé en ligne
    return False

def quatre_jetons_en_colonne(grille,num_joueur):
    '''
        IN: 
            grille : une liste de listes modélisant le plateau
            symboles : dictionnaires définissant les jetons des 2 joueurs
            num_joueur; Numéros du joueur à détecter (1 ou 2)
        OUT: booleen (True si 4 jetons alignés trouvés en colonne, False sinon)
    '''
    
    # définition du jeton à trouver
    jeton = str(num_joueur)
    chaine_a_trouver = jeton * 4
    for colonne in range(7):
        colonne = [str(grille[i][colonne]) for i in range(6)]
        colonne_txt = "".join(colonne)
        if chaine_a_trouver in colonne_txt :
            return True

    # Si on arrive ici, c'est qu'aucun alignement de 4 jetons n'a été trouvé en ligne
    return False

def quatre_jetons_diagonal_1(grille, num_joueur) -> bool:
    '''
        IN: 
            grille : une liste de listes modélisant le plateau
            symboles : dictionnaires définissant les jetons des 2 joueurs
            num_joueur; Numéros du joueur à détecter (1 ou 2)
        OUT: booleen (True si 4 jetons alignés trouvé en diagonale, False sinon)

        Recherche d'une victoire sur les diagonales descendantes vers la droite:
    '''

    jeton = str(num_joueur)

    diagonales = [ (2,0,4) , (1,0,5) , (0,0,6) , (0,1,6) , (0,2,5) , (0,3,4)]

    for diagonale  in diagonales :
        ligne,colonne,n = diagonale

        diag = [ str(grille[ligne+k][colonne+k]) for k in range(n) ]
        if jeton * 4 in "".join(diag)  :
            return True
    
    # Si on arrive ici, aucune diagonale n'a été trouvée, on renvoie False
    return False

def quatre_jetons_diagonal_2(grille, num_joueur) -> bool:
    '''
        IN: 
            grille : une liste de listes modélisant le plateau
            symboles : dictionnaires définissant les jetons des 2 joueurs
            num_joueur; Numéros du joueur à détecter (1 ou 2)
        OUT: booleen (True si 4 jetons alignés trouvé en diagonale, False sinon)

        Recherche d'une victoire sur les diagonales descendantes vers la gauche:
    '''

    jeton = str(num_joueur)

    diagonales = [ (0,3,4) , (0,4,5) , (0,5,6) , (0,6,6) , (1,6,5) , (2,6,4)]

    for diagonale  in diagonales :
        ligne,colonne,n = diagonale
        diag = [ str(grille[ligne+k][colonne-k]) for k in range(n) ]
        if jeton * 4 in "".join(diag)  :
            return True
    
    # Si on arrive ici, aucune diagonale n'a été trouvée, on renvoie False
    return False

def check_victoire(grille,joueur) :
    if quatre_jetons_en_ligne(grille,joueur) :return True
    if quatre_jetons_en_colonne(grille,joueur) :return True
    if quatre_jetons_diagonal_1(grille,joueur) :return True
    if quatre_jetons_diagonal_2(grille,joueur) :return True

    return False
