"""● Cargar biblioteca de canciones a través de un archivo XML
● Crear listas de reproducción seleccionando los datos de la biblioteca (ya sea por
canciones o por artistas) y reproducirlas utilizando estructuras de datos lineales.
● Mostrar un reporte de las canciones y artistas más reproducidos en HTML
● Mostrar un reporte de la biblioteca a través de la herramienta Graphviz"""

import tkinter as tk 
from tkinter import *
from tkinter.ttk import *

import cargarArchivo as carga
import reproductoM  as repro

class menuPrincipal: 

    def __init__(self): 
        self.mp =tk.Tk()
        self.mp.title('IPC Music')
        self.mp.geometry('670x300')
        self.mp['bg']='#170000'
        
        lab = Label(self.mp, text ="Proyecto 1",font=("Courier New", 20),background='#170000',foreground='#8f3d38') 
        
        lab.pack(side = TOP, pady = 5)
        
        cargarAchivos = tk.Button(self.mp,text = "CARGAR ARCHIVO XML",background = "#56070c",foreground = "#ffffff",height = 2, width = 40,font=("Courier New", 10))
        cargarAchivos.bind("<Button>") 
        cargarAchivos.pack(pady = 10)
        
        listaReproduccion = tk.Button(self.mp,text = "LISTAS DE REPRODUCCION",background = "#56070c",foreground = "#ffffff",height = 2, width = 40,font=("Courier New", 10))
        listaReproduccion.bind("<Button>") 
        listaReproduccion.pack(pady = 10)
        

        cargarAchivos.bind("<Button>", lambda e: cargaArc())
        listaReproduccion.bind("<Button>", lambda e: reproMusica())
        
        
        def cargaArc():
            
            self.mp.destroy()
            carga.ruta()
            
        def reproMusica():
            
            self.mp.destroy()
            repro.ReproductoMusica()

 
        self.mp.mainloop()


