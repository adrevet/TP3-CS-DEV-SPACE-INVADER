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
fenetre.geometry('1400x720')



canevas=Canvas(fenetre,width=1000,height=600,bg='black')
boutonQuitter=Button(fenetre,text='Quitter le jeu',fg='red',command=fenetre.destroy)
boutonRejouer=Button(fenetre,text='Rejouer',fg='red',command=fenetre.destroy) #faire une fct rejouer
score=Label(fenetre,text='Score : ')
vies=Label(fenetre,text='Vies : ')

canevas.grid(row=2,column=1,sticky="nesw")
boutonQuitter.grid(row=2,column=2)
boutonRejouer.grid(row=2,column=3)
score.grid(row=1,column=1,sticky="w")
vies.grid(row=1,column=1,sticky="e")



fenetre.mainloop()

