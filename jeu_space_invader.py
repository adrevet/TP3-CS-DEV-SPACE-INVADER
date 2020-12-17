""" lien Git: https://github.com/adrevet/TP3-CS-DEV-SPACE-INVADERS.git  """

"""
Date: 17/12/2020

@author: EL IDRISSI Moussa / DREVET Alexandre 3ETI

Statut:
"""

""" on importe les ressources nécéssaires : """
import random, math
from tkinter import Tk, PhotoImage, Canvas, Button, Label, StringVar, Entry, Frame, Menu
from ma_lib import deplacement, clavier
from random import uniform

""" on créé la fenêtre et on paramètre un canvas : """


""" fenetre principale + création canevas : """
fenetre = Tk()
fenetre.title('LE JEU DU SPACE INVADERS')

LARGEUR = 1000
HAUTEUR = 600
canevas=Canvas(fenetre,width=LARGEUR,height=HAUTEUR,bg='black')
boutonQuitter=Button(fenetre,text='Quitter le jeu',fg='red',command=fenetre.destroy)
boutonRejouer=Button(fenetre,text='Rejouer',fg='red',command=fenetre.destroy) #faire une fct rejouer
score=Label(fenetre,text='Score : ')
vies=Label(fenetre,text='Vies : ')


canevas.grid(row=2,column=1,rowspan=4,sticky="nesw")
boutonQuitter.grid(row=3,column=2,padx=50)
boutonRejouer.grid(row=4,column=2)
score.grid(row=1,column=1,sticky="w")
vies.grid(row=1,column=1,sticky="e")


""" menu option avec différentes options : """
menubar = Menu(fenetre)
menuoption = Menu(menubar,tearoff =0)
menuoption.add_command(label="Rejouer", command = fenetre.destroy) #faire une fct rejouer
menuoption.add_command(label="Quitter", command = fenetre.destroy) # boutton pour arreter de jouer 
menubar.add_cascade(label="Option", menu = menuoption)


""" affichage menu : """
fenetre.config(menu = menubar)


""" création alien : """
X = LARGEUR/2 #position intiale de l'alien
Y = HAUTEUR/6 #position intiale de l'alien
r=25

angle= random.uniform(0,2*math.pi) #direction initiale aléatoire
vitesse = uniform(1.8,2)*5
DX=vitesse*math.cos(angle)
alien = canevas.create_rectangle(X-r,Y-r,X+r,Y+r,width=0,fill="red") #on créé l'aliene

deplacement(X,Y,DX,LARGEUR,r,canevas,alien,fenetre) 


""" création vaisseau : """
PosX = 500 #position intiale du vaisseau
PosY = 550 #position intiale du vaisseau
vaisseau = canevas.create_rectangle(PosX-10,PosY-10,PosX+10,PosY+10,width=0,fill="green") #on créé le vaisseau
canevas.focus_set()
canevas.bind('<Key>',lambda event:clavier(event,PosX,canevas,vaisseau,PosY))






fenetre.mainloop()

