"""
Date: 17/12/2020

@author: DREVET Alexandre 3ETI

"""
from tkinter import PhotoImage, messagebox

#Cette fonction permet de créer les différents aliens
""" Création des aliens """
DX_POS = 2
DX_NEG = -2
DX_GLOB = DX_POS
DY_POS = 0.01
DY_NEG = 0
DY_GLOB = DY_POS
list_images_alien = []
def CreationAliens(X,Y,LARGEUR,r,canevas,alien,fenetre):
    global Alien
    Alien = PhotoImage (file = 'alien.gif')
    new_img = Alien.copy()
    list_images_alien.append(new_img)
    alien = canevas.create_image(X-r, Y-r, image = new_img) #on crée l'alien
    deplacement(X,Y,LARGEUR,r,canevas,alien,fenetre) 
#    CreationTirAlien(alien,canevas,TirAlien,X,Y,fenetre)
    return alien

#Cette fonction décrit le déplacement de l'alien que ce soit horizontalement 
#ou verticalement
""" Déplacement de l'alien """
def deplacement(X,Y,LARGEUR,r,canevas,alien,fenetre):
    global DX_GLOB, DX_NEG, DX_POS, DY_POS, DY_NEG, DY_GLOB
    if X+r+DX_GLOB > LARGEUR: #rebond à droite
        X = 2*(LARGEUR-r)-X
        DX_GLOB = DX_NEG
        DY_GLOB = DY_NEG
        
    if X-r+DX_GLOB < 0: #rebond à gauche
        X = 2*r-X
        DX_GLOB = DX_POS
        DY_GLOB = DY_POS
        
    X = X + DX_GLOB
    Y = Y + DY_GLOB
    
    
    canevas.coords(alien, X-r, Y-r)
    fenetre.after(30,lambda:deplacement(X,Y,LARGEUR,r,canevas,alien,fenetre))

#Cette fonction permet de créer les différents îlots
""" Création des ilots """
def CreationIlots (X,Y,Largeur,Hauteur,canevas):
    Ilots = canevas.create_rectangle(X+Largeur, Y+Largeur, X-Largeur, Y-Hauteur,
                                     width = 0, fill = "grey")
    return Ilots

#Cette fonction permet de gérer les différents appuis sur une touche du clavier
""" Gestion de l'évènement Appui sur une touche du clavier """    
def Clavier(event,PosX,canevas,vaisseau,PosY,PosBas,fenetre):
    touche = event.keysym
#    print(touche)
    DX = 0
    (x1, y1, x2, y2) = canevas.bbox(vaisseau)
    if touche == "Right" and x2 == 995:
        DX = 0
    elif touche == "Right": #déplacement à droite
        DX = 10
    
    if touche == "Left" and x1 == 5:
        DX = 0
    elif touche == "Left": #déplacement à gauche
        DX = -10   
    if touche == "space":
        Laser(x1,y1,canevas,PosX,PosBas,fenetre)
    canevas.move(vaisseau, DX, 0)
    
#Cette fonction permet de créer le laser du vaisseau
""" Définition du laser """
def Laser(DX,PosY,canevas,PosX,PosBas,fenetre):
    x = DX
    y = PosY
    Laser = canevas.create_rectangle(x-3, y, x+3, y-5, fill = 'yellow', 
                                     stroke = None)
    Tir(PosX,Laser,PosBas,canevas,fenetre)

#Cette fonction est appelée pour le tir du laser du vaisseau 
""" Définition du tir """
def Tir(PosX,Laser,PosBas,canevas,fenetre):
    canevas.unbind('space')
    if PosBas <= 0:
        canevas.bind('space', Clavier)
        canevas.delete(Laser)
    else:
        PosBas -= 10
        canevas.move(Laser, 0, -10)
#        CoordonneesLaser = canevas.coords(Laser)
#        Impact = canevas.find_overlapping(x1,y1,x2,y2)
#        if Impact == CoordonneesLaser:
#            canevas.delete(Laser)
#            canevas.delete(Ilots)
#            canevas.delete(alien)
        fenetre.after(50,Tir,PosX,Laser,PosBas,canevas,fenetre)
        
""" Définition du tir des aliens """
#def CreationTirAlien(alien,canevas,TirAlien,X,Y,fenetre):
#   TirAlien.append(canevas.create_rectangle(X,Y,X+10,Y+25, fill = 'purple', 
#                                            stroke = None))
#    fenetre.after(1000,CreationTirAlien)
      

        
""" Création de l'ennemi bonus """
#def CreationEnnemiBonus (EnnemiBonus,canevas,fenetre):
#    canevas.move(EnnemiBonus,-10,0)
#    fenetre.after(50,CreationEnnemiBonus)

""" Définition du Jeu """ #La fonction n'est pas terminée
#def Jeu(x,y):
#    Vies = 3
#    y.set("Nombre de vies : "+str(Vies))
#    Score = 0
#    x.set("Score : "+str(Score))

""" Définition de l'a propos """
def Apropos():
    messagebox.showinfo("A propos", "Jeu du Space Invader par Alexandre DREVET."
                        " Ce jeu est sorti en 1978 et consiste à tirer sur des" 
                        " aliens sans se faire toucher par leurs tirs.")


  