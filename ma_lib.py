"""
Date: 17/12/2020

@author: DREVET Alexandre 3ETI

Statut:
"""


""" Création des aliens """
DX_POS = 5
DX_NEG = -5
DX_GLOB = DX_POS
def CreationAliens(X,Y,DX,LARGEUR,r,canevas,alien,fenetre):
    alien = canevas.create_rectangle(X-r,Y-r,X+r,Y+r,width = 0,fill = "red") #on crée l'alien
    deplacement(X,Y,DX,LARGEUR,r,canevas,alien,fenetre) 
    return alien


""" Fonction qui décrit le deplacement de l'alien en horizontal : """
def deplacement(X,Y,DX,LARGEUR,r,canevas,alien,fenetre):
    global DX_GLOB, DX_NEG, DX_POS
    if X+r+DX_GLOB > LARGEUR: #rebond à droite
        X = 2*(LARGEUR-r)-X
        DX_GLOB = DX_NEG
        
    if X-r+DX_GLOB < 0: #rebond à gauche
        X = 2*r-X
        DX_GLOB = DX_POS
        
    X = X+DX_GLOB
    
    canevas.coords(alien,X-r,Y-r,X+r,Y+r)
    fenetre.after(20,lambda:deplacement(X,Y,DX,LARGEUR,r,canevas,alien,fenetre))

""" Création des ilots """
def CreationIlots (X,Y,Largeur,Hauteur,canevas):
    Ilots = canevas.create_rectangle(X+Largeur,Y+Largeur,X-Largeur,Y-Hauteur, width = 0, fill = "grey")
    return Ilots

""" Gestion de l'évènement Appui sur une touche du clavier """    
def clavier(event,PosX,canevas,vaisseau,PosY,PosBas,fenetre):
    touche = event.keysym
#    print(touche)
    DX=0
    (x1,y1,x2,y2)=canevas.bbox(vaisseau)
    if touche == "Right" and x2 == 991:
        DX = 0
    elif touche == "Right": #déplacement à droite
        DX = 10
    
    if touche == "Left" and x1 == 9:
        DX = 0
    elif touche == "Left": #déplacement à gauche
        DX = -10   
    if touche == "space":
        Laser(x1,y1,canevas,PosX,PosBas,fenetre)
    canevas.move(vaisseau,DX,0)
    

""" Définition du laser """
def Laser(DX,PosY,canevas,PosX,PosBas,fenetre):
    x = DX
    y = PosY
    Laser = canevas.create_rectangle(x-3,y,x+3,y-5, fill = 'yellow', stroke = None)
    Tir(PosX,Laser,PosBas,canevas,fenetre)
  
""" Définition du tir """
def Tir(PosX,Laser,PosBas,canevas,fenetre):
    canevas.unbind('space')
    if PosBas <= 0:
        canevas.bind('space',clavier)
        canevas.delete(Laser)
    else:
        PosBas -= 10
        canevas.move(Laser,0,-10)
        fenetre.after(50,Tir,PosX,Laser,PosBas,canevas,fenetre)