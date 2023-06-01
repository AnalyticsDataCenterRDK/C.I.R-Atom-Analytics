from tkinter import ttk
from tkinter import *


def setting():
    root = Tk()

    root.geometry("1000x500")
    root.title("C.I.R Atom Analytics Settings")

    mainmenu = Menu(root)
    root.config(menu=mainmenu)

    settings = Menu(mainmenu, tearoff=0)
    settings.add_command(label="белый")
    settings.add_command(label="черный")
    settings.add_command(label="желтый")
    settings.add_command(label="оранжевый")
    settings.add_command(label="фиолетовый")
    settings.add_command(label="коричневый")
    settings.add_command(label="красный")
    settings.add_command(label="синий")
    settings.add_command(label="голубой")
    settings.add_command(label="зеленый")


    mainmenu.add_cascade(label="Поменять фон в программы", menu=settings)
    mainmenu.add_cascade(label="Поменять шрифт программы")