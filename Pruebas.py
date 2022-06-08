from tkinter import *           #importar todo de tkinter
import tkinter as tk            #llamar a la libreria como tk
import pygame                   #pygame, por el momento para musica
from threading import Thread    #hilos 
import threading                #hilos
import os    
from random import *

vidas=0

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
    def __init__(self,root):
        self.root=root
        self.main_canvas = tk.Canvas(root,width=1200,height=600, bg="green") #1600,800
        self.main_canvas.place(x=0,y=0)
        self.pantalla_game()
    def pantalla_game(self):
        self.canvas_enemi = Canvas(self.root,width=600,height=600,bg="red")
        self.canvas_enemi.place(x=0,y=0)
        self.canvas_player = Canvas(self.root,width=600,height=600,bg="blue")
        self.canvas_player.place(x=601,y=0)
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
        #self.fondo00=self.canvas_enemi.create_rectangle(0,60,60,0,fill="#5555FF")
        #self.fondo00=self.canvas_enemi.create_rectangle(60,120,100,60,fill="#5600FF")
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

        actualiza_enemy()
        def mostrar(e):
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
                print(self.espacio_enemy[b][a])
                actualiza_enemy()
        self.canvas_enemi.bind("<Button-1>",mostrar)

        

main_menu = Tk()
main_menu.title("SHIPSTACK")
main_menu.config(cursor="pirate")
main_menu.minsize(1200,600)#
main_menu.resizable(width=NO,height=NO)
pantalla_principal = game(main_menu) #se cambió la palabra ventana por pantalla, parece funcionar igual
main_menu.mainloop() #usado para tkinter