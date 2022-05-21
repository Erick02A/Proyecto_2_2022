from tkinter import *   #importar todo de tkinter
import tkinter as tk    #llamar a la libreria como tk
import pygame           #música
from threading import Thread 
import threading

End_game = lambda: exit()
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

def main_screen(): 
    """
    En primera instancia este modulo mostrará la interfaz del menú principal.
    End_game es una función lambda utilizada para terminar la ejecución del
    programa.
    """
    mainTrack= Thread(target=main_track,args=())
    mainTrack.start() #comando para ejecutar sonido con hilos
    
    main_menu = Tk()
    main_menu.title("ShipStack")
    main_menu.minsize(900,700)
    main_menu.resizable(width=YES,height=YES)

    main_canvas = tk.Canvas(main_menu, width=900, height=700, bg="blue")
    main_canvas.place(x=0,y=0)

    def our_command():
        print("works")
    #Se genera la barra de menu
    options_bar = Menu(main_menu)
    main_menu.config(menu=options_bar)
    #Columna del menu
    file_menu = Menu(options_bar)
    options_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Nuevo...",command=our_command)
    file_menu.add_separator()
    file_menu.add_command(label="Detener musica", command=stop_music)
    file_menu.add_command(label="Salir", command=End_game)
    #Columna del menu
    edit_menu = Menu(options_bar)
    options_bar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Nuevo...",command=our_command)
    edit_menu.add_separator()
    edit_menu.add_command(label="Detener musica", command=stop_music)
    edit_menu.add_command(label="Salir", command=End_game)

    main_menu.mainloop() #usado para tkinter
main_menu_thread= Thread(target = main_screen, args=())
main_menu_thread.start()
    
