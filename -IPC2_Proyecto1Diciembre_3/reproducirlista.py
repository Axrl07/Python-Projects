import tkinter as tk 
from tkinter import *
from tkinter.ttk import *

from tkinter import filedialog

import menu as menuPrin
import BotonListaRepro as BLR
import reportes as Repo
import ListasdeReproduccion as ldr

from TDA import *


class ReproducLista: 

      #arreglo de datos
    

    def __init__(self,nodoListado): 
        self.playlist=nodoListado.dato.listadoCanciones
        self.titulo=nodoListado.dato.nombre
        self.CA =tk.Tk()
        self.CA.title('Practica_1')
        self.CA.geometry('1000x500')
       # self.CA.resizable(0, 0)
        self.CA['bg']='#170000'
        
        self.apuntador = self.playlist.primero
        
        
        
        
        self.frame = Frame(master=self.CA,width=800, height=400, relief="sunken")
        self.frame.grid(row=5, column=3, columnspan=3,rowspan=5, padx=2, pady=5)
        self.frame.propagate(False) 
        
        self.frame3 = Frame(master=self.CA,width=400, height=310, relief="sunken")
        self.frame3.grid(row=5, column=1, columnspan=3, rowspan=5, padx=2, pady=5)
        self.frame3.propagate(False) 
        
        self.frame2 = Frame(self.frame, width=200, height=200, relief="sunken")
        self.frame2.grid(row=7, column=3, columnspan=5, padx=2, pady=5)
        self.frame2.propagate(False)  # Mueve esto aquí para evitar que el frame se ajuste automáticamente

        self.v2 = Label(self.frame2, text=" ",font=("Perpetua", 14),foreground='#000000') 
        self.v2.grid(row=1, column=2, columnspan=5, padx=10, pady=5)
        #*****************Tabla de canciones*****************
        
        def mostrar_info_seleccionada(event):
            item = TablaCanciones.focus()  # Obtener el item seleccionado
            if item:
                # Obtener los valores de la fila seleccionada
                dataFila = TablaCanciones.item(item, 'values')
                # Puedes hacer lo que quieras con los valores, por ejemplo, imprimirlos
                print("Información de la fila seleccionada:", dataFila)
                objetoCancion = self.playlist.obtenerNodo(dataFila[0])
                print(objetoCancion.dato.artista)
                objetoCancion.dato.contador+=1
                self.nombreCancion.config(text=objetoCancion.dato.nombre) 
                self.nombreArtista.config(text=objetoCancion.dato.artista) 
                self.nombreAlbum.config(text=objetoCancion.dato.album)
                      
            
        columnas = ('Todas las canciones',)
        TablaCanciones=Treeview(self.frame3,columns=columnas,show='headings')
        
        for col in columnas:
            TablaCanciones.heading(col, text=col)
            TablaCanciones.column(col, width=200, anchor="center")  # Ajusta el ancho de las columnas según sea necesario
            
        apuntador = self.playlist.primero
        condi = self.playlist.primero

        while True:
            TablaCanciones.insert('', 'end', values=(apuntador.dato.nombre,))
            print(apuntador.dato.imagen)
            apuntador = apuntador.siguiente
            if apuntador==condi: 
                break
            
        TablaCanciones.bind('<ButtonRelease-1>', mostrar_info_seleccionada)
        
        TablaCanciones.grid(row=2, column=1, columnspan=2,rowspan=1 ,padx=2, pady=5)
        
        #*********************************************************
        
        
        #labels no modificar 
        self.cancion = Label(self.frame2, text="Canción:",font=("Perpetua", 14),foreground='#000000') 
        self.cancion.grid(row=2, column=2, columnspan=3, padx=10, pady=5)     
        self.Artista = Label(self.frame2, text="Artista:",font=("Perpetua", 14),foreground='#000000') 
        self.Artista.grid(row=3, column=2, columnspan=3, padx=10, pady=5)   
        self.Album = Label(self.frame2, text="Album:",font=("Perpetua", 14),foreground='#000000') 
        self.Album.grid(row=4, column=2, columnspan=3, padx=10, pady=5)
        #************************************
        
        
        #labels paea colocar las canciones, artistas y album
        self.nombreCancion = Label(self.frame2, text=self.apuntador.dato.nombre,font=("Perpetua", 14),foreground='#000000') 
        self.nombreCancion.grid(row=2, column=6, columnspan=5, padx=10, pady=5)   
          
        self.nombreArtista = Label(self.frame2, text=self.apuntador.dato.artista,font=("Perpetua", 14),foreground='#000000') 
        self.nombreArtista.grid(row=3, column=6, columnspan=5, padx=10, pady=5) 
          
        self.nombreAlbum = Label(self.frame2, text=self.apuntador.dato.album,font=("Perpetua", 14),foreground='#000000') 
        self.nombreAlbum.grid(row=4, column=6, columnspan=5, padx=10, pady=5)
        #************************************
        
        
        self.v = Label(self.frame2, text=" ",font=("Perpetua", 14),foreground='#000000') 
        self.v.grid(row=5, column=2, columnspan=5, padx=10, pady=5)
        
        
        
        #Boton de Busqueda
        
        self.buscarEntry = Entry(self.CA,font=("Times", 16),foreground="#cb7169")
        self.buscarEntry.grid(row=2, column=4, columnspan=1, padx=2, pady=5,ipadx=100)
        #print(self.buscarEntry.get)
        
        self.imagen = PhotoImage(file="Imagenes/im.png", master=self.CA)
        self.imagen_sub=self.imagen.subsample(19)
        self.botonBusqueda = tk.Button(self.CA, image=self.imagen_sub,command=self.BuscarCancion)
        self.botonBusqueda.grid(row=2, column=3, columnspan=1,rowspan=1 ,padx=2, pady=5)
        
        
        
        
        #**********************
        
        #imagen de usuario
        self.user = PhotoImage(file="Imagenes/user.png", master=self.CA)
        self.user_sub=self.user.subsample(6)
        self.labelima2 = Label(self.CA,image=self.user_sub)
        self.labelima2.grid(row=2, column=6, columnspan=1,rowspan=2 ,padx=2, pady=5)
        #**********************
        
        
        
        #para poner foto de la cancion
        self.imagenCancion = PhotoImage(file="Imagenes/auriculares.png", master=self.frame)
        self.labelima4 = Label(self.frame,image=self.imagenCancion)
        self.labelima4.grid(row=5, column=1, columnspan=1,rowspan=10 ,padx=2, pady=5)
        #*****************************
        
        #Boton Atras
        self.imagenatras = PhotoImage(file="Imagenes/atras.png", master=self.CA)
        self.imagenatras_sub=self.imagenatras.subsample(3)
        self.botonAtras = tk.Button(self.frame, image=self.imagenatras_sub,command=self.AccionRegresar)
        self.botonAtras.grid(row=10, column=3, columnspan=1,rowspan=1 ,padx=2, pady=5)
        #**********************
        
        #Boton Siguiente
        self.imagensiguiente = PhotoImage(file="Imagenes/siguiente.png", master=self.CA)
        self.imagensiguientes_sub=self.imagensiguiente.subsample(3)
        self.botonSiguientes = tk.Button(self.frame, image=self.imagensiguientes_sub,command=self.AccionAdelante)

        self.botonSiguientes.grid(row=10, column=5, columnspan=1,rowspan=1 ,padx=2, pady=5)
        #**********************
        
        #Boton Pausa
        self.imagenPausa = PhotoImage(file="Imagenes/pausa.png", master=self.CA)
        self.imagenPausa_sub=self.imagenPausa.subsample(3)
        self.botonPausa = tk.Button(self.frame, image=self.imagenPausa_sub)
        self.botonPausa.bind("<Button>") 
        self.botonPausa.grid(row=5, column=4, columnspan=1,rowspan=1 ,padx=2, pady=5)
        #**********************
        
        #Boton para Detener Todo
        self.imagenDetenerTodo = PhotoImage(file="Imagenes/detenerTodo.png", master=self.CA)
        self.imagenDetenerTodo_sub=self.imagenDetenerTodo.subsample(3)
        self.botonDetenerTodo = tk.Button(self.frame, image=self.imagenDetenerTodo_sub)
        self.botonDetenerTodo.bind("<Button>") 
        self.botonDetenerTodo.grid(row=5, column=5, columnspan=1,rowspan=1 ,padx=2, pady=5)
        #**********************
        
        #Boton Reproducir
        self.imagenReproducir = PhotoImage(file="Imagenes/reproducir.png", master=self.CA)
        self.imagenReproducir_sub=self.imagenReproducir.subsample(3)
        self.botonDetenerTodo = tk.Button(self.frame, image=self.imagenReproducir_sub)
        self.botonDetenerTodo.bind("<Button>") 
        self.botonDetenerTodo.grid(row=5, column=3, columnspan=1,rowspan=1 ,padx=2, pady=5)
        #**********************
        
        #Boton Salir
        self.imagenSalir = PhotoImage(file="Imagenes/cerrar.png", master=self.CA)
        self.imagenSalir_sub=self.imagenSalir.subsample(4)
        self.botonSalir = tk.Button(self.CA, image=self.imagenSalir_sub)
        self.botonSalir.bind("<Button>",lambda e: ejemplo()) 
        self.botonSalir.grid(row=1, column=6, columnspan=1,rowspan=1 ,padx=2, pady=5)
        #**********************


        self.label = Label(self.CA, text="IPC MUSIC",font=("Times", 20),background='#170000',foreground='#ffffff') 
        self.label.grid(row=1, column=2, columnspan=5, padx=10, pady=5)
        
        self.Archivo = Label(self.CA, text="Archivo",font=("Times", 20),background='#170000',foreground='#ffffff') 
        self.Archivo.grid(row=2, column=1, columnspan=1, padx=1, pady=5)
        
        # Crear caja de texto.
        self.archivoEntry = Entry(self.CA,font=("Times", 16),foreground="#cb7169")
        # Posicionarla en la ventana.
        self.archivoEntry.grid(row=2, column=2, columnspan=1, padx=2, pady=5,ipadx=5)


        
        
        
        def BotonListasR():
            
            self.CA.destroy()
            ldr.ListasdeReproduccion()
            #BLR.BotonListasReproduc()
            
        def Reportes():
            
            self.CA.destroy()
            Repo.Reportes4()
        
        def ejemplo():
            
            self.CA.destroy()
            menuPrin.menuPrincipal()
            
    def AccionAdelante(self):
        
        self.apuntador = self.apuntador.siguiente

        self.nombreCancion.config(text=self.apuntador.dato.nombre) 
        self.nombreArtista.config(text=self.apuntador.dato.artista) 
        self.nombreAlbum.config(text=self.apuntador.dato.album) 
        #print(self.apuntador.dato.Imagen)
        
    def AccionRegresar(self):
        
        self.apuntador = self.apuntador.anterior

        self.nombreCancion.config(text=self.apuntador.dato.nombre) 
        self.nombreArtista.config(text=self.apuntador.dato.artista) 
        self.nombreAlbum.config(text=self.apuntador.dato.album) 
        
    def BuscarCancion(self):

        k=self.playlist.obtenerNodo(str(self.buscarEntry.get()))
        print(k.dato.artista)
        k.dato.contador+=1
        self.nombreCancion.config(text=k.dato.nombre) 
        self.nombreArtista.config(text=k.dato.artista) 
        self.nombreAlbum.config(text=k.dato.album) 
        
        
    


        
        self.CA.mainloop()
        
        