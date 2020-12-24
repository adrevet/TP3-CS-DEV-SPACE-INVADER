""" lien Git: https://github.com/adrevet/TP3-CS-DEV-SPACE-INVADERS.git  """

"""
Date: 17/12/2020

@author: EL IDRISSI Moussa / DREVET Alexandre 3ETI

Statut:
"""

""" Fonction qui décrit le deplacement de l'alien en horizontal : """
def deplacement(X,Y,DX,LARGEUR,r,canevas,alien,fenetre):
    
    if X+r+DX > LARGEUR: #rebond à droite
        X = 2*(LARGEUR-r)-X
        DX = -DX
        
    if X-r+DX < 0: #rebond à gauche
        X=2*r-X
        DX=-DX
        
    X = X+DX
    
    canevas.coords(alien,X-r,Y-r,X+r,Y+r)
    fenetre.after(20,lambda:deplacement(X,Y,DX,LARGEUR,r,canevas,alien,fenetre))

""" Gestion de l'évènement Appui sur une touche du clavier """    
def clavier(event,PosX,canevas,vaisseau,PosY):
    touche = event.keysym
    print(touche)
    DX=0
    (x1,y1,x2,y2)=canevas.bbox(vaisseau)
    if touche == "d" and x2 == 991:
        DX = 0
    elif touche == "d": #déplacement à droite
        DX = 10
    
    if touche == "q" and x1 == 9:
        DX = 0
    elif touche == "q": #déplacement à gauche
        DX = -10   
    if touche == "l":
        Laser()
    canevas.move(vaisseau,DX,0)
    
""" Définition du laser """
#def Laser(PosX,PosY):
#    x = PosX
#    y = PosY
#    Laser = canevas.create_rectangle(x,y,image = Laser)
#    Tir()
  
""" Définition du tir """
#def Tir(PosX,PosY,Laser,touche,Largeur,Long):
#    Long = 15
#    Largeur = 5
#    canevas.unbind('l')
#    x = PosX
#    y = PosY
#    dx = 0
#    dy = -10
#    if y < 0:
#        canevas.bind('l',clavier)
#        canevas.delete(Laser)
#    else:
#        canevas.move(Laser,dx,dy)