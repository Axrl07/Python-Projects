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
import BotonListaRepro as BLR
import reproducirlista as rpl
from BotonListaRepro import *


from TDA import *
import menu as menuPrin


objetoseleccionado=None
class ListasdeReproduccion: 

    def __init__(self): 
        self.CA =tk.Tk()
        self.CA.title('Practica_1')
        self.CA.geometry('470x350')
        self.CA['bg']='#170000'
        print("si entra")

        lab = Label(self.CA, text ="Listas de reproducción",font=("Courier New", 20),background='#170000',foreground='#8f3d38') 
        
        lab.grid(row=1, column=1, columnspan=5,rowspan=1 ,padx=2, pady=5)
        

        
         
        #*********************tabla principal*********************
        def mostrar_info_seleccionada(event):
            item = tablaCancionPrincipal.focus()  # Obtener el item seleccionado
            if item:
                # Obtener los valores de la fila seleccionada
                dataFila = tablaCancionPrincipal.item(item, 'values')
                # Puedes hacer lo que quieras con los valores, por ejemplo, imprimirlos
                print("Información de la fila seleccionada:", dataFila)
                objetoCancion = blb.obtenerNodo(dataFila[0])
                print(objetoCancion.dato.artista)
            #//////  aqui se debe e poner el mettodo para crear una nueva lista/////

        def seleccionarInformacionPlay(event):
            item = tablaCancionPrincipal.focus()  # Obtener el item seleccionado
            if item:
                # Obtener los valores de la fila seleccionada
                dataFila = tablaCancionPrincipal.item(item, 'values')
                # Puedes hacer lo que quieras con los valores, por ejemplo, imprimirlos
                print("Información de la fila seleccionada:", dataFila)
                objetoplay = playlists.obtenerNodo(dataFila[0])
                print(objetoplay.dato.nombre)
                global objetoseleccionado 
                objetoseleccionado=objetoplay
        
            
            #//////  aqui se debe e poner el mettodo para crear una nueva lista/////

        
        


        columnas = ('Listado de canciones',)
        tablaCancionPrincipal= Treeview(self.CA,columns=columnas,show='headings')

        for col in columnas:
            tablaCancionPrincipal.heading(col, text=col)
            tablaCancionPrincipal.column(col, width=450, anchor="center")  # Ajusta el ancho de las columnas según sea necesario
            
        apuntador = playlists.primero
        condi = playlists.primero
        
        
        

        while True:
            
            print(apuntador.dato.nombre)
            tablaCancionPrincipal.insert('', 'end', values=(apuntador.dato.nombre,))
   
            apuntador = apuntador.siguiente
            
            if apuntador==condi: 
                break
            
            
        tablaCancionPrincipal.bind('<ButtonRelease-1>', seleccionarInformacionPlay)
        tablaCancionPrincipal.grid(row=2, column=1, columnspan=6,rowspan=6 ,padx=2, pady=5)
        #****************************************************************

        #Boton Salir
        self.imagenSalir = PhotoImage(file="Imagenes/cerrar.png", master=self.CA)
        self.imagenSalir_sub=self.imagenSalir.subsample(4)
        self.botonSalir = tk.Button(self.CA, image=self.imagenSalir_sub)
        self.botonSalir.bind("<Button>",lambda e: ejemplo()) 
        self.botonSalir.grid(row=1, column=6, columnspan=1,rowspan=1 ,padx=2, pady=5)
        #**********************
        
        #Boton crear lista

        self.crearlista = tk.Button(self.CA,text = "Crear lista",background = "#56070c",foreground = "#ffffff",height = 2, width = 20,font=("Courier New", 10))
        self.crearlista.bind("<Button>",lambda e: BotonListasR()) 
        self.crearlista.grid(row=10, column=1, columnspan=3,rowspan=1 ,padx=2, pady=5)
        
    
        #**********************
        
        #Boton crear lista

        self.crearlista = tk.Button(self.CA,text = "Continuar",background = "#56070c",foreground = "#ffffff",height = 2, width = 20,font=("Courier New", 10))
        self.crearlista.bind("<Button>",lambda e:BotonReproduccionListas()) 
        self.crearlista.grid(row=10, column=5, columnspan=3,rowspan=1 ,padx=2, pady=5)
        
    
        #**********************
        
        def BotonListasR():
            
            self.CA.destroy()

            BLR.BotonListasReproduc()
            
        def BotonReproduccionListas():
            
            self.CA.destroy()

            rpl.ReproducLista(objetoseleccionado)
            
        
        def ejemplo():
            
            self.CA.destroy()
            menuPrin.menuPrincipal()
        
 
        self.CA.mainloop()