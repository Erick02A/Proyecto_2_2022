from tkinter import *           #importar todo de tkinter
import tkinter as tk            #llamar a la libreria como tk
import pygame                   #pygame, por el momento para musica
from threading import Thread    #hilos 
import threading                #hilos
import os   
import time 
from random import *
from tkinter import messagebox


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
    def __init__(self,root,forma,barcos,tablero,nombre):
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
        self.abrir_juego.add_command(label="Guardar Partida",command=lambda:Guardar())
        self.abrir_juego.add_separator()
        self.segundos=0
        self.min=0
        self.mar_seg=Label(self.canvas_info,text="Tiempo. "+str(self.min)+":"+str(self.segundos),width=9,height=2,fg="black",bg="#b4b0f7")
        self.mar_seg.place(x=0,y=0)
        self.espacio_enemy=generabarcos()
        self.espacio_player=self.tablero
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
                self.pasa=True
                actualiza_player()
            elif self.espacio_player[b][a]==2:
                self.espacio_player[b][a]+=1
                self.pasa=False
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
                        self.fondo=self.canvas_enemi.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00AAFF")
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
                if self.espacio_enemy[b][a]==0:
                    self.espacio_enemy[b][a]+=1
                    self.pasa=False
                    actualiza=Thread(targer= actualiza_enemy())
                    actualiza.start()
                if self.espacio_enemy[b][a]==2:
                    self.espacio_enemy[b][a]+=1
                    #pygame.mixer.init() 
                    #pygame.mixer.music.load("boom.wav")
                    #pygame.mixer.music.play(loops=0)
                    actualiza=Thread(targer= actualiza_enemy())
                    actualiza.start()
                else:
                    messagebox.showinfo("Error","Ya disparaste en esta casilla")
            else:
                messagebox.showinfo("Error","No es tu turno")

        Click=Thread(target=self.canvas_enemi.bind("<Button-1>",Disparo))
        Click.start()
        def Guardar():
            l=1
#############################################################################################################
    def pantalla_gameB(self):
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
            for f in range(len(self.espacio_player)):
                for c in range(len(self.espacio_player[0])):
                    if self.espacio_player[f][c]==0:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#00FFFF")
                    if self.espacio_player[f][c]==2:
                        self.fondo=self.canvas_player.create_rectangle(60*c,60+(60*f),60+(60*c),60*f,fill="#0000FF")
        actualiza_tablero()

        def Coloca(e):
            """
            Selecciona la casilla escogida por el usuario para x motivo
            """
            if self.pasa==True:
                counter=60
                def creaA(e):
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
                        self.espacio_player[b][a]+=2
                        self.contador+=1
                        actualiza_tablero()
                else:
                    messagebox.showinfo("Error","Alcansate tu limite de barcos")
        Click=Thread(target=self.canvas_player.bind("<Button-1>",Coloca))
        Click.start()
        def seguirJuego(forma):
            self.root.destroy()
            pantalla_juego=Tk()
            pantalla_juego.title("SHIPSTACK")
            pantalla_juego.config(cursor="pirate")
            pantalla_juego.minsize(1300,600)#
            pantalla_juego.resizable(width=NO,height=NO)
            partida=game(pantalla_juego,forma,0,self.espacio_player,self.player_name)
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
            def abrir_txt():#tiene como argumentos el nombre y puntaje del jugador que finalizo partida 
                archivo= open("puntajes.txt","r") 
                nombres = archivo.readlines()#guarda los nombres y puntajes en una variable
                archivo.close() 
                comparador(nombres,"",0)#llama a la funcion que compara el puntaje con los del top 7 
    
            def comparador(lista, res ,i):
                if i == 10: #contador que verifica que se revise hasta el 7 lugar
                    return actualizar(res) 
                divisor = lista[0].split(";")#separa el nombre del puntaje y los guarda en una lista
                Punt = divisor[1].split(":")#obtiene el puntaje de la lista y lo convierte en entero
                actualPunt=(int(Punt[0])*100)+int(Punt[1])
                if actualPunt > (self.min*100+self.segundos): #compara si el puntaje obtenido es mayor a uno del top 7          
                    res += self.player_name + ";" + str(self.min)+":"+str(self.segundos)+ "\n"#guarda el nombre y puntaje del jugador en el string de resultado           
                    #usando el contador +1 se obtiene la posición que consiguió y se muestra en un label junto con el puntaje
                    messagebox.showinfo("Felicidades","Obtuviste la pocicion "+str(i+1)+"\n"+
                    "Con un tiempo de "+str(self.min)+":"+str(self.segundos))
                    self.segundos=61
                    self.min=2000
                    return comparador(lista,res,i+1)#cambia el valor del puntaje a 0 para no reemplazar los demas puntajes menores
                comparador(lista[1:],res+lista[0],i+1)#guarda los datos del top 7 cuando el puntaje del jugador no es superior a alguno de estos

            #funcion que obtiene la variable con los datos del nuevo top 7 y actualiza el archivo de texto con estos    
            def actualizar(nuevos):
                archivo = open("puntajes.txt","w") 
                archivo.write(nuevos) 
                archivo.close()
            abrir_txt()
        elif ganar==False:
            messagebox.showinfo("Manco","Game Over")
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
    for i in range(10):
        a=randint(0,9)
        b=randint(0,9)
        if pant[a][b]!=2:
            pant[a][b]=2
    return pant
