# nodo de la lista doblemente enlazada circular
import random


class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        self.anterior = None
        self.identificador = None
        
# creamos la lista doblemente enlazada circular
class ListaCircularDoblementeEnlazada:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

    def vacia(self) -> bool:
        if self.cabeza == None:
            return True
        else:
            return False
    
    def agregar(self, nueva_data) -> None:
        nuevo_nodo = Nodo(nueva_data)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.longitud += 1
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
            self.cola.siguiente = self.cabeza
            self.cabeza.anterior = self.cola
            self.longitud +=1

    def imprimir(self) -> None:
        if self.esta_vacia():
            print("La lista está vacía")
        else:
            nodo_actual = self.cabeza
            while True:
                # lo que queremos que nos imprima
                print(f"{nodo_actual.data}")
                nodo_actual = nodo_actual.siguiente
                if nodo_actual == self.cabeza:
                    break
    
    def linkearIndices(self):
        nodo_actual = self.cabeza
        contador = 0
        # comparamos el nombre del data dentro del nodo con la nombre y recorremos la lista
        while nodo_actual:
            # almacenamos el nodo siguiente (hasta que lleguemos al de interes)
            nodo_actual.identificador = contador
            nodo_actual = nodo_actual.siguiente
            contador += 1
            if nodo_actual == self.cabeza:
                break
    
    def obtenerNodo_index(self, index):
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
    
    # metodos que necesitan una llave
    def remover(self, llave) -> None:
        nodo_actual = self.cabeza
        # comparamos el nombre del data dentro del nodo con el nombre ingresado y recorremos la lista
        while nodo_actual and nodo_actual.data.llave != llave:
            # almacenamos el nodo siguiente (hasta que lleguemos al de interes)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.cabeza:
                break
        if nodo_actual:
            #actualizamos puntero siguiente del nodo anterior
            nodo_actual.anterior.siguiente = nodo_actual.siguiente
            #actualizamos puntero anterior del nodo posterior
            nodo_actual.siguiente.anterior = nodo_actual.anterior
            # si el nodo es el primero o el último, actualizamos el head o tail
            if nodo_actual == self.cabeza:
                self.cabeza = nodo_actual.siguiente
            if nodo_actual == self.cola:
                self.cola = nodo_actual.anterior   
    
    def obtenerNodo_llave(self, llave):
        nodo_actual = self.cabeza
        nodo_None = False
        # comparamos el nombre del data dentro del nodo con la nombre y recorremos la lista
        while nodo_actual and nodo_actual.data.llave != llave:
            # almacenamos el nodo siguiente (hasta que lleguemos al de interes)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.cabeza:
                nodo_None = True
                break
        if nodo_None:
            return None
        else:
            return nodo_actual
    
    # metodos que se deben adecuar para que funcionen
    # def copiarLista(self):
    #     # Crear una copia independiente de la lista actual
    #     copiaListaActual = ListaCircularDoblementeEnlazada()
        
    #     # copiando datos de la lista actual
    #     apuntadorCopia = self.cabeza
    #     print(apuntadorCopia.nombre)
    #     while True:
    #         datos = apuntadorCopia.data
    #         copiaListaActual.agregar_al_final(datos.nombre, datos.artista, datos.album, datos.imagen, datos.ruta)
    #         apuntadorCopia = apuntadorCopia.siguiente
    #         if apuntadorCopia == self.cabeza:
    #             break
    #     return copiaListaActual
            
    # def revolverLista(self):
    #     Crear una copia independiente de la lista actual
    #     copiaListaActual = ListaCircularDoblementeEnlazada()
    #     copiando datos de la lista actual
    #     apuntadorCopia = self.cabeza
    #     while True:
    #         datos = apuntadorCopia.dato
    #         copiaListaActual.agregar_al_final(datos.nombre, datos.artista, datos.album, datos.imagen, datos.ruta)
    #         apuntadorCopia = apuntadorCopia.siguiente
    #         if apuntadorCopia == self.cabeza:
    #             break
        
    #     trabajando modo aleatroio
    #     apuntador = self.cabeza
    #     ListaResultado = ListaCircularDoblementeEnlazada()
        
    #     metodo que devuelve la lista doblemente enlazada circular con los datos aleatorios
    #     while True:
    #         y = random.randrange(1, copiaListaActual.tamanio, 1)
    #         x = 0
    #         while x < y: 
    #             apuntador = apuntador.siguiente
    #             x += 1
    #         datos = apuntador.dato
    #         if ListaResultado.obtenerNodo(datos.nombre) is None:
    #             ListaResultado.agregar_al_final(datos.nombre, datos.artista, datos.album, datos.imagen, datos.ruta)
    #             copiaListaActual.remover_nodo(apuntador.dato.nombre)
    #         if ListaResultado.tamanio == self.tamanio:
    #             break
    #     return ListaResultado

        
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
