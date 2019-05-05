import pygame
pygame.init()

screen = pygame.display.set_mode((600,300), pygame.RESIZABLE) 
background = pygame.image.load(artpath + "200x200.png").convert()

"""

words ="Random Text this is"
print(words[0:10])

"""





#words2 = words.split(" ", 1)






"""
from tkinter import *
Hoch = 75*4   #höhe in cm
Breit = 75*7  #breite in cm

Fenster = Tk() # Fenster erstellen
Fenster.wm_title("GUI") # Fenster Titel
Fenster.config(background = "#000000")
leftFrame = Frame(Fenster, width = Breit, height = Hoch, background = "#FF0000") # Frame initialisieren
leftFrame.grid(row=0, column=0, padx=1, pady=1) # Relative Position und Seitenabstand (padding) angeben
topLabel1 = Label(leftFrame, text=words2[1], bg="#F0F000")
topLabel1.grid(row=0, column=0, padx=3, pady=3)
"""