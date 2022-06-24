import p5

palette=[
(0,0,0),#noir
(255,0,0),#rouge
(0,255,0),#vert
(0,0,255),#bleu
(255,255,0),#jaune
(255,0,255),#rose
(0,255,255),#cyan
(255,128,128),#rouge pâle
(128,255,128),#vert pâle
(128,128,255),#bleu pâle
(255,255,128),#jaune pâle
(255,128,255),#rose pâle
(128,255,255),#cyan pâle
(128,0,0),#rouge foncé
(0,128,0),#vert foncé
(0,0,128),#bleu foncé
(128,128,0),#ocre
(128,0,128),#violet
(0,128,128),#océan
(200,200,200),#gris clair
(128,128,128),#gris moyen
(80,80,80),#gris foncé
(255,255,255)#blanc
]

matrice=0
tab=0
fic=1
resolution=10

class Bitmap:


    def __init__(self,cat,taille=16,fichier=''):
        self.cat=cat
        if cat==tab:
            self.taille=taille
            if (self.taille & (self.taille-1))!=0:
                raise ValueError('la taille doit être une puissance de 2')
            self.__point__=[[0]*taille for i in range(taille)]
        else:
            if fichier:
                donnees=[]
                with open(fichier,'rb') as f:
                    c=f.read(1)
                    while c!=b'':
                        donnees.append(ord(c))
                        c=f.read(1)
                if not(donnees[0]==66 and donnees[1]==77 and donnees[28]==24):
                    raise IOError('format bitmap 24 bits nécessaire')
                self.taille=donnees[18]+(donnees[19]<<8)+(donnees[20]<<16)+(donnees[21]<<24)
                dim2=donnees[22]+(donnees[23]<<8)+(donnees[24]<<16)+(donnees[25]<<24)
                if self.taille>dim2 or self.taille & (self.taille-1)!=0:
                    raise ValueError('image non carrée ou taille non puissance de 2')
                donnees.reverse()
                self.__point__=[]
                for j in range(self.taille):
                    ligne=[]
                    for i in range(self.taille):
                        decalage=(j*self.taille+i)*3
                        ligne.append((donnees[decalage],donnees[decalage+1],donnees[decalage+2]))
                    ligne.reverse()
                    self.__point__.append(ligne.copy())
            else:
                raise IOError('nom de fichier manquant')

    def charge_pixels(self,valeurs):
        if not (len(valeurs)==self.taille==len(valeurs[0])):
                raise ValueError(f"matrice carrée {self.taille} x {self.taille} attendue")
        if self.cat==tab:
            for rg in valeurs:
                for pt in rg:
                    if pt>len(palette):
                        raise ValueError('valeur de couleur hors limite')
            self.__point__=valeurs
        else:
            for rg in valeurs:
                for pt in rg:
                    if (len(pt)!=3) or (pt[1] not in range(0,256)) or (pt[2] not in range(0,256)) or (pt[2] not in range(0,256)):
                        raise ValueError("donnée incorrecte")
            self.__point__=valeurs

    def lecture_pixels(self):
        return self.__point__

    def lecture_taille(self):
        return self.taille

    def __tracepixel__(self,x0,y0,x,y,couleur):
        if self.cat==tab:
            rvb=palette[couleur]
            p5.stroke(*rvb)
            p5.fill(*rvb)
            p5.rect(x0+resolution*x,y0+y*resolution,resolution,resolution)
        else:
            p5.stroke(*couleur)
            p5.point(x0+x,y0+y)



    def dessine(self,x0,y0):
        for y in range(self.taille):
                for x in range(self.taille):
                    self.__tracepixel__(x0,y0,x,y,self.__point__[y][x])







