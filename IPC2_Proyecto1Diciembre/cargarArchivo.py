import tkinter as tk 
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from TDA import *
# from TDA2 import *

import menu as menuPrin


class ruta: 

      #arreglo de datos

    def __init__(self): 

        self.CA =tk.Tk()
        self.CA.title('Practica_1')
        self.CA.geometry('691x500')
        self.CA['bg']='#170000'

        label = Label(self.CA, text="CARGAR ARCHIVO",font=("Times", 20),background='#170000',foreground='#ffffff') 
        urlDatos =Label(self.CA,background='#170000',foreground='#ffffff')
        
        def browseFiles(): 
            filename = filedialog.askopenfilename(initialdir = "/", 
                                                title = "Select a File", 
                                                filetypes = (("Text files", 
                                                                "*.xml*"), 
                                                            ("all files", 
                                                                "*.*"))) 
            urlDatos.configure(text=filename)
            
        btn = tk.Button(self.CA, text ="BUSCAR",command = browseFiles,background = "#56070c",foreground = "#ffffff",height = 2, width = 26,font=("Courier New", 10))

        #cargarAchivos = tk.Button(self.mp,text = "CARGAR ARCHIVO",background = "#c999af",foreground = "#ffffff",height = 2, width = 20,font=("Courier New", 10))
        btn2 = tk.Button(self.CA, text ="CARGA",background = "#56070c",foreground = "#ffffff",height = 2, width = 26,font=("Courier New", 10))

        btn3 = tk.Button(self.CA, text ="SALIR",background = "#56070c",foreground = "#ffffff",height = 2, width = 26,font=("Courier New", 10))
        
        
        btn2.bind("<Button>", lambda e: printVariable()  ) 
        btn3.bind("<Button>", lambda e: salir())
        
        
        label.grid(row=1, column=3, columnspan=5, padx=5, pady=5)
        urlDatos.grid(row=3, column=3, columnspan=5, padx=5, pady=5)
        btn.grid(row=5, column=1, columnspan=3, padx=5, pady=5) 
        btn2.grid(row=5, column=4, columnspan=3, padx=5, pady=5) 
        btn3.grid(row=5, column=7, columnspan=3, padx=5, pady=5) 
        
        def printVariable():
            
            print(urlDatos.cget("text"))
            prueba.leer_xml(self,urlDatos.cget("text"))


        # metodo salir
        def salir():
            self.CA.destroy()
            
            menuPrin.menuPrincipal()
            

        self.CA.mainloop()

 

