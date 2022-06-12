from tkinter import *           #importar todo de tkinter
import tkinter as tk            #llamar a la libreria como tk
import pygame                   #música
from threading import Thread    #hilos 
import threading                #hilos
import os                       #carga de imagenes
from Juego import game
from tkinter import messagebox

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

    def requisitos(self):
        """
        Este metodo le indica al usuario mediante una etiqueta cómo ingresar al top 10.
        """
        self.canvas = Canvas(self.root, width=1200, height=700)
        self.canvas.place(x=0, y=0)
        self.imagen=cargaimagen("bg.png")
        self.canvas.create_image(550,350, image=self.imagen)

        self.texto = Label(self.canvas, text="¿CÓMO INGRESAR AL TOP 10?:\n*Juegue bien xd*", font=("Times New Roman", 15),fg="#000000",bg="#04faee")
        self.texto.place(x=300,y=15)
        #Botón para volver de la seccion  al menú
        self.Boton_requisitosToMain = Button(self.canvas, text="VOLVER",font=("Times New Roman", 15),bg="#04faee",command=self.pantalla_principal)
        self.Boton_requisitosToMain.place(x=350,y=520, width=80, height=30)

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
                           "Profesor: Jason Leitón Jiménez\n"
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
        
    def puntajes(self): #parámetros : self
        """
        Metodo que genera el canvas de la pantalla de puntajes
        Parametros: 
            self: parametro que se usa para modificar cosas dentro de la clase
        """
        self.canvas= Canvas(self.root,width=1200,height=700,bg="#ffffff")
        self.canvas.place(x=0, y=0)
        #Se carga una imagen de fondo
        """self.imagen=cargaimagen("Trofeo (1).png")
        self.canvas.create_image(600,350, image=self.imagen)"""
        # Lugar donde se mostrara el puntaje
        self.score = Label(self.canvas, text="TOP 10: ", font=("Helvetica", 15), fg="#f55cdf", bg="#04faee")
        self.score.place(x=580,y=30) 
        # Boton para regresar ala pantalla principal
        self.boton_back_punt = Button(self.canvas, text="Back",font=("Times New Roman", 18),bg="#04faee",command=self.pantalla_principal)
        self.boton_back_punt.place(x=550,y=520, width=80, height=30)
        #funcion que habre el archivo de puntajes y los guarda en una variable
        def abrir_puntajes(): 
            """
            funcion que habre el archivo de puntajes y los guarda en una variable
            Parametros: 
                Ninguno
            return:
                no se retorna 
            """
            archivo= open("puntajes.txt") 
            nombres = archivo.readlines() #guarda los nombres y puntajes en una variable
            archivo.close() 
            separar(nombres,[],[])#llama a la funcion para separar los nombres y puntajes
        # Se inicia la funcion de puntajes en un hilo
        top10 = Thread(target= abrir_puntajes) 
        top10.start()
        def separar(lista,nombre,puntos):
            """
            funcion que separa los nobres de los puntos
            Parametros: 
                lista: variable con los nobres y sus puntajes
                nombre: variable que guarda los nombre
                puntos: Variable que guarda los puntos
            return:
                no se retorna 
            """
            if lista==[]:
                h1=Thread(target=mostrar(nombre,350,50))
                h2=Thread(target=mostrar(puntos,450,50))
                h1.start()
                h2.start()
            else:
                divisor=lista[0].split(";")
                nombre+=[divisor[0]]
                puntos+=[divisor[1]]
                separar(lista[1:],nombre,puntos)

        def mostrar(nombres,x1,y1):
            """
            funcion que coloca cada nombre o cada puntaje en un label en el canvas de puntajes
            Parametros: 
                x1: variable que va aumentando para generar otra coordenada en x
                nombre: variable con los nobres o puntos
                y1: variable que va aumentando para generar otra coordenada en y
            return:
                no se retorna 
            """
            if nombres!=[]:
                self.info1= Label(self.canvas, text=nombres[0], font=("Helvetica", 15), fg="white", bg="black")
                self.info1.place(x=x1,y=y1)
                y1+=50
                mostrar(nombres[1:],x1,y1)

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
        self.titulo = Label(self.main_canvas, text="SHIPSTACK", font=("Helvetica", 12), fg="#000000", bg="#04faee")
        self.titulo.place(x=510,y=30,width=180, height=130)

        self.player_name = Entry(self.main_canvas)
        self.player_name.place(x=550,y=155,width=100,height=30)

        self.cantBarcos = Entry(self.main_canvas)
        self.cantBarcos.place(x=550,y=200,width=100,height=30)
        #Se genera la barra de menu
        self.options_bar = Menu(self.root)
        self.root.config(menu=self.options_bar)
        #Columna del menu para abrir una partida guardada
        self.abrir_juego = Menu(self.options_bar)
        self.options_bar.add_cascade(label="ABRIR JUEGO", menu=self.abrir_juego)
        self.abrir_juego.add_command(label="Abrir partida guardada",command=lambda:abrirjuego("Guardado"))
        self.abrir_juego.add_separator() 
        #Columna del menu para acceder al salón de la fama
        self.fama_menu = Menu(self.options_bar)
        self.options_bar.add_cascade(label="SALÓN DE LA FAMA", menu=self.fama_menu)
        self.fama_menu.add_command(label="TOP 10",command=self.puntajes)
        self.fama_menu.add_command(label="¿CÓMO ENTRAR EN EL TOP 10?",command=self.requisitos)

        #Columna del menu para acceder a la seccion de ayudas
        self.help_menu = Menu(self.options_bar)
        self.options_bar.add_cascade(label="AYUDA", menu=self.help_menu)
        self.help_menu.add_command(label="CÓMO JUGAR", command=self.instrucciones)
        self.help_menu.add_command(label="CREDITOS", command=self.creditos)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="DETENER MUSICA", command=stop_music)
        self.help_menu.add_command(label="SALIR DEL JUEGO", command=End_game)
                
        startGame = Button(main_menu, text="   JUGAR    ",width=30, height= 5, bg='#E00707', font=('calibre',10, 'bold'),command=lambda:abrirjuego("PlayB"))
        startGame.place(x=500,y=500)
    
        def abrirjuego(forma):
            if self.player_name.get() != "":
                x=self.cantBarcos.get()
                y=self.player_name.get()
                if isinstance(int(x),int):
                        x=int(x)
                        main_menu.destroy()
                        stop_music()
                        pantalla_juego=Tk()
                        pantalla_juego.title("SHIPSTACK")
                        pantalla_juego.config(cursor="pirate")
                        pantalla_juego.minsize(600,600)#
                        pantalla_juego.resizable(width=NO,height=NO)
                        partida=game(pantalla_juego,forma,x,[],y)
                        pantalla_juego.mainloop()
                else:
                        messagebox.showinfo("Error","Debe ingresar un numero")
                """except:
                    pass"""
            if forma=="Guardado":
                main_menu.destroy()
                pantalla_juego=Tk()
                pantalla_juego.title("SHIPSTACK")
                pantalla_juego.config(cursor="pirate")
                pantalla_juego.minsize(1300,600)#
                pantalla_juego.resizable(width=NO,height=NO)
                partida=game(pantalla_juego,forma)
                pantalla_juego.mainloop()


main_menu = Tk()
pantalla_principal = main_screen(main_menu) #se cambió la palabra ventana por pantalla, parece funcionar igual
main_menu.title("SHIPSTACK")
main_menu.config(cursor="target")
main_menu.minsize(1000,600)
main_menu.resizable(width=NO,height=NO)
main_menu.mainloop() #usado para tkinter
