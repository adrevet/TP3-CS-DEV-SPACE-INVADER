""" lien Git: https://github.com/adrevet/TP3-CS-DEV-SPACE-INVADERS.git  """

"""
Date: 17/12/2020

@author: EL IDRISSI Moussa / DREVET Alexandre 3ETI

Statut:
"""


""" Création des aliens """
def CreationAliens(X,Y,DX,DY,LARGEUR,HAUTEUR,r,canevas,alien,fenetre):
    alien = canevas.create_rectangle(X-r,Y-r,X+r,Y+r,width = 0,fill = "red") #on crée l'alien
    deplacement(X,Y,DX,DY,LARGEUR,HAUTEUR,r,canevas,alien,fenetre) 
    return alien


""" Fonction qui décrit le deplacement de l'alien en horizontal : """
def deplacement(X,Y,DX,DY,LARGEUR,HAUTEUR,r,canevas,alien,fenetre):
#    TailleAlien = 40
#    DY = 5
#    XP = canevas.coords(alien[0][0])[0]
#    XD = canevas.coords(alien[0][-1])[0]
#    if XP+DX < 0: #rebond à gauche
#        X = 0
#        DX = -DX
#        Y += TailleAlien
#    if XD + TailleAlien + DX > LARGEUR: #rebond à droite
#        X = LARGEUR -TailleAlien -500
#        DX =-DX
#        Y += TailleAlien
#    X = X+DX
#    Y = Y+DY
#    for i in range (len(alien)):
#        for j in range (len(alien[i])):
#            canevas.coords(alien[i][j],X+j*100,Y+i*100)
#    if Y >= 700:
#        canevas.unbind('space')
#        canevas.create_image(0,0, anchor = NW, image = Défaite)
#    fenetre.after(40, lambda:deplacement(X,Y,DX,DY,LARGEUR,HAUTEUR,r,canevas,alien,fenetre))
    
    
    if X+r+DX > LARGEUR: #rebond à droite
        X = 2*(LARGEUR-r)-X
        DX = -DX
        
    if X-r+DX < 0: #rebond à gauche
        X = 2*r-X
        DX=-DX
        
    X = X+DX
    
    canevas.coords(alien,X-r,Y-r,X+r,Y+r)
    fenetre.after(20,lambda:deplacement(X,Y,DX,LARGEUR,r,canevas,alien,fenetre))

""" Création des ilots """
def CreationIlots (X,Y,Largeur,Hauteur,canevas):
    Ilots = canevas.create_rectangle(X+Largeur,Y+Largeur,X-Largeur,Y-Hauteur, width = 0, fill = "grey")
    return Ilots

""" Gestion de l'évènement Appui sur une touche du clavier """    
def clavier(event,PosX,canevas,vaisseau,PosY):
    touche = event.keysym
    print(touche)
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
#    if touche == "space":
#        Laser()
    canevas.move(vaisseau,DX,0)
    

""" Définition du laser """
#def Laser(DX,PosY,canevas,Laser):
#    x = DX
#    y = PosY
#    Laser = canevas.create_rectangle(x,y,image = Laser)
#    Tir()
#  
""" Définition du tir """
#def Tir(PosX,Laser,touche,PosBas,canevas,fenetre):
#    canevas.unbind('l')
#    if PosBas <= 0:
#        canevas.bind('l',clavier)
#        canevas.delete(Laser)
#    else:
#        PosBas -= 10
#        canevas.coords(Laser,PosX,PosBas)
#        fenetre.after(50,Tir)