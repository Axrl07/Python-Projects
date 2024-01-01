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
import menu as menuPrin

listadoAuxiliar=ListaCircularDoblementeEnlazada()

class BotonListasReproduc: 

    def __init__(self): 
        self.CA =tk.Tk()
        self.CA.title('Practica_1')
        self.CA.geometry('530x500')
        self.CA['bg']='#170000'
        
        print("si entra")

        lab = Label(self.CA, text ="Nombre de la lista de canciones: ",font=("Courier New", 13),background='#170000',foreground='#8f3d38') 
        
        lab.grid(row=2, column=3, columnspan=2,rowspan=2 ,padx=2, pady=5)
                
        self.archivoEntry = Entry(self.CA,font=("Times", 16),foreground="#cb7169")
        # Posicionarla en la ventana.
        self.archivoEntry.grid(row=4, column=3, columnspan=2, padx=2, pady=5,ipadx=5)
        print(self.archivoEntry.get())

        
         
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
                listadoAuxiliar.agregar_al_final(objetoCancion.dato.nombre,objetoCancion.dato.artista,objetoCancion.dato.album,objetoCancion.dato.imagen,objetoCancion.dato.ruta)
            #//////  aqui se debe e poner el mettodo para crear una nueva lista/////
                tablaParaPlayList.insert('', 'end', values=((objetoCancion.dato.nombre,)))
                
                
                
                
                
                



        columnas = ('Listado de canciones',)
        tablaCancionPrincipal= Treeview(self.CA,columns=columnas,show='headings')

        for col in columnas:
            tablaCancionPrincipal.heading(col, text=col)
            tablaCancionPrincipal.column(col, width=200, anchor="center")  # Ajusta el ancho de las columnas según sea necesario
            
        apuntador = blb.primero
        condi = blb.primero
        
        

        while True:
            tablaCancionPrincipal.insert('', 'end', values=(apuntador.dato.nombre,))
            print(apuntador.dato.imagen)
            apuntador = apuntador.siguiente
            if apuntador==condi: 
                break
        tablaCancionPrincipal.bind('<ButtonRelease-1>', mostrar_info_seleccionada)
        tablaCancionPrincipal.grid(row=2, column=1, columnspan=2,rowspan=6 ,padx=2, pady=5)
        #****************************************************************
        
        #*********************tabla para play list*********************
        columna = ('Canciones para la play list',)
        tablaParaPlayList= Treeview(self.CA,columns=columna,show='headings')

        for col in columna:
            tablaParaPlayList.heading(col, text=col)
            tablaParaPlayList.column(col, width=200, anchor="center")  # Ajusta el ancho de las columnas según sea necesario
            
        apuntador = blb.primero
        condi = blb.primero

        
        tablaParaPlayList.grid(row=6, column=3, columnspan=2,rowspan=2 ,padx=2, pady=5)
        #****************************************************************
        
        #Boton Salir
        self.imagenSalir = PhotoImage(file="Imagenes/cerrar.png", master=self.CA)
        self.imagenSalir_sub=self.imagenSalir.subsample(4)
        self.botonSalir = tk.Button(self.CA, image=self.imagenSalir_sub)
        self.botonSalir.bind("<Button>",lambda e: ejemplo()) 
        self.botonSalir.grid(row=1, column=5, columnspan=1,rowspan=1 ,padx=2, pady=5)
        #**********************
        
        #Boton crear lista

        self.crearlista = tk.Button(self.CA,text = "Crear lista",background = "#56070c",foreground = "#ffffff",height = 2, width = 20,font=("Courier New", 10),command=self.guardarLista)
        self.crearlista.bind("<Button>") 
        self.crearlista.grid(row=10, column=2, columnspan=1,rowspan=1 ,padx=2, pady=5)
        
    
        #**********************
        
        def ejemplo():
            
            self.CA.destroy()
            menuPrin.menuPrincipal()
            
    def guardarLista(self):
        nombre=self.archivoEntry.get()
        canciones=listadoAuxiliar
        playlists.agregar_al_final_playlist(nombre,canciones)
        
        playlists.imprimir_playlist()
        
        
        
 
        self.CA.mainloop()

