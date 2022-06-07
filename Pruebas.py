from tkinter import *           #importar todo de tkinter
import tkinter as tk            #llamar a la libreria como tk
import pygame                   #música
from threading import Thread    #hilos 
import threading                #hilos
import os    
from random import *

vidas=0




class game:
    def __init__(self,root):
        self.root=root
        self.main_canvas = tk.Canvas(root,width=1000,height=600, bg="green") #1500,800
        self.main_canvas.place(x=0,y=0)
        self.pantalla_game()
    def pantalla_game(self):
        self.canvas_enemi = Canvas(self.root,width=500,height=600,bg="red")
        self.canvas_enemi.place(x=0,y=0)
        self.canvas_player = Canvas(self.root,width=500,height=600,bg="blue")
        self.canvas_player.place(x=501,y=0)
        self.bottlist_enemy=[]
        self.bottlist_player=[]
        def verifica(boton,i,j):
            boton[i][j].config(bg="#FF0000") #color rojo
            print("funciona!!")
        for i in range(0,10):
            self.bottlist_enemy.append([])
                                
            for j in range(0,10):
                self.bottlist_enemy[i].append(Button(self.canvas_enemi,bg="#15E4E9",command= lambda:verifica(self.bottlist_enemy,i,j))) #color turquesa
                self.bottlist_enemy[i][j].place(relx=0.1*j,rely=0.1*i,relwidth=0.1,relheight=0.1)
                #self.bottlist_enemy[i][j].config()                       
        for i in range(0,10):
            self.bottlist_player.append([])
            
            for j in range(0,10):
                self.bottlist_player[i].append(Button(self.canvas_player,bg="#7553F1")) #color morado
                self.bottlist_player[i][j].place(relx=0.1*j,rely=0.1*i,relwidth=0.1,relheight=0.1)
                self.bottlist_player[i][j].config(command= lambda: verifica(self.bottlist_player,i,j))                       

        

        
"""
main_menu = Tk()
main_menu.title("SHIPSTACK")
main_menu.config(cursor="pirate")
main_menu.minsize(1000,600)#
main_menu.resizable(width=NO,height=NO)
pantalla_principal = game(main_menu) #se cambió la palabra ventana por pantalla, parece funcionar igual
main_menu.mainloop() #usado para tkinter
"""
