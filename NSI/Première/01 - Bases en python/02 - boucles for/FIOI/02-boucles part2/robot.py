from p5 import *

def init_kailash() :
    global case,OK , GAME,dist,checkPoint
    GAME = 'kailash'
    case = [1,14]
    OK = True
    dist = 0
    checkPoint = [0,0,0,0]

    
def init_palais() :
    global case,OK,GAME,visites,chemin
    chemin = [(0,0)]
    GAME = 'palais'
    case = (0,0)
    visites = [ [False for i in range(10)] for j in range(10)]
    OK = True

def init_vendanges() :
    global case,OK , porte,GAME,dist,nb_depots
    GAME = 'vendanges'
    case = 0
    porte = False
    OK = True
    nb_depots = 0

def ramasser() :
    global case,porte,OK
    if OK is False : return

    if case != 0 :
        print("Vous ne pouvez pas ramasser le raisin ici, allez dans la vigne !")
        OK = False
    else :
        porte = True

def deposer() :
    global case,nb_depots,porte,OK
    
    if OK is False : return

    if case != 15:
        print("Vous ne pouvez pas déposer le raisin ici, allez dans la charette !")
        OK = False
    elif porte == False :
        print("vous ne pouvez pas déposer le raisn, il faut d'abord le ramasser !!!")
        OK = False
    else :
        porte = False
        nb_depots+=1
    
    
def preload():
    global img,robot,GAME,robot_raisin,raisin
    if GAME == 'kailash' :
        img = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/01-16/11-33-13/kailash.jpg")
        robot = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/01-16/12-15-22/robot_kailash.png")
    if GAME == 'vendanges' :
        img = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/05-14/16-50-45/vendanges.png")
        robot = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/05-14/17-11-02/robot_vendanges.png")
        robot_raisin = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/05-14/17-20-54/robot_vendanges_raisin.png")
        raisin = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/05-14/16-46-51/raisin.jpg")
    if GAME == 'palais' :
        img = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/05-14/18-21-24/challenge.jpg")
        robot = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/05-14/17-11-02/robot_vendanges.png")

def setup():
    global img,robot,b,robot2,GAME,bouse,robot_raisin
    
    if GAME == 'kailash' :
        createCanvas(322,322)
        fill(255,255,255)
        background(255,255,255)
        
    if GAME == 'vendanges' :
        createCanvas(800,150)
        fill(255,255,255)
        background(255,255,255)
    if GAME == 'palais' :
        createCanvas(250,250)
        fill(255,255,255)
        background(255,255,255)

def draw():
    global img,robot,case,GAME,raisin,robot_raisin,chemin
    if GAME == 'kailash':
        dx = 322/16
        posx=int(case[0]*dx)+ 2
        posy=int(case[1]*dx)- 3
        image(img,0,0)
        image(robot,posx,posy)
        if mouseIsPressed :
            case = [1,14]

    if GAME == 'vendanges' :
        image(img,0,30)
        if nb_depots <20 :
            image(raisin,20,45)
        if porte :
            image(robot_raisin,20+case*725/15,45)
        else :
            image(robot_raisin,20+case*725/15,45)
    if GAME == 'palais' :
        image(img,0,0)
        image(robot,5+case[0]*215/9,5+(9-case[1])*210/9)
        stroke(255)
        for i in range(1,len(chemin)) :
            x1 = 15 + chemin[i-1][0] * 24
            y1 = 235 -chemin[i-1][1] * 24
            x2 = 15+ chemin[i][0] * 24
            y2 = 235 -chemin[i][1] * 24
            line(x1,y1,x2,y2)
        
            
def start():

    #preload()
    #run()
    run(preload = preload)
    verif()
    
def check(case) :
    global checkPoint
    if case == [1,14] : checkPoint[0]+=1
    if case == [1,1] : checkPoint[1]+=1
    if case == [14,1] : checkPoint[2]+=1
    if case == [14,14] : checkPoint[3]+=1
    
def droite():
    global case,OK,GAME,dist,checkPoint,visites
    if OK is False : return

    if GAME == 'vendanges' :
        if case == 15 :
            print("Vous ne pouvez pas aller à droite !")
            OK = False
        else :
            case+=1
        
    if GAME == 'kailash' :
        case[0] += 1
        dist+=1
        check(case)
        if mur() : 
            OK = False
            print("Vous avez quitté le chemin")  
            
    if GAME == 'palais' :
        x = case[0]+1
        y = case[1]
        if case[0]==9 :
            print("Vous ne pouvez pas aller à droite !")
            OK = False
        elif visites[x][y] :
            case = (x,y)
            print("Vous êtes déjà passé par cette pièce")
            OK = False
        else :
            case = (x,y)
            visites[x][y]=True
            chemin.append( case )
            
def gauche():
    global case,OK,GAME,checkPoint,dist,visites
    if OK is False : return

    if GAME == 'vendanges' :
        if case == 0 :
            print("Vous ne pouvez pas aller à gauche !")
            OK = False
        else :
            case-=1
            
    if GAME == 'kailash' :
        case[0] -= 1
        dist+=1
        check(case)
        if mur() : 
            OK = False
            print("Vous avez quitté le chemin")
    if GAME == 'palais' :
        x = case[0]-1
        y = case[1]
        if case[0]==0 :
            print("Vous ne pouvez pas aller à gauche !")
            OK = False
        elif visites[x][y] :
            case = (x,y)
            print("Vous êtes déjà passé par cette pièce")
            OK = False
        else :
            case = (case[0]-1,case[1])
            visites[x][y]=True
            chemin.append( case )

def haut() :
    global case,OK,GAME,dist,checkPoint
    if OK is False : return
    if GAME == 'kailash' :
        case[1] -= 1
        dist+=1
        check(case)
        if mur() : 
            OK = False
            print("Vous avez quitté le chemin")
    if GAME == 'palais' :
        x = case[0]
        y = case[1]+1
        if case[1]==9 :
            print("Vous ne pouvez pas aller en haut !")
            OK = False
        elif visites[x][y] :
            case = (x,y)
            print("Vous êtes déjà passé par cette pièce")
            OK = False
        else :
            case = (x,y)
            visites[x][y]=True
            chemin.append( case )

def bas() :
    global case,OK,GAME,dist,checkPoint
    if OK is False : return
    if GAME == 'kailash' :
        case[1] += 1
        dist+=1
        check(case)
        if mur() : 
            OK = False
            print("Vous avez quitté le chemin")
    if GAME == 'palais' :
        x = case[0]
        y = case[1]-1
        if case[1]==0 :
            print("Vous ne pouvez pas aller en bas !")
            OK = False
        elif visites[x][y] :
            case = (x,y)

            print("Vous êtes déjà passé par cette pièce")
            OK = False
        else :
            case = (x,y)
            visites[x][y]=True
            chemin.append( case )

def mur():
    global OK,case
    if case[0] == 1 and 1<=case[1]<=14: 
        return False
    if case[1] == 1 and 1<=case[0]<=14: 
        return False
    if case[0] == 14 and 1<=case[1]<=14: 
        return False
    if case[1] == 14 and 1<=case[0]<=14: 
        return False
    return True

def verif() :
    global GAME,OK,case,checkPoint,dist,nb_depots,visites
    if GAME == 'kailash' :
        d =  5616 
        if OK is False : 
            print("Revoyez votre code, le robot n'a pas fait les 108 tours...")
            return
        if dist == d :
            print("Vous avez bien parcourru",d,"km.")
            if checkPoint == [108 for _ in range(4)] :
                print("le trajet est correct, Bravo !")
            else:
                print("mais le trajet n'est pas correct...")
            return
        print("Vous avez  parcourru",d,"km, la distance n'est pas correcte, revoyez votre code.")
        
    if GAME == 'vendanges' :
        print("vérification")
        if OK is False : 
            print("Revoyez votre code, vous n'avez pas accompli la tâche.")
            return
        if nb_depots == 20 :
            print("Vous avez bien déposé les 20 brassés de raisin")
        else :
            print("vous avez transporté ",nb_depots,"brassées de raisins, il en fallait 20 !")
            print("revoyer votre code")
            return
        if case != 0 :
            print("vous n'êtes pas retourné dans la champs à la fin..")
            print("revoyer votre code")
            return
        print("votre code est correct")
        
    if GAME == "palais" :
        if OK is False : 
            print("Revoyez votre code, vous n'avez pas accompli la tâche.")
            return
        for ligne in visites :
            if False in ligne :
                print("vous n'avez pas visité toutes les case")
                return
        print("votre code est correct")

            
