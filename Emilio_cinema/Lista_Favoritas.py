from Registrar_Usuario import ListaUsuarios
lista = ListaUsuarios()
Favoritas = []

class Lista():
    def __init__(self, nombre):
        self.nombre = nombre

class PelisFav():
    def AñadirFav(self, nombre):
        lista = Lista(nombre)
        