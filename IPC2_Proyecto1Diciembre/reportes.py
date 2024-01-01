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
from TDA import *
from exportaciones import *

class Reportes4: 

    def __init__(self): 
        self.mp =tk.Tk()
        self.mp.title('IPC Music')
        self.mp.geometry('647x300')
        self.mp['bg']='#170000'
        
        lab = Label(self.mp, text ="Reportes",font=("Courier New", 20),background='#170000',foreground='#8f3d38') 
        
        lab.grid(row=1, column=1, columnspan=5,rowspan=1 ,padx=2, pady=5)
        #        self.botonPlaylist.grid(row=5, column=6, columnspan=1,rowspan=1 ,padx=2, pady=5)
        
        Repo1 = tk.Button(self.mp,text = "Exportar HTML",background = "#56070c",foreground = "#ffffff",height = 2, width = 25,font=("Courier New", 10))
        Repo1.bind("<Button>",lambda e:HTMLRe() ) 
        Repo1.grid(row=3, column=1, columnspan=1,rowspan=1 ,padx=2, pady=5)
        
        Repo2 = tk.Button(self.mp,text = "Exportar XML",background = "#56070c",foreground = "#ffffff",height = 2, width = 25,font=("Courier New", 10))
        Repo2.bind("<Button>", lambda e:XMLRE) 
        Repo2.grid(row=3, column=3, columnspan=1,rowspan=1 ,padx=2, pady=5)
        
        Repo3 = tk.Button(self.mp,text = "Reporte Graphviz",background = "#56070c",foreground = "#ffffff",height = 2, width = 25,font=("Courier New", 10))
        Repo3.bind("<Button>", lambda e:Gra) 
        Repo3.grid(row=3, column=5, columnspan=1,rowspan=1 ,padx=2, pady=5)
        
        Regresar = tk.Button(self.mp,text = "Regresar",background = "#56070c",foreground = "#ffffff",height = 2, width = 25,font=("Courier New", 10))
        Regresar.bind("<Button>", lambda e: salir()) 
        Regresar.grid(row=4, column=3, columnspan=1,rowspan=1 ,padx=2, pady=5)
        
        """cargarAchivos.bind("<Button>", lambda e: cargaArc())
        listaReproduccion.bind("<Button>", lambda e: reproMusica())
        
        """
        def salir():
            
            self.mp.destroy()
            repro.ReproductoMusica()
            
        def HTMLRe():
            exportarHTML(blb)
            
        def XMLRE():
            exportarXML(playlists)
            
        def Gra(): 
            write_graphviz(blb)
            
        
            

 
        self.mp.mainloop()


