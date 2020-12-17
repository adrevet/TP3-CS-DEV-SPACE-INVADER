""" lien Git: https://github.com/adrevet/TP3-CS-DEV-SPACE-INVADERS.git  """

"""
Date: 17/12/2020

@author: EL IDRISSI Moussa 3ETI

Statut:
"""

""" on importe les ressources nécéssaires : """
import random, math
from tkinter import Tk, PhotoImage, Canvas, Button, Label, StringVar, Entry, Frame

""" on créé la fenêtre et on paramètre un canvas : """


""" fenetre principale + création canevas : """
fenetre = Tk()
fenetre.title('LE JEU DU SPACE INVADERS')
fenetre.geometry('1280x720')

canevas=Canvas(fenetre,width=1000,height=600,bg='black')
canevas.pack(side="left",padx=10,pady=10)


boutonQuitter=Button(fenetre,text='Quitter le jeu',fg='red',command=fenetre.destroy)
boutonQuitter.pack(side='right',padx=90)
boutonRejouer=Button(fenetre,text='Rejouer',fg='red',command=fenetre.destroy) #faire une fct rejouer
boutonRejouer.pack(side='right')


fenetre.mainloop()

