def check_grille_vierge(f) :
    g = f()
    ans = [[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."],[".",".",".",".",".",".","."]] 
    if g == ans :
            print("Vode code est correct")
            return

    if len(g) == 6 : 
        print("votre grille à bien 6 lignes")
    else :
        print("La grille devrait avoir 6 lignes. Nombre de lignes de votre grille : ",len(g))
          
    if [len(g[i]) for i in range(len(g))] == [len(g[0]) for i in range(len(g))] :
        if len(g[0])==7 :
            print("votre grille à bien 7 colonnes")
        else :
            print("Toutes les colonnes de votre grille ont ",len(g[0]),"éléments, elles devraient en avoir 7")
        
        if len(g) == 6 and len(g[0])==7 :
            print("La grille est bien une liste contenant 6 listes de longueur 7, \nmais il y a une erreur dans les éléments des sous listes, qui doivent être des chaines de caractères \".\"")
            
    else :
            print("La grille est bien une liste contenant 6 listes,\nmais les sous listes n'ont pas toutes la même longueur.")


def affiche(grille) -> None :
    ''' Cette fonction affiche la grille de jeu telle que ci-dessous
    IN: Rien
    OUT: Rien
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
    
    # Affichage des indices du haut de la grille (0 à 6)
    print("   ", end="")
    for i in range(7):
        print(str(i)+" ",end="")
    print("\n  ") # '\n' est un saut de ligne  (passage à une nouvelle ligne) suivi de deux espaces
    
    # Affichage des lignes
    for i in range(6): # Pour chaque ligne i
        print(str(i)+" ",end="")
        for j in range(7): # Pour chaque colonne j
            print("|"+ grille[i][j],end ="")
        print("|")
        
    # Affichage du trait en bas de la grille
    print(" ","-"*15)
    
def check_colonne_pleine(f) :
    
    g = [['.', 'X', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.'], ['.', 'X', '.', 'O', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.'], ['X', 'X', '.', '.', '.', '.', '.']]
    if f(g,1) == True and f(g,0) == False :
        print("votre code semble correct")
    else :
        print("Votre code comporte une erreur. Nous avons testé avec cette grille :\n")
        affiche(g)

        
        if f(g,1) != True : print("colonne_pleine(grille,1) devrait renvoyer True, et renvoie False")
        for i in [0,2,3,4,5,6] :
            if f(g,i) != False : print("colonne_pleine(grille,",i,") devrait renvoyer False, et renvoie True")
 
def check_joue_jeton(f):
    grille = [["-" for j in range(7)] for i in range(6)]
    symboles = {1:"X", 2:"O"} 

    grille = f(grille, symboles, 1, 3)  # Joueur 1 joue dans colonne 3
    assert(grille == [['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', 'X', '-', '-', '-']])

    grille = f(grille, symboles, 2, 0)  # Joueur 2 joue dans colonne 0
    assert grille == [['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['O', '-', '-', 'X', '-', '-', '-']]

    grille = f(grille, symboles, 1, 3)  # Joueur 1 joue dans colonne 3
    assert [['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', 'X', '-', '-', '-'], ['O', '-', '-', 'X', '-', '-', '-']]
    
    print("votre code semble correct")