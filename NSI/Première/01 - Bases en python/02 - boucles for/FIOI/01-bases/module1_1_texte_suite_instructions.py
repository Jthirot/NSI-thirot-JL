from p5 import *

def init_exercice() :
    global pos
    pos = [1,4]
    
def haut() :
    global pos
    if "pos" not in globals() : pos = [1,4]

    if buisson() or piege()or cle():return
    pos[1] -= 1
    draw()
    if buisson() : print("Vous avez poussé le robot dans un buisson")  
    if piege() : print("Vous avez poussé le robot dans un piege")  
    if cle() : print("Bravo !")
    
def bas() :
    global pos
    if "pos" not in globals() : pos = [1,4]

    if buisson() or piege()or cle():return
    pos[1] += 1
    if buisson() : print("Vous avez poussé le robot dans un buisson")  
    if piege() : print("Vous avez poussé le robot dans un piege")  
    if cle() : print("Bravo !")
    
def droite() :
    global pos
    if buisson() or piege()or cle():return
    pos[0] += 1
    if buisson() : print("Vous avez poussé le robot dans un buisson")  
    if piege() : print("Vous avez poussé le robot dans un piege")  
    if cle() : print("Bravo !")

def gauche() :
    global pos
    if buisson() or piege()or cle():return
    pos[0] -= 1
    draw()
    if buisson() : print("Vous avez poussé le robot dans un buisson")  
    if piege() : print("Vous avez poussé le robot dans un piege")  
    if cle() : print("Bravo !")
    
def buisson():
    global pos
    if pos[0] in [0,6] : return True
    if pos[1] == 0 : return True
    if pos[1] == 4 and pos[0] != 1 : return True
    if pos[0] == 2 and pos[1]==2 : return True
    if pos[0] == 4 and pos[1]==2 : return True
    return False

def piege():
    global pos
    if pos[0] == 2 and pos[1]==3 : return True
    if pos[0] == 4 and pos[1]==1 : return True
    if pos[0] == 5 and pos[1]==2 : return True
    return False

def cle() :
    global pos
    if pos == [4,3] : return True
    return False

def preload():
    global img,robot,pos,code
    #if "pos" not in globals(): pos=[1,4]
    img = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022-01-08-13-35-33/fond-robot.jpg")
    robot = loadImage("https://capytale2.ac-paris.fr/web/sites/default/files/2022-01-08-13-35-33/robot.png")

def setup():
    global img,robot,b
    #imageMode(CENTER)
    #img.resize(50,50)
    createCanvas(280,198)

    # specific to Basthon, useless for standard p5js (see documentation)
    fill(255,255,255)
    background(255,255,255)


def draw():
    global img,robot,pos,b
    background(255, 255, 255)

    # Code à compléter
    image(img,0,0)
    dx = 280/7
    dy=198/5
    posx=pos[0]*dx
    posy=pos[1]*dy+5
    image(robot,posx,posy)
    if mouseIsPressed :
        pos=[1,4]
        
def start():
    preload()
    #run()
    run(preload = preload)
    
    
#### challenge hanoi

def deplacer(a,b) :
    global OK
    if not OK: return
    hanoi[b-1].append(hanoi[a-1].pop())
    if not check(b-1): 
        print('vous avez créé un empilement instable sur la pile ',b)
        OK = False

def check(pile):
    if hanoi[pile] == sorted(hanoi[pile],reverse = True) : return True
    return False
def init_challenge1() :
    global hanoi,OK
    OK = True
    hanoi = [ [4,3,2,1] , [] , []]

def verif_challenge1(hanoi) :
    
    if hanoi == [ [] , [] , [4,3,2,1]] : print('le code est correct')
    else : print("le code n'est pas correct")
    
def remplir(n) :
    global OK
    if not OK : return
    if n not in [5,3] :
        print("il n'y a pas de saut de "+str(n)+"L")
        OK = False
    etat[n] = n

def transferer(n,m) :
    global OK,etat
    if n not in [5,3] :
        print("il n'y a pas de saut de "+str(n)+"L")
        OK = False
    if m not in [5,3] :
        print("il n'y a pas de saut de "+str(m)+"L")
        OK = False
    etat[m]+= etat[n]
    etat[n]=0
    if etat[m]> m :
        reste = etat[m]-m
        etat[n] = reste
        etat[m]=m
    
def vider(n):
    global OK
    if not OK : return
    if n not in [5,3] :
        print("il n'y a pas de saut de "+str(n)+"L")
        OK = False
    etat[n] = 0
    
def init_challenge2():
    global etat,OK
    etat = {5:0,3:0}
    OK = True
    
def verif_challenge2(etat) :
      
    if 4 in etat.values() : print('le code est correct')
    else : print("le code n'est pas correct")