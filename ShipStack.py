from tkinter import *           #importar todo de tkinter
import tkinter as tk            #llamar a la libreria como tk
import pygame                   #música
from threading import Thread    #hilos 
import threading                #hilos
import os                       #carga de imagenes
from Pruebas import *

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
stop_music = lambda: pygame.mixer.music.stop()

def cargaimagen(nombre):
    """
    Funcion que cargas las imagenes usadas en el programa
    Parametros: 
        Nombre: Nombre de la imagen en str
    return:
        la imagen
    """
    ruta = os.path.join("Imagenes",nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

End_game = lambda: main_menu.destroy()
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
    def instrucciones(self):
        """
        Este metodo le indica al usuario mediante una etiqueta cómo jugar.
        """
        self.canvas = Canvas(self.root, width=1200, height=700)
        self.canvas.place(x=0, y=0)
        self.imagen=cargaimagen("bg.png")
        self.canvas.create_image(550,350, image=self.imagen)

        self.texto = Label(self.canvas, text="CÓMO JUGAR:\n*Por definirse*", font=("Times New Roman", 15),fg="#000000",bg="#04faee")
        self.texto.place(x=300,y=15)
        #Botón para volver de la seccion instrucciones al menú
        self.Boton_instruccionesToMain = Button(self.canvas, text="VOLVER",font=("Times New Roman", 15),bg="#04faee",command=self.pantalla_principal)
        self.Boton_instruccionesToMain.place(x=350,y=520, width=80, height=30)

    def creditos(self):
        """
        Metodo que genera el canvas de la pantalla de Creditos con todos sun widgets
        Parametros: 
            self: parametro que se usa para modificar cosas dentro de la clase
        return:
            no se retorna 
        """
        self.canvas = Canvas(self.root, width=1200, height=700)
        self.canvas.place(x=0, y=0)
        self.imagen=cargaimagen("bg.png")
        self.canvas.create_image(550,350, image=self.imagen)

        self.texto = Label(self.canvas, text="Instituto Tecnologico de Costa Rica\n"
                           "Ingeniería en Computadores\n"
                           "CE 1102-Taller de Programación\n"
                           "Profesor: Jason Leitó Jiménez\n"
                           "Versión 1.0\n"
                           "última modificación: 14/06/2022\n"
                           "Desarrolladores:\n", font=("Times New Roman", 15),fg="#000000",bg="#04faee")
        self.texto.place(x=150,y=15)

        self.Erick = Label(self.canvas, text="Erick Abarca Pérez\n2022284936", font=("Times New Roman", 15),fg="#000000",bg="#04faee")
        self.Erick.place(x=3, y=200)

        self.Jose = Label(self.canvas, text="José Ignacio Rivera Mora\n2022227827", font=("Times New Roman", 15),fg="#000000",bg="#04faee")
        self.Jose.place(x=300, y=200)

        self.imagen_Erick= cargaimagen("Erick.png")
        self.foto_Erick = Label(self.canvas, image= self.imagen_Erick)
        self.foto_Erick.place(x=3, y=250)
        
        self.imagen_Jose= cargaimagen("Jose.png")
        self.foto_Jose = Label(self.canvas, image= self.imagen_Jose)
        self.foto_Jose.place(x=300, y=250)
        #Botón para volver de la seccion creditos al menú
        self.Boton_creditosToMain = Button(self.canvas, text="VOLVER",font=("Times New Roman", 15),bg="#04faee",command=self.pantalla_principal)
        self.Boton_creditosToMain.place(x=350,y=520, width=80, height=30)
        
    def pantalla_principal(self):
        """
        Aqui dentro van todos los widgets de la pantalla principal.
        1. Se llama a la función de la música
        2. Se agrega el fondo de pantalla
        3. Se implementa la barra de opciones
        4. Se solicita el nombre del usuario y la cantidad de naves a usar con su respectivo tipo
        """
        main_track()

        self.main_canvas = tk.Canvas(self.root, width=900, height=700, bg="blue")
        self.main_canvas.place(x=0,y=0)
        self.main_bg = cargaimagen("bg(1).png")
        self.main_canvas.create_image(1,1,image=self.main_bg)
        
        #Se genera la barra de menu
        self.options_bar = Menu(self.root)
        self.root.config(menu=self.options_bar)
        #Columna del menu para abrir una partida guardada
        self.abrir_juego = Menu(self.options_bar)
        self.options_bar.add_cascade(label="ABRIR JUEGO", menu=self.abrir_juego)
        self.abrir_juego.add_command(label="Opción vacante")
        self.abrir_juego.add_separator()
        #Columna del menu para acceder al salón de la fama
        self.fama_menu = Menu(self.options_bar)
        self.options_bar.add_cascade(label="SALÓN DE LA FAMA", menu=self.fama_menu)
        self.fama_menu.add_command(label="Opción vacante")
        #Columna del menu para acceder a la seccion de ayudas
        self.help_menu = Menu(self.options_bar)
        self.options_bar.add_cascade(label="AYUDA", menu=self.help_menu)
        self.help_menu.add_command(label="CÓMO JUGAR", command=self.instrucciones)
        self.help_menu.add_command(label="CREDITOS", command=self.creditos)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="DETENER MUSICA", command=stop_music)
        self.help_menu.add_command(label="SALIR DEL JUEGO", command=End_game)

        startGame = Button(main_menu, text="   JUGAR    ",width=30, height= 5, bg='#E00707', font=('calibre',10, 'bold'))
        startGame.place(x=500,y=500)
        
main_menu = Tk()
pantalla_principal = main_screen(main_menu) #se cambió la palabra ventana por pantalla, parece funcionar igual
main_menu.title("SHIPSTACK")
main_menu.config(cursor="target")
main_menu.minsize(700,600)
main_menu.resizable(width=NO,height=NO)
main_menu.mainloop() #usado para tkinter
