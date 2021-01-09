"""
Date: 17/12/2020

@author: DREVET Alexandre 3ETI

"""

# Header
"""
Que fait ce programme : Jeu Space Invaders
Qui l'a fait : Alexandre Drevet
Quand a-t-il été réalisé : //2021
Que reste-t-il à faire : Faire une fonction rejouer, faire en sorte que 
lorsqu'un alien touche un bord ils reviennent tous, regarder les fonctions laser
et tir pour les faire marcher
Lien github : 
"""

#Importation des bibliothèques nécessaires
import random, math
from tkinter import Tk, PhotoImage, Canvas, Button, Label, StringVar, Entry, Frame, Menu, NW
from ma_lib import clavier, CreationAliens, CreationIlots, Laser
from random import uniform


""" Fenêtre principale + création canevas : """
fenetre = Tk()
fenetre.title('LE JEU DU SPACE INVADERS')

LARGEUR = 1000
HAUTEUR = 666
canevas = Canvas(fenetre, width = LARGEUR, height = HAUTEUR, bg = 'white')
Fond = PhotoImage (file = 'terre.gif')
canevas.create_image(0, 0, anchor = NW, image = Fond)

boutonQuitter = Button(fenetre, text = 'Quitter le jeu', fg ='red',
                       command = fenetre.destroy)
boutonRejouer = Button(fenetre, text = 'Rejouer', fg = 'red',
                       command = fenetre.destroy) #faire une fct rejouer

PosBas = 600

""" Affichage du score """
x = StringVar
##x.set("Score : "+str(score)) #Créer une fonction qui calcule le score
score = Label(fenetre,textvariable = x,fg = 'black',bg = 'white')

""" Affichage du nombre de vies """
y = StringVar
##y.set("Nombre de vies : "+str(vies)) #Créer une fonction qui calcule le nombre de vie
vies = Label(fenetre,textvariable = y, fg = 'black', bg = 'white')


canevas.grid(row = 2, column = 1, rowspan = 4, sticky = "nesw")
boutonQuitter.grid(row = 3, column = 2, padx = 50)
boutonRejouer.grid(row = 4, column = 2)
score.grid(row = 1, column = 1, sticky = "w")
vies.grid(row = 1, column = 1, sticky = "e")


""" Menu option avec différentes options : """
menubar = Menu(fenetre)
menuoption = Menu(menubar, tearoff = 0)
menuoption.add_command(label = "Rejouer", command = fenetre.destroy) #faire une fct rejouer
menuoption.add_command(label = "Quitter", command = fenetre.destroy) # boutton pour arreter de jouer 
menubar.add_cascade(label = "Option", menu = menuoption)
menubar.add_cascade(label = "A propos")


""" Affichage menu : """
fenetre.config(menu = menubar)


""" Création alien : """
alien = []
X = LARGEUR/2 #position intiale de l'alien
Y = HAUTEUR/6 #position intiale de l'alien
r = 25
angle= random.uniform(0,2*math.pi) #direction initiale aléatoire
vitesse = uniform(1.8,2)*5
DX = vitesse*math.cos(angle)
DY = 5
for i in range (0,10):
    alien.append(CreationAliens(X,Y,DX,LARGEUR,r,canevas,alien,fenetre))
    if X == 900:
        X = 400
        Y += 100
    else:
        X += 200

""" Création vaisseau : """
PosX = 500 #position intiale du vaisseau
PosY = 550 #position intiale du vaisseau
vaisseau = canevas.create_rectangle(PosX-10,PosY-10,PosX+10,PosY+10,width = 0,
                                    fill = "green") #on créé le vaisseau
canevas.focus_set()
canevas.bind('<Key>',lambda event:clavier(event,PosX,canevas,vaisseau,PosY,PosBas,fenetre))

""" Création Ilots """
Ilots = []
X = LARGEUR/6
Y = HAUTEUR/1.5
Largeur = 60
Hauteur = 30
for i in range (0,3):
    Ilots.append(CreationIlots(X,Y,Largeur,Hauteur,canevas))
    if X == 1000:
        X = 100
        Y += 300
    else:
        X += 300

""" Image du laser """
lambda:Laser(DX,PosY,canevas,Laser,PosX,PosBas,fenetre)






fenetre.mainloop()

