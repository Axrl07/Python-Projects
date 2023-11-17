from Listado_Pelis import ListadoPelis
Lista = []

class Datos:
    def __init__(self, nombre):
        self.nombre = nombre

class Favoritos:
    def AgregarFav(self, nombre):
        Lista.append(nombre)

    def Imprimir(self):
        for i in Lista:
            print(i)
