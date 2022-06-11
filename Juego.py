from tkinter import *           #importar todo de tkinter
import tkinter as tk            #llamar a la libreria como tk
import pygame                   #pygame, por el momento para musica
from threading import Thread    #hilos 
import threading                #hilos
import os   
import time 
from random import *
from tkinter import messagebox

def boom():
    pygame.mixer.init() 
    pygame.mixer.music.load("boom.wav")
    pygame.mixer.music.play(loops=0)

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


class game:
    def __init__(self,root,forma,barcos):
        self.root=root
        self.barcos=barcos #int()
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
        self.canvas_enemi = Canvas(self.root,width=600,height=600,bg="red")
        self.canvas_enemi.place(x=0,y=0)
        self.canvas_player = Canvas(self.root,width=600,height=600,bg="blue")
        self.canvas_player.place(x=701,y=0)
        self.canvas_info=Canvas(self.root,width=100,height=600)
        self.canvas_info.place(x=601,y=0)
        self.segundos=0
        self.min=0
        self.mar_seg=Label(self.canvas_info,text="Tiempo: "+str(self.min)+":"+str(self.segundos),width=9,height=2,fg="black",bg="#b4b0f7")
        self.mar_seg.place(x=0,y=0)
        ganar=True
        """self.botonVolver =Button(self.root, text="VOLVER", command=self.juegoterminado(ganar))
        self.botonVolver.place(x="200",y="100")"""
        self.espacio_enemy=generabarcos()        
        self.espacio_player=[
        [0,0,0,0,0,0,0,2,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,2,0,0,2,0,2],
        [0,0,0,0,0,0,2,0,0,0],
        [0,0,2,0,0,0,2,0,0,0],
        [0,0,2,0,0,0,2,0,0,2],
        [0,0,2,0,0,0,0,0,2,0],
        [0,0,2,0,0,0,0,0,0,0],
        [0,0,2,0,2,0,0,2,0,0],
        [0,0,2,0,0,0,0,0,0,0]
        ]
        self.pasa=True
        def Cronometro():
            if self.segundos==60:
                self.segundos=0
                self.min+=1
            self.segundos+=1
            self.mar_seg.config(text="Tiempo. "+str(self.min)+":"+str(self.segundos))
            self.root.after(1000,Cronometro)
        Hilo_crono=Thread(target=Cronometro())
        Hilo_crono.start()
        def actualiza_player():
            for f in range(len(self.espacio_player)):
                for c in range(len(self.espacio_player[0])):
                    if self.espacio_player[f][c]==0:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")
                    if self.espacio_player[f][c]==2:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#0000FF")
                    if self.espacio_player[f][c]==1:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#555555")
                    if self.espacio_player[f][c]==3:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#FF0000")
            if cuentabarcos(self.espacio_player)==0:
                print("LOSER")
                self.juegoterminado(False)
        actualiza_player()
        def disparo_enemy():
            """
            disparo_enemy
            Selecciona un cuadro aleatorio y le dispara desde la posición del computador hacia el tablero del jugador
            """
            a=randint(0,9)
            b=randint(0,9)
            if self.espacio_player[b][a]!=1 and self.espacio_player[b][a]!=3:
                self.espacio_player[b][a]+=1
                self.pasa=True
                actualiza_player()
            else:
                disparo_enemy()

        def actualiza_enemy():
            print(self.espacio_enemy)
            for f in range(len(self.espacio_enemy)):
                for c in range(len(self.espacio_enemy[0])):
                    if self.espacio_enemy[f][c]==0:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")
                    if self.espacio_enemy[f][c]==2:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")
                    if self.espacio_enemy[f][c]==1:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#555555")
                    if self.espacio_enemy[f][c]==3:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#FF0000")
            if cuentabarcos(self.espacio_enemy)==0:
                print("WINER")
                self.juegoterminado(True)
            if self.pasa==False:
                self.root.after(2000,disparo_enemy)
        actualiza_enemy()

        def Disparo(e):
            if self.pasa==True:
                counter=60
                def creaA(e):
                    if e.x<counter:
                        a=0
                        boom()
                    elif e.x<counter*2:
                        a=1
                        boom()
                    elif e.x<counter*3:
                        a=2
                        boom()
                    elif e.x<counter*4:
                        a=3
                        boom()
                    elif e.x<counter*5:
                        a=4
                        boom()
                    elif e.x<counter*6:
                        a=5
                        boom()
                    elif e.x<counter*7:
                        a=6
                        boom()
                    elif e.x<counter*8:
                        a=7
                        boom()
                    elif e.x<counter*9:
                        a=8
                        boom()
                    elif e.x<counter*10:
                        a=9
                        boom()
                    return a
                def creaB(e):
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
                if self.espacio_enemy[b][a]!=1 and self.espacio_enemy[b][a]!=3:
                    self.espacio_enemy[b][a]+=1
                    self.pasa=False
                    actualiza_enemy()
                else:
                    messagebox.showinfo("Error","Ya disparaste en esta casilla")
            else:
                messagebox.showinfo("Error","No es tu turno")

        Click=Thread(target=self.canvas_enemi.bind("<Button-1>",Disparo))
        Click.start()
#############################################################################################################
    def pantalla_gameB(self):
        self.canvas_enemi = Canvas(self.root,width=600,height=600,bg="red")
        self.canvas_enemi.place(x=0,y=0)
        #Se genera la barra de menu
        self.options_bar = Menu(self.root)
        self.root.config(menu=self.options_bar)
        #Columna del menu para abrir una partida guardada
        self.abrir_juego = Menu(self.options_bar)
        self.options_bar.add_cascade(label="ABRIR JUEGO", menu=self.abrir_juego)
        self.abrir_juego.add_command(label="Abrir partida guardada",command=lambda:seguirJuego("Play"))
        self.abrir_juego.add_separator()
        self.espacio_enemy=[
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
            print(self.espacio_enemy,"hols")
            for f in range(len(self.espacio_enemy)):
                for c in range(len(self.espacio_enemy[0])):
                    if self.espacio_enemy[f][c]==0:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")
                    if self.espacio_enemy[f][c]==1:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#FF0000")
        actualiza_tablero()

        def Disparo(e):
            """
            Selecciona la casilla escogida por el usuario para x motivo
            """
            if self.pasa==True:
                counter=60
                def creaA(e):
                    if e.x<counter:
                        a=0
                        print("boom")
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
                if self.espacio_enemy[b][a]!=1 and self.espacio_enemy[b][a]!=3:
                    self.espacio_enemy[b][a]+=1
                    self.pasa=True #era false
                    actualiza_tablero()
        Click=Thread(target=self.canvas_enemi.bind("<Button-1>",Disparo))
        Click.start()
        def seguirJuego(forma):
            self.root.destroy()
            pantalla_juego=Tk()
            pantalla_juego.title("SHIPSTACK")
            pantalla_juego.config(cursor="pirate")
            pantalla_juego.minsize(1200,600)#
            pantalla_juego.resizable(width=NO,height=NO)
            partida=game(pantalla_juego,forma,self.cantBarcos)
            pantalla_juego.mainloop()
#############################################################################################################
    def pantalla_guard(self):
        self.canvas_enemi = Canvas(self.root,width=600,height=600,bg="red")
        self.canvas_enemi.place(x=0,y=0)
        self.canvas_player = Canvas(self.root,width=600,height=600,bg="blue")
        self.canvas_player.place(x=701,y=0)
        self.canvas_info=Canvas(self.root,width=100,height=600)
        self.canvas_info.place(x=601,y=0)
        self.segundos=0
        self.min=0
        self.mar_seg=Label(self.canvas_info,text="Tiempo. "+str(self.min)+":"+str(self.segundos),width=9,height=2,fg="black",bg="#b4b0f7")
        self.mar_seg.place(x=0,y=0)
        self.espacio_enemy=generabarcos()        
        self.espacio_player=[
        [0,0,0,0,0,0,0,2,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,2,0,0,2,0,2],
        [0,0,0,0,0,0,2,0,0,0],
        [0,0,2,0,0,0,2,0,0,0],
        [0,0,2,0,0,0,2,0,0,2],
        [0,0,2,0,0,0,0,0,2,0],
        [0,0,2,0,0,0,0,0,0,0],
        [0,0,2,0,2,0,0,2,0,0],
        [0,0,2,0,0,0,0,0,0,0]
        ]
        def Cronometro():
            if self.segundos==60:
                self.segundos=0
                self.min+=1
            self.segundos+=1
            self.mar_seg.config(text="Tiempo. "+str(self.min)+":"+str(self.segundos))
            self.root.after(1000,Cronometro)
        Hilo_crono=Thread(target=Cronometro())
        Hilo_crono.start()
        def actualiza_player():
            for f in range(len(self.espacio_player)):
                for c in range(len(self.espacio_player[0])):
                    if self.espacio_player[f][c]==0:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")
                    if self.espacio_player[f][c]==2:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#0000FF")
                    if self.espacio_player[f][c]==1:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#555555")
                    if self.espacio_player[f][c]==3:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#FF0000")
            if cuentabarcos(self.espacio_player)==0:
                print("LOSER")
                
        actualiza_player()
        def disparo_enemy():
            a=randint(0,9)
            b=randint(0,9)
            if self.espacio_player[b][a]!=1 and self.espacio_player[b][a]!=3:
                self.espacio_player[b][a]+=1
                actualiza_player()
            else:
                disparo_enemy()

        def actualiza_enemy():
            for f in range(len(self.espacio_enemy)):
                for c in range(len(self.espacio_enemy[0])):
                    if self.espacio_enemy[f][c]==0:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")
                    if self.espacio_enemy[f][c]==2:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")
                    if self.espacio_enemy[f][c]==1:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#555555")
                    if self.espacio_enemy[f][c]==3:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#FF0000")
            if cuentabarcos(self.espacio_enemy)==0:
                print("WINNER")
                
            disparo_enemy()
        actualiza_enemy()

        def Disparo(e):
            def creaA(e):
                if e.x<60:
                    a=0
                elif e.x<120:
                    a=1
                elif e.x<180:
                    a=2
                elif e.x<240:
                    a=3
                elif e.x<300:
                    a=4
                elif e.x<360:
                    a=5
                elif e.x<420:
                    a=6
                elif e.x<480:
                    a=7
                elif e.x<540:
                    a=8
                elif e.x<600:
                    a=9
                return a
            def creaB(e):
                if e.y<60:
                    a=0
                elif e.y<120:
                    a=1
                elif e.y<180:
                    a=2
                elif e.y<240:
                    a=3
                elif e.y<300:
                    a=4
                elif e.y<360:
                    a=5
                elif e.y<420:
                    a=6
                elif e.y<480:
                    a=7
                elif e.y<540:
                    a=8
                elif e.y<600:
                    a=9
                return a
            a=creaA(e)
            b=creaB(e)
            if self.espacio_enemy[b][a]!=1 and self.espacio_enemy[b][a]!=3:
                self.espacio_enemy[b][a]+=1
                actualiza_enemy()
        Click=Thread(target=self.canvas_enemi.bind("<Button-1>",Disparo))
        Click.start()
    
    def pantalla_joistick(self):
        self.canvas_enemi = Canvas(self.root,width=600,height=600,bg="red")
        self.canvas_enemi.place(x=0,y=0)
        self.canvas_player = Canvas(self.root,width=600,height=600,bg="blue")
        self.canvas_player.place(x=701,y=0)
        self.canvas_info=Canvas(self.root,width=100,height=600)
        self.canvas_info.place(x=601,y=0)
        self.segundos=0
        self.min=0
        self.mar_seg=Label(self.canvas_info,text="Tiempo. "+str(self.min)+":"+str(self.segundos),width=9,height=2,fg="black",bg="#b4b0f7")
        self.mar_seg.place(x=0,y=0)
        self.espacio_enemy=generabarcos()        
        self.espacio_player=[
        [0,0,0,0,0,0,0,2,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,2,0,0,2,0,2],
        [0,0,0,0,0,0,2,0,0,0],
        [0,0,2,0,0,0,2,0,0,0],
        [0,0,2,0,0,0,2,0,0,2],
        [0,0,2,0,0,0,0,0,2,0],
        [0,0,2,0,0,0,0,0,0,0],
        [0,0,2,0,2,0,0,2,0,0],
        [0,0,2,0,0,0,0,0,0,0]
        ]
        def Cronometro():
            if self.segundos==60:
                self.segundos=0
                self.min+=1
            self.segundos+=1
            self.mar_seg.config(text="Tiempo. "+str(self.min)+":"+str(self.segundos))
            self.root.after(1000,Cronometro)
        Hilo_crono=Thread(target=Cronometro())
        Hilo_crono.start()
        def actualiza_player():
            for f in range(len(self.espacio_player)):
                for c in range(len(self.espacio_player[0])):
                    if self.espacio_player[f][c]==0:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")
                    if self.espacio_player[f][c]==2:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#0000FF")
                    if self.espacio_player[f][c]==1:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#555555")
                    if self.espacio_player[f][c]==3:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#FF0000")
            if cuentabarcos(self.espacio_player)==0:
                print("LOSER")
                
        actualiza_player()
        def disparo_enemy():
            a=randint(0,9)
            b=randint(0,9)
            if self.espacio_player[b][a]!=1 and self.espacio_player[b][a]!=3:
                self.espacio_player[b][a]+=1
                actualiza_player()
            else:
                disparo_enemy()

        def actualiza_enemy():
            for f in range(len(self.espacio_enemy)):
                for c in range(len(self.espacio_enemy[0])):
                    if self.espacio_enemy[f][c]==0:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")
                    if self.espacio_enemy[f][c]==2:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")
                    if self.espacio_enemy[f][c]==1:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#555555")
                    if self.espacio_enemy[f][c]==3:
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#FF0000")
            if cuentabarcos(self.espacio_enemy)==0:
                print("WINER")
                
            disparo_enemy()
        actualiza_enemy()
        """
        def Disparo(e):
            if self.espacio_enemy[b][a]!=1 and self.espacio_enemy[b][a]!=3:
                self.espacio_enemy[b][a]+=1
                actualiza_enemy()
        Click=Thread(target=self.canvas_enemi.bind("<Button-1>",Disparo))
        Click.start()
        """
    def juegoterminado(self,ganar):
        if ganar==True:
            ganar
        self.root.destroy()
        import ShipStack       
def cuentabarcos(pant):
    cant=0
    for filas in pant:
        for lugar in filas:
            if lugar==2:
                cant+=1
    return cant
def generabarcos():
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
    cant=randint(0,20)
    for i in range(cant+1):
        f=randint(0,9)
        c=randint(0,9)
        pant[f][c]=2
    return pant
