from tkinter import *   #importar todo de tkinter
import tkinter as tk    #llamar a la libreria como tk
import pygame           #música
from threading import Thread 
import threading

End_game = lambda: main_menu.destroy()
stop_music = lambda: pygame.mixer.music.stop()

def main_track():
    """
    Esta es la función para ejecutar el sonido con la bibloteca pygame.
    Primero se inicializa el mixer y se escoge el archivo.
    Luego hay que indicar la cantidad de reproducciones para que ejecute la
    acción.

    stop_music es una función utilizada para detener la música
    """
    pygame.mixer.init() 
    pygame.mixer.music.load("ShipStackMaintheme.mp3")
    pygame.mixer.music.play(loops=0)

class main_screen: 
    """
    En primera instancia esta clase soporta todo lo relacionado a pantallas,
    créditos y puntajes.
    End_game es una función lambda utilizada para terminar la ejecución del
    programa.
    """
    def __init__(self,root):
        self.root=root
        self.main_canvas = tk.Canvas(root, width=900, height=700, bg="blue")
        self.main_canvas.place(x=0,y=0)
        self.pantalla_principal()
    def pantalla_principal(self):
        """
        Aqui dentro van todos los widgets de la pantalla principal.
        """
        main_track()
        #Se genera la barra de menu
        self.options_bar = Menu(self.root)
        self.root.config(menu=self.options_bar)
        #Columna del menu
        self.file_menu = Menu(self.options_bar)
        self.options_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Nuevo...")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Detener musica", command=stop_music)
        self.file_menu.add_command(label="Salir", command=End_game)
        #Columna del menu
        self.edit_menu = Menu(self.options_bar)
        self.options_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Nuevo...")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Detener musica", command=stop_music)
        self.edit_menu.add_command(label="Salir", command=End_game)
    
main_menu = Tk()
ventana_principal = main_screen(main_menu)
main_menu.title("ShipStack")
main_menu.minsize(900,700)
main_menu.resizable(width=YES,height=YES)

main_menu.mainloop() #usado para tkinter
    
