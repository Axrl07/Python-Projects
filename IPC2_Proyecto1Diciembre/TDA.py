import time
import xml.etree.ElementTree as ET
import random

class Cancion:
    def __init__(self,nombre,artista,album,imagen,ruta,vecesReproducida=0):
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.imagen = imagen
        self.ruta = ruta
        self.contador = 0

class Playlist:
    def __init__(self, nombre=None, EDD_canciones=None):
        self.nombre = nombre
        self.listadoCanciones = EDD_canciones

class Album:
    def __init__(self, nombre=None, nombreArtista=None, imagenAlbum=None, EDD_canciones=None):
        self.nombre = nombre
        self.imagen = imagenAlbum
        self.listadoCanciones = EDD_canciones
        self.nombreArtista = nombreArtista

class Artista:
    def __init__(self, nombre=None, EDD_albums=None):
        self.nombre = nombre
        self.listadoAlbums = EDD_albums

# nodo de la lista doblemente enlazada circular
class Nodo:
    def __init__(self, nombre,artista,album,imagen,ruta, vecesReproducida=0):
        self.dato = Cancion(nombre,artista,album,imagen,ruta,vecesReproducida)
        self.siguiente = None
        self.anterior = None
        self.identificador = None
        
class NodoPlaylist:
    def __init__(self, nombre, listadoCanciones):
        self.dato = Playlist(nombre, listadoCanciones)
        self.siguiente = None
        self.anterior = None
        self.identificador = None
        
# creamos la lista doblemente enlazada circular
class ListaCircularDoblementeEnlazada:
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.primero is None

    def agregar_al_final(self, nombre,artista,album,imagen,ruta, contador=0):
        nuevo_nodo = Nodo(nombre,artista,album,imagen,ruta, contador)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio += 1
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
            self.tamanio +=1

    def imprimir_lista(self):
        if self.esta_vacia():
            print("La lista está vacía")
        else:
            actual = self.primero
            while True:
                print(f"{actual.dato.nombre} del album: {actual.dato.artista}")
                # print(actual.dato.artista)
                # print(actual.dato.album)
                # print(actual.dato.imagen)
                # print(actual.dato.ruta)
                # print(f"veces reproducida: {actual.dato.contador}")
                # simulando que se reproduce la canción
                # actual.dato.contador+=1
                print(" - "*30)
                actual = actual.siguiente
                # time.sleep(0.75)
                if actual == self.primero:
                    break
                
    def remover_nodo(self, nombre):
        actual = self.primero
        # comparamos el nombre del data dentro del nodo con el nombre ingresado y recorremos la lista
        while actual and actual.dato.nombre != nombre:
            # almacenamos el nodo siguiente (hasta que lleguemos al de interes)
            actual = actual.siguiente
            if actual == self.primero:
                break
        if actual:
            #actualizamos puntero siguiente del nodo anterior
            actual.anterior.siguiente = actual.siguiente
            #actualizamos puntero anterior del nodo posterior
            actual.siguiente.anterior = actual.anterior
            # si el nodo es el primero o el último, actualizamos el head o tail
            if actual == self.primero:
                self.primero = actual.siguiente
            if actual == self.ultimo:
                self.ultimo = actual.anterior
    
    def simulacionReproduccion(self):
        apuntador = self.primero
        condicion = True
        while condicion:
            print(f"Cancion: {apuntador.dato.nombre} del artista: {apuntador.dato.artista}")
            x = input("Presione A para atrasar, D para adelantar y S para detener")
            if x =="d":
                apuntador = apuntador.siguiente
            elif x =="a":
                apuntador = apuntador.anterior
            elif x == "s":
                condicion = False
            else:
                print("Escoja bien >:v")    
            print(" - "*40)   

    def busca_albumn(self, album):
        apuntador = self.primero                 
        while True:
            if  album == apuntador.dato.album:
                return apuntador
            else: 
                apuntador = apuntador.siguiente
            if apuntador == self.ultimo:
                break
    
    def revolver(self):
        apuntador = self.primero
        while True:
            # time.sleep(0.75)
            x = random.randrange(1,self.tamanio,1)
            for i in range(x):
                apuntador = apuntador.siguiente
            print(f"Cancion {apuntador.dato.nombre}")
    
    def obtenerNodo(self, nombre):
        nodo_actual = self.primero
        nodo_None = False
        # comparamos el nombre del data dentro del nodo con la nombre y recorremos la lista
        while nodo_actual and nodo_actual.dato.nombre != nombre:
            # almacenamos el nodo siguiente (hasta que lleguemos al de interes)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                nodo_None = True
                break
        if nodo_None:
            return None
        else:
            return nodo_actual
    
    def linkearIndices(self):
        nodo_actual = self.primero
        contador = 0
        # comparamos el nombre del data dentro del nodo con la nombre y recorremos la lista
        while nodo_actual:
            # almacenamos el nodo siguiente (hasta que lleguemos al de interes)
            nodo_actual.identificador = contador
            nodo_actual = nodo_actual.siguiente
            contador += 1
            if nodo_actual == self.primero:
                break
        
    def obtenerNodoIndex(self, index):
        nodo_actual = self.primero
        nodo_None = False
        # comparamos el identificador del nodo con el index brindado
        while nodo_actual and nodo_actual.identificador != index:
            # almacenamos el nodo siguiente (hasta que lleguemos al de interes)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                nodo_None = True
                break
        if nodo_None:
            return None
        else:
            return nodo_actual  
    
    def copiarLista(self):
        # Crear una copia independiente de la lista actual
        copiaListaActual = ListaCircularDoblementeEnlazada()
        # copiando datos de la lista actual
        apuntadorCopia = self.primero
        print(apuntadorCopia.nombre)
        while True:
            datos = apuntadorCopia.dato
            copiaListaActual.agregar_al_final(datos.nombre, datos.artista, datos.album, datos.imagen, datos.ruta)
            apuntadorCopia = apuntadorCopia.siguiente
            if apuntadorCopia == self.primero:
                break
        return copiaListaActual
            
    def revolverPlaylist(self):
        # Crear una copia independiente de la lista actual
        copiaListaActual = ListaCircularDoblementeEnlazada()
        # copiando datos de la lista actual
        apuntadorCopia = self.primero
        while True:
            datos = apuntadorCopia.dato
            copiaListaActual.agregar_al_final(datos.nombre, datos.artista, datos.album, datos.imagen, datos.ruta)
            apuntadorCopia = apuntadorCopia.siguiente
            if apuntadorCopia == self.primero:
                break
        
        # trabajando modo aleatroio
        apuntador = self.primero
        ListaResultado = ListaCircularDoblementeEnlazada()
        
        # metodo que devuelve la lista doblemente enlazada circular con los datos aleatorios
        while True:
            y = random.randrange(1, copiaListaActual.tamanio, 1)
            x = 0
            while x < y: 
                apuntador = apuntador.siguiente
                x += 1
            datos = apuntador.dato
            if ListaResultado.obtenerNodo(datos.nombre) is None:
                ListaResultado.agregar_al_final(datos.nombre, datos.artista, datos.album, datos.imagen, datos.ruta)
                copiaListaActual.remover_nodo(apuntador.dato.nombre)
            if ListaResultado.tamanio == self.tamanio:
                break
        return ListaResultado
    
    ###################### metodo para crear playlist ############################
    def agregar_al_final_playlist(self, nombre, EDD_canciones):
        nuevo_nodo = NodoPlaylist(nombre, EDD_canciones)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio += 1
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
            self.tamanio +=1
    
    def imprimir_playlist(self):
        if self.esta_vacia():
            print("La lista está vacía")
        else:
            actual = self.primero
            while True:
                print(f"{actual.dato.nombre} con: {actual.dato.listadoCanciones}")
                listadoCanciones = actual.dato.listadoCanciones
                listadoCanciones.linkearIndices()
                for i in range(listadoCanciones.tamanio):
                    print(f"\t{listadoCanciones.obtenerNodoIndex(i).dato.nombre} del artista: {listadoCanciones.obtenerNodoIndex(i).dato.artista}")
                print(" - "*30)
                actual = actual.siguiente
                # time.sleep(0.75)
                if actual == self.primero:
                    break
    
    ################Metodo Filtar por Artista#####################
    def filter_by_Artist(self, artista):
        str(artista)
        apuntador = self.primero
        listaResultado = ListaCircularDoblementeEnlazada()
        while True:
            if apuntador == self.ultimo:
                if apuntador.dato.artista.lower() == artista.lower():
                    listaResultado.agregar_al_final(apuntador.dato.nombre,apuntador.dato.artista,apuntador.dato.album,apuntador.dato.imagen,apuntador.dato.ruta)
                    break
                else:
                    break
            else:
                if apuntador.dato.artista.lower() == artista.lower():
                    listaResultado.agregar_al_final(apuntador.dato.nombre,apuntador.dato.artista,apuntador.dato.album,apuntador.dato.imagen,apuntador.dato.ruta)
            apuntador = apuntador.siguiente
        return listaResultado    
    
    ################Metodo Filtar por Album#####################
    def filter_by_album(self,album):
        str(album)
        apuntador = self.primero
        listaResultado = ListaCircularDoblementeEnlazada()
        while True:
            if apuntador == self.ultimo:
                if apuntador.dato.album.lower() == album.lower():
                    listaResultado.agregar_al_final(apuntador.dato.nombre,apuntador.dato.artista,apuntador.dato.album,apuntador.dato.imagen,apuntador.dato.ruta)
                    break
                else:
                    break
            else:
                if apuntador.dato.album.lower() == album.lower():
                    listaResultado.agregar_al_final(apuntador.dato.nombre,apuntador.dato.artista,apuntador.dato.album,apuntador.dato.imagen,apuntador.dato.ruta)
            apuntador = apuntador.siguiente
        return listaResultado    

# nodo de la lista doblemente enlazada
class Nodo2:
    def __init__(self, data, prevPointer = None, nextPointer = None):
        self.data = data
        self.prevPointer = prevPointer
        self.nextPointer = nextPointer
        self.identifier = None
        
# creamos la lista doblemente enlazada
class ListaDoblementeEnlazada:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanio = 0
    
    def linkearIndices(self):
        nodo_actual = self.head
        contador = 0
        # comparamos el nombre del data dentro del nodo con la nombre y recorremos la lista
        while nodo_actual:
            # almacenamos el nodo siguiente (hasta que lleguemos al de interes)
            nodo_actual.identifier = contador
            nodo_actual = nodo_actual.nextPointer
            contador += 1
            if nodo_actual is None:
                break
    
    def insertarNodo(self, data):
        # si no hay nodos, se crea el primero
        if self.head is None:
            nodo_insertado = Nodo2(data)
            self.head = nodo_insertado
            self.tail = nodo_insertado
            self.tamanio += 1
        else:
            # Si la posición es -1, se inserta al final
            nodo_insertado = Nodo2(data, prevPointer=self.tail, nextPointer=None)
            self.tail.nextPointer = nodo_insertado
            self.tail = nodo_insertado
            self.tamanio += 1
    
    def removerNodo(self, llave):
        nodo_actual = self.head
        # comparamos el nombre del data dentro del nodo con la llave y recorremos la lista
        while nodo_actual and nodo_actual.data.nombre != llave:
            # almacenamos el nodo siguiente (hasta que lleguemos al de interes)
            nodo_actual = nodo_actual.nextPointer
        if nodo_actual and nodo_actual == self.head:
            # si el nodo es el primero, actualizamos el head
            nodo_actual.nextPointer.prevPointer = None
            self.head = nodo_actual.nextPointer
        elif nodo_actual and nodo_actual == self.tail:
            # si el nodo es el último, actualizamos el tail
            nodo_actual.prevPointer.nextPointer = None
            self.tail = nodo_actual.prevPointer
        else:
            # si el nodo está ente dos nodos
            # primero actualizamos puntero siguiente del nodo anterior al siguiente dle actual
            nodo_actual.prevPointer.nextPointer = nodo_actual.nextPointer
            # y por último actualizamos puntero anterior del nodo posterior al anterior del actual
            nodo_actual.nextPointer.prevPointer = nodo_actual.prevPointer
        self.tamanio += 1
    
    def obtenerNodo(self, llave):
        nodo_iterador = self.head
        while nodo_iterador and nodo_iterador.data.nombre != llave:
            nodo_iterador = nodo_iterador.nextPointer
        if nodo_iterador is None:
            return nodo_iterador
        else:
            return nodo_iterador.data
    
    def imprimir(self):
        if not self.head:
            return print("La lista está vacía")
        nodo_iterador = self.head
        while True:
            print(nodo_iterador.data.nombre)
            nodo_iterador = nodo_iterador.nextPointer
            if nodo_iterador is None:
                break

class prueba:
    
    def __init__(self):
        self.nombreAudio=""
    
    def leer_xml(self,ruta):
        
        tree = ET.parse(ruta)
        root = tree.getroot()
        
        for cancion in root.findall("cancion"):
            a = cancion.get("nombre")
            b = cancion.find("artista").text
            c = cancion.find("album").text
            d = cancion.find("imagen").text
            e = cancion.find("ruta").text
            blb.agregar_al_final(a,b,c,d,e)
        return blb
    
    def leer_xmlPlaylist(self,ruta):
        
        tree = ET.parse(ruta)
        root = tree.getroot()
        
        for playlist in root.findall("ListaReproduccion"):
            nombreLista = playlist.get("nombre")
            listadoCanciones = ListaCircularDoblementeEnlazada()
            for cancion in playlist.findall("Cancion"):
                nombre = cancion.get("nombre")
                artista = cancion.find("Artista").text
                album = cancion.find("Album").text
                imagen = cancion.find("Imagen").text
                ruta = cancion.find("Ruta").text
                contador = cancion.find("VecesReproducida").text
                listadoCanciones.agregar_al_final(nombre,artista,album,imagen,ruta, contador)
            playlists.agregar_al_final_playlist(nombreLista, listadoCanciones)
        return playlists
    
    # def CrearBase(self, listadoCanciones):
    #     print("Creando base de datos")
    #     listadoCanciones.linkearIndices()
    #     #for i in range(listadoCanciones.tamanio):
            
        
        
        
# canciones
blb = ListaCircularDoblementeEnlazada()
# playlists
playlists = ListaCircularDoblementeEnlazada()
# artistas
artistas = ListaDoblementeEnlazada()
# albums
albums = ListaDoblementeEnlazada()

#prueba().leer_xmlPlaylist("exportacionXML.xml")
# playlists.imprimir_playlist()
"""
# Ejemplo de uso

lista = leer_xml("Pruebas/entrada.xml")
#esta es una prueba



print("Lista circular doblemente enlazada:")
lista.imprimir_lista()
print("tamaño de la lista: "+str(lista.tamanio))
x = lista.busca_albumn("Uptown Special")
print(f"Cancion {x.dato.nombre} del artista {x.dato.artista} del album {x.dato.album}")

lista.revolver()
"""

'''x= prueba().leer_xml("entrada.xml")
x.imprimir_lista()
y = x.filter_by_Artist("Adele")
print("="*60)
print("_________Imprimir filtro de artista Adele en este caso_____")
y.imprimir_lista()
print("="*60)
print("_________Imprimir filtro de album Hotel California en este caso_____")
z = x.filter_by_album("Hotel California")
z.imprimir_lista()'''