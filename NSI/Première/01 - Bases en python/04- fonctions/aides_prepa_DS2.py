def aide1_1() :

    rep = input("ANALYSE DU PROBLEME (1):\nce code utilise-t-il une boucle ? (o/n) : ")
    if rep == "o" :
        rep = input('boucle for ou boucle while ? (f/w) : ')
        while rep != "f" and rep != "w" :
            print('vous devez répondre f ou w')
            rep = input('for/while (f/w) : ')
        if rep == "w" :
            print("très bien, on va en effet lancer TANT QUE on a pas atteint le total demandÃ©")
        else :
            print()
            print("ERREUR ! tu ne sais pas combien de lancers il faut faire, donc la boucle for ne sera pas possible")
            print("On doit lancer le dé TANT QUE on a pas atteint n")
    else :
        print('Comment va tu simuler les lancés successif si tu ne fait pas une boucle ?')
        
def aide1_2() : 

    rep = input("ANALYSE DU PROBLEME (2):\nce code utilise-t-il un compteur ? (o/n) : ")
    while rep != "o" and rep != "n":
        rep = input("il faut répondre o ou n ? Ce code utilise-t-il un compteur : ")

    if rep == "o" :
        print('très bien, en effet on dois compter le nombre de lancer du dé')
    else :
        print('ERREUR : Sans compteur, comment va tu COMPTER le nombre de lancer du dé ?')

def aide1_3() :            

    
    rep = input('ANALYSE DU PROBLEME (3):\nce code utilise-t-il un accumulateur ? (o/n) : ')
    while rep != "o" and rep != "n":
        rep = input("il faut répondre o ou n ? Ce code utilise-t-il un accumulateur(s) : ")
    if rep ==  "o":
        print('très bien, en effet on dois additionner (accumuler) les résultats obtenus')
    else :
        print('ERREUR : Sans accumulateur, comment va tu FAIRE LA SOMME des résultats du dé ?')

def aide1_4() :            

    
    rep = input('ANALYSE DU PROBLEME (4):\nIntialisation du compteur :\nn_jet = ?\nEntre la valeur initiale du compteur : ')
    while rep != "0" :
        rep = input("réfléchit bien, au début on a fait combien de jets ? ")
    print("oui, au départ on a lancé 0 fois le dÃ© !")

def aide1_5() :            

    
    rep = input("ANALYSE DU PROBLEME (5):\nAccumulateur :\nEntre la valeur initiale de l\'accumulateur : \ntotal = ?")
    while rep != "0" :
        rep = input("réfléchit bien, au début on a un total de combien ? ")
    print("oui, au départ on a lancé 0 fois le dé pour un score total égal à  0 !")
  
   
        
def aide1_6() :            

    rep = input('Syntaxe : lancer le dé:\nComment \'lancer un dé \n\n(tapez simplement entrée pour voir)')

    print('de = randint(1,6)')


def aide2_1() :

    print("")

    rep = input("ANALYSE DU PROBLEME (1):ce code utilise-t-il une boucle ? (o/n) : ")
    if rep == "o" :

        rep = input("Ce n'est pas obligé car il y a deux façon d'envisager le problème!\n\
Mais si vous décidez de faire une boucle ce sera for ou while ? (f/w) ")
        while rep != "f" and rep != "w" :
            print('vous devez répondre f ou w')
            rep = input('for/while (f/w) : ')
        if rep == "w" :
            rep = input("ok, vous allez ajouter un point devant le mot.\nVous continuerez TANT QUE ... ?")
            nrep=0
            while rep.replace(" ","") != 'len(mot)<10' and nrep < 3:
                nrep+=1
                rep = input("Je n'ai pas compris la réponse...\nEssaye de nouveau, on demande ce qu'on doit écrire après le while .... : que devrez vous mettre comme condition ?")
            if rep.replace(" ","")!='len(mot)<10 ' :
                    print('très bien, a toi de jouer...')
                else :
                    print("while len(mot) < 10 :")            return
        else :
            print("non, aucune boucle for n'est envisageable....")
    else :
        rep = input("En effet on peut s'en passer ici\nle mot à  renvoyer sera \'.\'*...+mot, que vaut ... ?")
        while rep.replace(" ","")!='10-len(mot)' :
            rep = input("combien veux tu ajouter de . devant le mot ?")
            
        if rep.replace(" ","")!='10-len(mot)' :
            print('très bien, a toi de jouer...')
        else :
            print("iL FAUT AJOUTER 10-len(mot) POINTS")
            
def aide3_1() :

    print("\nRappellez vous de ce code :\ndef nombre_de_fois(lettre,texte) -> int:\n    count = 0\n    for charactere in texte :\n        if lettre == charactere :\n        count += 1\n    return count")
    print()
    print("mais ici la condition est différente...")
    
def aide3_2() :

    print("la condition est :")
    print("is_upper(txt[i]) == True")
    print("qui peut s\'écrire simplement is_upper(txt[i])")

            
def aide4_1() :

    print("\nRappellez vous de ce code :\ndef nombre_de_fois(lettre,texte) -> int:\n    count = 0\n    for charactere in texte :\n        if lettre == charactere :\n            count += 1\n    return count")
    print()
    print("ici aussi vous allez parcourir la chaine, mais quand la condition sera vérifiée, au lieux d'incrémenter un compteur...")
    print("que voullez vous faire ?")
    
def aide4_2() :

    print("Vous voulez mémoriser la position (indice) de la dernière fois ou la condition est vraie")
    print()
    print("ferez vous un parcours sur les indices ou sur les lettres ?")
    
def aide4_3() :


    print(" Vous avez besoin de l'indice => un parcours sur les indices ?")  
    
def aide4_4() :


    rep = input("Doit-on place un return dans la boucle ? (o/n)")    
    if rep == "o" :
        print ("surtout pas, vous voulez parcourir TOUTE la chaine !")
    else :
        print ("en effet, car vous voulez parcourir TOUTE la chaine !")

def aide4_5() :


    rep = input("faut il un compteur")    
    if rep == "o" :
        print ("non, on ne compte rien ici, on garde seulement en mémoire l'indice de la dernière fois que l'égalité est vraie")
    else :
        print ("en effet, on va juste garder en mémoire l'indice, on ne compte rien.")
        
def aide4_6() :


    print("initialisez un repère : index = -1")
    print("parcourez la chaine et si vous rencontrez la lettre cherchÃ©e, mettez à jour index")
    print("quand le parcours est terminé renvoyez index")

