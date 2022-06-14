from tkinter import *           #importar todo de tkinter
import tkinter as tk            #llamar a la libreria como tk
import pygame                   #pygame, por el momento para musica
from threading import Thread    #hilos 
import threading                #hilos
import os   
import time 
from random import *
from tkinter import messagebox
import pickle

def boom():
    """
    Función que implementa el sonido de colisión
    """
    pygame.mixer.init() 
    pygame.mixer.music.load("boom.wav")
    pygame.mixer.music.play(loops=0)
def pickSound():
    """
    Función que implementa el sonido de elección
    """
    pygame.mixer.init() 
    pygame.mixer.music.load("coin_falling.mp3")
    pygame.mixer.music.play(loops=0)
def tensionSound():
    """
    Función que implementa la musica de fondo
    """
    pygame.mixer.init() 
    pygame.mixer.music.load("tension.mpeg")
    pygame.mixer.music.play(-1)
    
def cargaimagen(nombre):
    """
    Funcion que carga las imagenes usadas en el programa
    Parametros: 
        Nombre: Nombre de la imagen en str
    return:
        la imagen
    """
    ruta = os.path.join("Imagenes",nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

class game:
    """
    La clase utilizada para el juego
    """
    def __init__(self,root,forma,barcos,tablero,nombre):
        """
        Se declaran muchos de los atributos más importantes de todo el juego
        """
        self.root=root
        self.barcos=barcos #int()
        self.tablero=tablero
        self.player_name=nombre
        self.main_canvas = tk.Canvas(root,width=1300,height=600, bg="green") #1600,800
        self.main_canvas.place(x=0,y=0)
        if forma == "PlayB":
            self.pantalla_gameB()
        if forma == "Play":
            self.pantalla_game()
        if forma == "Guardado":
            self.pantalla_guard()
        if forma == "Joistick":
            self.pantalla_joistick()
        
    def pantalla_game(self):
        """
        Este método desarrolla la pantalla del juego
        """
        self.canvas_enemi = Canvas(self.root,width=600,height=600,bg="red")
        self.canvas_enemi.place(x=0,y=0)
        self.canvas_player = Canvas(self.root,width=600,height=600,bg="blue")
        self.canvas_player.place(x=701,y=0)
        self.canvas_info=Canvas(self.root,width=100,height=600)
        self.canvas_info.place(x=601,y=0)
        #Se genera la barra de menu
        self.options_bar = Menu(self.root)
        self.root.config(menu=self.options_bar)

        self.abrir_juego = Menu(self.options_bar)
        self.options_bar.add_cascade(label="Guardar", menu=self.abrir_juego)
        self.abrir_juego.add_command(label="Guardar Partida",command=lambda:self.Guardar())
        self.abrir_juego.add_separator()
        self.segundos=0
        self.min=0
        self.mar_seg=Label(self.canvas_info,text="Tiempo. "+str(self.min)+":"+str(self.segundos),width=14,height=2,fg="black",bg="#b4b0f7")
        self.mar_seg.place(x=0,y=0)
        self.name=Label(self.canvas_info,text="Jugador: "+self.player_name,width=14,height=2,fg="black",bg="#b4b0f7")
        self.name.place(x=0,y=50)
        self.espacio_enemy=generabarcos()
        self.espacio_player=self.tablero
        self.pasa=True
        def Cronometro():
            """
            Función que implementa el cronómetro que aparece durante la partida
            """
            if self.segundos==60:
                self.segundos=0
                self.min+=1
            self.segundos+=1
            self.mar_seg.config(text="Tiempo: "+str(self.min)+":"+str(self.segundos)+"secs")
            self.root.after(1000,Cronometro)
        Hilo_crono=Thread(target=Cronometro())
        Hilo_crono.start()
        def actualiza_player():
            """
            Función que verifica qué color asignarle al espacio elegido por el jugador
            También verifica si el juego ya acaba en base a la situación
            En palabras simples, actualiza la posicion del jugador
            """
            for f in range(len(self.espacio_player)):
                for c in range(len(self.espacio_player[0])):
                    if self.espacio_player[f][c]==0:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")#cian
                    if self.espacio_player[f][c]==2:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#0000FF")#azul
                    if self.espacio_player[f][c]==1:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#555555")#gris
                    if self.espacio_player[f][c]==3:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#FF0000")#rojo
            self.root.after(500, tensionSound)
            if cuentabarcos(self.espacio_player)==0:
                print("LOSER")
                self.juegoterminado(False)
            if self.pasa==False:
                self.root.after(2000,disparo_enemy)
        actualiza_player()
        def disparo_enemy():
            """
            disparo_enemy
            Selecciona un cuadro aleatorio y le dispara desde el punto de vista del computador hacia el tablero del jugador.
            Modifica la variable booleana para asignarle el turno al otro jugador.
            """
            a=randint(0,9)
            b=randint(0,9)
            if self.espacio_player[b][a]==0:
                self.espacio_player[b][a]+=1
                pickSound()
                self.pasa=True
                actualiza_player()
            elif self.espacio_player[b][a]==2:
                self.espacio_player[b][a]+=1
                boom()
                self.pasa=False
                actualiza_player()
            else:
                disparo_enemy()

        def actualiza_enemy():
            """
            Función que verifica qué color asignarle al espacio elegido por el jugador
            También verifica si hay ganador en base a la situación
            En palabras simples, actualiza la posicion del enemigo
            """
            print(self.espacio_enemy)
            for f in range(len(self.espacio_enemy)):
                for c in range(len(self.espacio_enemy[0])):
                    if self.espacio_enemy[f][c]==0:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")#cian
                    if self.espacio_enemy[f][c]==2:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00AAFF")#celeste
                    if self.espacio_enemy[f][c]==1:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#555555")#gris
                    if self.espacio_enemy[f][c]==3:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#FF0000")#rojo
            if cuentabarcos(self.espacio_enemy)==0:
                print("WINNER")
                messagebox.showinfo("Felicidades","Le ganaste al computador")
                self.juegoterminado(True)
            if self.pasa==False:
                self.root.after(2000,disparo_enemy)
        actualiza_enemy()

        def Disparo(e):
            """
            Función que se encarga de conectar las acciones del usuario con la situación en la interfaz
            Basado en la bandera booleana, le asigna un espacio en matriz al click del usuario
            También se encarga de las validaciones que robustecen al juego, tales como si no es el turno del
            usuario pero este quiere elegir un espacio o bien si está eligiendo un mismo espacio más de una vez.
            """
            if self.pasa==True:
                counter=60
                def creaA(e):
                    """
                    Verifica las posiciones en el eje x
                    """
                    if e.x<counter:
                        a=0
                    elif e.x<counter*2:
                        a=1
                    elif e.x<counter*3:
                        a=2
                    elif e.x<counter*4:
                        a=3
                    elif e.x<counter*5:
                        a=4
                    elif e.x<counter*6:
                        a=5
                    elif e.x<counter*7:
                        a=6
                    elif e.x<counter*8:
                        a=7
                    elif e.x<counter*9:
                        a=8
                    elif e.x<counter*10:
                        a=9
                    return a
                def creaB(e):
                    """
                    Verifica las posiciones en el eje y
                    """
                    if e.y<counter:
                        a=0
                    elif e.y<counter*2:
                        a=1
                    elif e.y<counter*3:
                        a=2
                    elif e.y<counter*4:
                        a=3
                    elif e.y<counter*5:
                        a=4
                    elif e.y<counter*6:
                        a=5
                    elif e.y<counter*7:
                        a=6
                    elif e.y<counter*8:
                        a=7
                    elif e.y<counter*9:
                        a=8
                    elif e.y<counter*10:
                        a=9
                    return a
                a=creaA(e)
                b=creaB(e)
                if self.espacio_enemy[b][a]==1 or self.espacio_enemy[b][a]==3 : #disparada
                    tensionSound()
                    messagebox.showinfo("Error","Ya disparaste aquí")
                else:
                    if self.espacio_enemy[b][a]==0: #cian
                        self.espacio_enemy[b][a]+=1
                        pickSound()
                        self.pasa=False #linea para rotar turnos
                        actualiza=Thread(target= actualiza_enemy())
                        actualiza.start()
                        self.root.after(500, tensionSound)

                    if self.espacio_enemy[b][a]==2: #azul
                        self.espacio_enemy[b][a]+=1
                        boom()
                        actualiza=Thread(target= actualiza_enemy())
                        actualiza.start()
                        self.root.after(500, tensionSound)
            else:
                messagebox.showinfo("Error","No es tu turno")

        Click=Thread(target=self.canvas_enemi.bind("<Button-1>",Disparo))
        Click.start()
#############################################################################################################
    def pantalla_gameB(self):
        """
        Función que se encarga de la pantalla previa al juego.
        Aquí, el usuario encuentra una tabla sin naves y puede colocarlas a su gusto.
        """
        self.canvas_player = Canvas(self.root,width=600,height=600,bg="red")
        self.canvas_player.place(x=0,y=0)
        #Se genera la barra de menu
        self.options_bar = Menu(self.root)
        self.root.config(menu=self.options_bar)
        #Columna del menu para seguir el juego
        self.abrir_juego = Menu(self.options_bar)
        self.options_bar.add_cascade(label="Iniciar Partida", menu=self.abrir_juego)
        self.abrir_juego.add_command(label="Iniciar Partida",command=lambda:seguirJuego("Play"))
        self.abrir_juego.add_separator()
        self.contador=0
        self.espacio_player=[
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]   
        self.pasa=True #el turno es nuestro
        def actualiza_tablero():
            """
            Actualiza el tablero del enemigo con la respectiva, nueva casilla disparada
            """
            pickSound()
            for f in range(len(self.espacio_player)):
                for c in range(len(self.espacio_player[0])):
                    if self.espacio_player[f][c]==0:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")#cian
                    if self.espacio_player[f][c]==2:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#0000FF")#azul
        actualiza_tablero()

        def Coloca(e):
            """
            Selecciona la casilla escogida por el usuario 
            """
            if self.pasa==True:
                counter=60
                def creaA(e):
                    """
                    Verifica las posiciones en el eje x
                    """
                    if e.x<counter:
                        a=0
                    elif e.x<counter*2:
                        a=1
                    elif e.x<counter*3:
                        a=2
                    elif e.x<counter*4:
                        a=3
                    elif e.x<counter*5:
                        a=4
                    elif e.x<counter*6:
                        a=5
                    elif e.x<counter*7:
                        a=6
                    elif e.x<counter*8:
                        a=7
                    elif e.x<counter*9:
                        a=8
                    elif e.x<counter*10:
                        a=9
                    return a
                def creaB(e):
                    """
                    Verifica las posiciones en el eje y
                    """
                    if e.y<counter:
                        a=0
                    elif e.y<counter*2:
                        a=1
                    elif e.y<counter*3:
                        a=2
                    elif e.y<counter*4:
                        a=3
                    elif e.y<counter*5:
                        a=4
                    elif e.y<counter*6:
                        a=5
                    elif e.y<counter*7:
                        a=6
                    elif e.y<counter*8:
                        a=7
                    elif e.y<counter*9:
                        a=8
                    elif e.y<counter*10:
                        a=9
                    return a
                a=creaA(e)
                b=creaB(e)
                if self.contador!=self.barcos:
                    if self.espacio_player[b][a]!=2:
                        #Permite seleccionar un espacio
                        self.espacio_player[b][a]+=2
                        self.contador+=1
                        actualiza_tablero()
                else:
                    messagebox.showinfo("Error","Alcanzaste tu limite de barcos")
        Click=Thread(target=self.canvas_player.bind("<Button-1>",Coloca))
        Click.start()
        def seguirJuego(forma):
            """
            Una vez terminada la partida, esta función se encarga de redireccionar al usuario al menú principal
            """
            if cuentabarcos(self.espacio_player)==self.barcos:
                self.root.destroy()
                pantalla_juego=Tk()
                pantalla_juego.title("SHIPSTACK")
                pantalla_juego.config(cursor="pirate")
                pantalla_juego.minsize(1300,600)#
                pantalla_juego.resizable(width=NO,height=NO)
                partida=game(pantalla_juego,forma,0,self.espacio_player,self.player_name)
                pantalla_juego.mainloop()
            else:
                messagebox.showinfo("Error","No haz ingresado la cantidad de barcos indicada")
#############################################################################################################
    def pantalla_guard(self):
        """
        Función usada en caso de abrir una partida guardada en sus primeras líneas de código es una recreación de
        la pantalla del juego tal cual
        """
        self.canvas_enemi = Canvas(self.root,width=600,height=600,bg="red")
        self.canvas_enemi.place(x=0,y=0)
        self.canvas_player = Canvas(self.root,width=600,height=600,bg="blue")
        self.canvas_player.place(x=701,y=0)
        self.canvas_info=Canvas(self.root,width=100,height=600)
        self.canvas_info.place(x=601,y=0)
        #Se genera la barra de menu
        self.options_bar = Menu(self.root)
        self.root.config(menu=self.options_bar)

        self.abrir_juego = Menu(self.options_bar)
        self.options_bar.add_cascade(label="Guardar", menu=self.abrir_juego)
        self.abrir_juego.add_command(label="Guardar Partida",command=lambda:self.Guardar())
        self.abrir_juego.add_separator()
        self.segundos=self.sacaguard("seg")
        self.min=self.sacaguard("min")
        self.mar_seg=Label(self.canvas_info,text="Tiempo. "+str(self.min)+":"+str(self.segundos),width=14,height=2,fg="black",bg="#b4b0f7")
        self.mar_seg.place(x=0,y=0)
        self.name=Label(self.canvas_info,text="Jugador: "+self.sacaguard("name"),width=14,height=2,fg="black",bg="#b4b0f7")
        self.name.place(x=0,y=50)
        self.espacio_enemy=self.sacaguard("enemy")
        self.espacio_player=self.sacaguard("player")
        self.pasa=True
        def Cronometro():
            """
            Función que implementa el cronómetro que aparece durante la partida
            """
            if self.segundos==60:
                self.segundos=0
                self.min+=1
            self.segundos+=1
            self.mar_seg.config(text="Tiempo: "+str(self.min)+":"+str(self.segundos)+"secs")
            self.root.after(1000,Cronometro)
        Hilo_crono=Thread(target=Cronometro())
        Hilo_crono.start()
        def actualiza_player():
            """
            Función que verifica qué color asignarle al espacio elegido por el jugador
            También verifica si el juego ya acaba en base a la situación
            En palabras simples, actualiza la posicion del jugador
            """
            for f in range(len(self.espacio_player)):
                for c in range(len(self.espacio_player[0])):
                    if self.espacio_player[f][c]==0:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")#cian
                    if self.espacio_player[f][c]==2:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#0000FF")#axul
                    if self.espacio_player[f][c]==1:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#555555")#gris
                    if self.espacio_player[f][c]==3:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#FF0000")#rojo
            self.root.after(500, tensionSound)
            if cuentabarcos(self.espacio_player)==0:
                print("LOSER")
                self.juegoterminado(False)
            if self.pasa==False:
                self.root.after(2000,disparo_enemy)
        actualiza_player()
        def disparo_enemy():
            """
            disparo_enemy
            Selecciona un cuadro aleatorio y le dispara desde la posición del computador hacia el tablero del jugador
            """
            a=randint(0,9)
            b=randint(0,9)
            if self.espacio_player[b][a]==0:
                self.espacio_player[b][a]+=1
                pickSound()
                self.pasa=True
                actualiza_player()
            elif self.espacio_player[b][a]==2:
                self.espacio_player[b][a]+=1
                boom()
                self.pasa=False
                actualiza_player()
            else:
                disparo_enemy()

        def actualiza_enemy():
            """
            Función que verifica qué color asignarle al espacio elegido por el jugador
            También verifica si hay ganador en base a la situación
            En palabras simples, actualiza la posicion del enemigo
            """
            print(self.espacio_enemy)
            for f in range(len(self.espacio_enemy)):
                for c in range(len(self.espacio_enemy[0])):
                    if self.espacio_enemy[f][c]==0:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")#cian
                    if self.espacio_enemy[f][c]==2:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00AAFF")#celeste
                    if self.espacio_enemy[f][c]==1:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#555555")#gris
                    if self.espacio_enemy[f][c]==3:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#FF0000")#rojo
            if cuentabarcos(self.espacio_enemy)==0:
                print("WINNER")
                messagebox.showinfo("Felicidades","Le ganaste al computador")
                self.juegoterminado(True)
            if self.pasa==False:
                self.root.after(2000,disparo_enemy)
        actualiza_enemy()

        def Disparo(e):
            """
            Función que se encarga de conectar las acciones del usuario con la situación en la interfaz
            Basado en la bandera booleana, le asigna un espacio en matriz al click del usuario
            También se encarga de las validaciones que robustecen al juego, tales como si no es el turno del
            usuario pero este quiere elegir un espacio o bien si está eligiendo un mismo espacio más de una vez.
            """
            if self.pasa==True:
                counter=60
                def creaA(e):
                    """
                    Verifica las posiciones en el eje x
                    """
                    if e.x<counter:
                        a=0
                    elif e.x<counter*2:
                        a=1
                    elif e.x<counter*3:
                        a=2
                    elif e.x<counter*4:
                        a=3
                    elif e.x<counter*5:
                        a=4
                    elif e.x<counter*6:
                        a=5
                    elif e.x<counter*7:
                        a=6
                    elif e.x<counter*8:
                        a=7
                    elif e.x<counter*9:
                        a=8
                    elif e.x<counter*10:
                        a=9
                    return a
                def creaB(e):
                    """
                    Verifica las posiciones en el eje y
                    """
                    if e.y<counter:
                        a=0
                    elif e.y<counter*2:
                        a=1
                    elif e.y<counter*3:
                        a=2
                    elif e.y<counter*4:
                        a=3
                    elif e.y<counter*5:
                        a=4
                    elif e.y<counter*6:
                        a=5
                    elif e.y<counter*7:
                        a=6
                    elif e.y<counter*8:
                        a=7
                    elif e.y<counter*9:
                        a=8
                    elif e.y<counter*10:
                        a=9
                    return a
                a=creaA(e)
                b=creaB(e)
                if self.espacio_enemy[b][a]==1 or self.espacio_enemy[b][a]==3 : #disparada
                    tensionSound()
                    messagebox.showinfo("Error","Ya disparaste aquí")
                else:
                    if self.espacio_enemy[b][a]==0: #cian
                        self.espacio_enemy[b][a]+=1
                        pickSound()
                        self.pasa=False #linea para rotar turnos
                        actualiza=Thread(target= actualiza_enemy())
                        actualiza.start()
                        self.root.after(500, tensionSound)

                    if self.espacio_enemy[b][a]==2: #azul
                        self.espacio_enemy[b][a]+=1
                        boom()
                        actualiza=Thread(target= actualiza_enemy())
                        actualiza.start()
                        self.root.after(500, tensionSound)
            else:
                messagebox.showinfo("Error","No es tu turno")

        Click=Thread(target=self.canvas_enemi.bind("<Button-1>",Disparo))
        Click.start()
    def sacaguard(self,saca):
        """
        En caso de que el usuario decida que quiere seguir jugando, esta función se encarga de devolver los datos
        """
        archivo=open("partida.txt","rb")
        lista=pickle.load(archivo)
        if saca=="seg":
            return lista[2]
        if saca=="name":
            return lista[3]
        if saca=="enemy":
            return lista[0]
        if saca=="player":
            return lista[1]
        if saca=="min":
            return lista[4]
    def Guardar(self):
        """
        En caso de que el usuario decida seguir jugando después, esta función se encarga de guardar la partida
        """
        archivo=open("partida.txt","wb")
        pickle.dump([self.espacio_enemy,self.espacio_player,self.segundos,self.player_name,self.min],archivo)
        archivo.close()
    def juegoterminado(self,ganar):
        """
        Al finalizar el juego
        La siguiente función se encarga de evaluar los datos.
        Esto con el fin de verificar si la puntación debe ser incluída en el top 10.
        """
        if ganar==True:
            def abrir_txt():#tiene como argumentos el nombre y puntaje del jugador que finalizo partida 
                archivo= open("puntajes.txt","r") 
                nombres = archivo.readlines()#guarda los nombres y puntajes en una variable
                archivo.close() 
                comparador(nombres,"",0)#llama a la funcion que compara el puntaje con los del top 7 
    
            def comparador(lista, res ,i):
                """
                Es la función encargada de monitorear que solo los mejores 10 tiempos estén en el top 10
                """
                if i == 10: #contador que verifica que se revise hasta el lugar 10 
                    return actualizar(res) 
                divisor = lista[0].split(";")#separa el nombre del puntaje y los guarda en una lista
                Punt = divisor[1].split(":")#obtiene el puntaje de la lista y lo convierte en entero
                actualPunt=(int(Punt[0])*100)+int(Punt[1])
                if actualPunt > (self.min*100+self.segundos): #compara si el puntaje obtenido es mayor a uno del top 7          
                    res += self.player_name + ";" + str(self.min)+":"+str(self.segundos)+ "\n"#guarda el nombre y puntaje del jugador en el string de resultado           
                    #usando el contador +1 se obtiene la posición que consiguió y se muestra en un label junto con el puntaje
                    messagebox.showinfo("Felicidades","Obtuviste la posición "+str(i+1)+"\n"+
                    "Con un tiempo de "+str(self.min)+":"+str(self.segundos))
                    self.segundos=61
                    self.min=2000
                    return comparador(lista,res,i+1)#cambia el valor del puntaje a 0 para no reemplazar los demas puntajes menores
                comparador(lista[1:],res+lista[0],i+1)#guarda los datos del top 7 cuando el puntaje del jugador no es superior a alguno de estos

            #funcion que obtiene la variable con los datos del nuevo top 7 y actualiza el archivo de texto con estos    
            def actualizar(nuevos):
                """
                Se encarga de actualizar los nuevos puntajes registrados en el sistema
                """
                archivo = open("puntajes.txt","w") 
                archivo.write(nuevos) 
                archivo.close()
            abrir_txt()
        elif ganar==False:
            messagebox.showinfo("Manco","Perdiste, juegue bien manco")
        self.root.destroy()
        import ShipStack       
def cuentabarcos(pant):
    """
    Cuenta la cantidad de barcos, si esta es 0, otras funciones se encargarán de dar por terminada la partida
    """
    cant=0
    for filas in pant:
        for lugar in filas:
            if lugar==2:
                cant+=1
    return cant
def generabarcos():
    """
    Funcion encargada de generar los barcos para el tablero enemigo
    """
    pant=[
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]
    for i in range(10):
        a=randint(0,9)
        b=randint(0,9)
        if pant[a][b]!=2:
            pant[a][b]=2
    return pant
