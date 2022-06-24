from p5 import *

def init_bouses() :
    global case,OK , GAME,nbouse,is_bouse,nbouse
    GAME = 'bouses'
    case = 0
    nbouse = 0
    is_bouse=[True for i in range(15)]+[False]
    OK = True

def init_sisyphe() :
    global step,adroite,OK , GAME,npas,stepmax
    GAME = 'sisyphe'
    step = 0
    adroite=0
    OK = True
    npas = 0
    stepmax = 0

    

def preload():
    global img,robot,pos,code,robot2,eau,img2,GAME,bouse
    if GAME == 'eau' :
        img = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/01-15/13-23-06/rue.jpg")
        img2 = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/01-15/14-08-13/rue2.jpg")
        robot = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/01-15/13-13-34/robot.jpg")
        robot2 = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/01-15/13-42-36/robot2.jpg")
        eau = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/01-15/13-56-11/eau.jpg")
    if GAME == 'bouses' :
        img = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/01-15/15-50-10/bouses.jpg")
        bouse = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/01-15/15-40-24/bouse.jpg")
        robot = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022/01-15/15-48-05/robot_bouses.jpg")

    
def ramasser():
    global EAU,etat,OK,GAME,case,nbouse,is_bouse
    if GAME == 'eau' :
        if not OK : return
        if etat['case'] != 0 :
            print("vous ne pouvez ramasser l'eau ici")
            OK = False
            return
        EAU = True
        etat['eau']=True
    if GAME == "bouses" :
        if not OK : return
        if is_bouse[case-1] :
            is_bouse[case-1] = False
            nbouse+=1
        else :
            if case == 16 :
                print("Il n'y a pas de bouse à ramasser sur cette case !")
            else :
                print("vous avez déjà ramassé cette bouse !")
            OK = False

def deposer() :
    global EAU,etat,OK,GAME,is_bouse,case
    if GAME == 'eau' :
        if not OK : return
        if etat['eau'] is False :
            print("Vous ne pouvez pas déposer l'eau, vous ne l'avez pas ramassée !")
            OK = False
            return
        etat['depot'] = etat['case']
    if GAME == 'bouses' :
        if not OK : return
        if case == 0 :
            print("vous ne pouvez pas déponser sur la case de départ !")
            OK = False
            return
        is_bouse[case-1] = True
    
def setup():
    global img,robot,b,robot2,GAME,bouse
    if GAME == 'eau' :
        createCanvas(800,49)
        # specific to Basthon, useless for standard p5js (see documentation)
        fill(255,255,255)
        background(255,255,255)
    if GAME == 'bouses' :
        createCanvas(759,91)
        # specific to Basthon, useless for standard p5js (see documentation)
        fill(255,255,255)
        background(255,255,255)


def draw():
    global img,robot,case,b,robot2,EAU,etat,eau,img2,GAME,is_bouse
    if GAME == 'eau':
        dx = 11.2
        posx=int(case*dx)
        posx+=posx+37
        posy=5


        if EAU :
            image(img2,0,0)
            if etat['depot'] == False :
                image(robot2,posx,posy)
            else :
                image(robot,posx,posy)
        else :
            image(img,0,0)
            image(robot,posx,posy)


        if etat['depot'] != False :
            posx=int(etat['depot']*dx)
            posx+=posx+37
            x= int(etat['depot']*dx)+37
            image(eau,posx,25)
        if mouseIsPressed :
            case = 2
    if GAME == 'bouses' :
        image(img,0,0)
        dx = int(680/17)
        x = 110-int(dx*1.5)+case*dx
        y=10
        image(robot,x,y)
        for i in range(16):
            if is_bouse[i] :
                x = 110 + i * dx
                y=40
                image(bouse,x,y)

        
def start():

    #preload()
    #run()
    run(preload = preload)
     

def init_porter_eau() :
    global case,OK, EAU , etat,GAME
    GAME = 'eau'
    EAU = False
    case = 2
    OK = True
    etat={'eau':False,'case':2,'depot':False,'mur':False}
    
def droite():
    global case,OK,GAME,step,adroite,npas
    if OK is False : return

    if GAME == 'eau' :
        if not OK : return
        case += 1
        etat['case'] = case
        if  mur() : 
            print("Vous avez percuté le mur")
            OK=False
            
    if GAME == 'bouses' :
        if not OK : return
        case += 1
        
    if GAME == "sisyphe" :
        if OK is False : return
        if adroite == 0 :
            print("Vous percutez le mur")
            OK = False
        adroite = 0
        npas+=1
        
def haut() :
    global adroite,step,OK,npas,stepmax
    if OK is False : return
    if adroite == 1 :
        print("Vous ne pouvez pas monter, vous devez avancer à droite")
        OK = False
    if step == 21 :
        print("vous ne pouvez plus monter, vous êtes au sommet !")
        OK=False
    adroite = 1
    step+=1
    stepmax = max(step,stepmax)
    npas+=1
    
def bas() :
    global adroite,step,OK,npas
    if OK is False : return
    if adroite == 0 :
        print("Vous ne pouvez pas descendre, vous devez avancer à gauche")
        OK = False
    if step == 0 :
        print("vous ne pouvez plus descendre, vous êtes en bas !")
        OK=False
    adroite = 0
    step-=1
    npas+=1
    
def gauche():
    global case,OK,npas,step,adroite
    if not OK : return
    if GAME == "eau" :
        case -= 1
        etat['case'] = case
        if case == 0 : etat[0]=True
        if  mur() : 
            print("Vous avez percuté le mur")
            OK=False
    if GAME == "sisyphe" :
        if OK is False : return
        if adroite == 1 :
            print("Vous tombez dans le vide")
            OK = False
        adroite = 1
        
        npas+=1
    if GAME == 'bouses' :
        if not OK : return
        case -= 1 

    
def mur():
    global etat,OK
    if etat['case'] in [-1,33] : 
        etat['mur']=True
        return True
    return False

def verif() :
    global GAME,etat,is_bouse
    if GAME == 'eau' :
        if etat['mur'] : 
            print("vous avez percuté un mur")
            return
        if 0 in etat.keys() :
            if etat == {'eau': True, 'case': 32, 'depot': 32, 'mur': False,0:True} :
                print('votre code est correct')
            elif etat == {'eau': True, 'case': 32, 'depot': False, 'mur': False,0:True} :
                print("vous avez ramassez l'eau, et l'avez apporté à la maison. Mais vous avez oublié de la déposer !")
            elif etat == {'eau': False, 'case': 32, 'depot': False, 'mur': False, 0: True} :
                print("vous êtes passé au début de la rue, puis vous êtes allé à la maison")
                print("mais vous n'avez pas pensé à ramasser l'eau !")
            else :
                print("votre code n'est pas correct :")
                if etat['eau'] : 
                    print ("vous avez rammassé l'eau")
                else :
                    print("vous n'avez pas ramassé l'eau")
                    return
                if etat['depot'] is not False and etat['depot'] != 32 :
                    print("vous n'avez pas déposé l'eau au bon endroit !")
                    return
        else :
            print("vous devez vous déplacer au début de la rue, pour ramasser l'eau")
    if GAME == 'bouses' :
        if is_bouse == [False for i in range(15)] + [True] and nbouse == 15 :
            print("votre code est correct")
        else :
            print("vous avez ramassé : ",nbouse," bouses")
            if is_bouse[15] :
                print("vous les avez déposée")
            else :
                print("vous n'avez rien déposé dans la boite de la dernière case.")
                
    if GAME == "sisyphe" :
        global npas,stepmax,step
        if npas == 84 and stepmax ==21 and step == 0 : 
            print('votre code est correct')
        else :
            print("votre code n'est pas correct")
