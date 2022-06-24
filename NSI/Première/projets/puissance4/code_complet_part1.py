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
            
def jeu() :
    grille = creation_grille_vierge()
    symboles = {1:"x",2:"o"}
    joueur = 1
    cont = True
    
    while cont :
        n = demander_ou_jouer(grille,joueur)
        if n != -1 :
            # jouer le coup (modifier la grille) :
            grille = joue_jeton(grille,symboles,joueur,n)
            # changer de joueur :
            if joueur == 1 :
                joueur = 2
            else :
                joueur = 1
        else :
            # il faut arrêter la boucle infinie :
            cont = False
    
jeu()