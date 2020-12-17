""" lien Git:  """

"""
Date: 17/12/2020

@author: EL IDRISSI Moussa 3ETI

Statut:
"""

""" on importe les ressources nécéssaires : """
import random, math
from tkinter import Tk, PhotoImage, Canvas, Button, Label, StringVar, Entry

""" on créé la fenêtre et on paramètre un canvas : """
fenetre=Tk()
fenetre.title("Jeu Space Invader")

canvas=Canvas(fenetre,width=1280,height=720,bg='black')
