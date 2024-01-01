from Tienda.codigo.funciones import *
import time

# clase padre (información base de los objetos)
class Prop:
    def __init__(self, nombre):
        self.id = generadorId()
        self.nombre = nombre

# clases hijas (información especifica de productos, clientes y facturas)
class Producto(Prop):
    def __init__(self, nombre, descripcion,precio,stock):
        super().__init__(nombre)
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

class Cliente(Prop):
    def __init__(self, nombre, direccion,nit, telefono):
        super().__init__(nombre)
        self.direccion = direccion
        self.nit = nit
        self.telefono = telefono
        
class Factura(Prop):
    def __init__(self, nombre, listadoCompras, subToal, total):
        super().__init__(nombre)
        segundos_desde_epoch = time.time()
        hora_actual = time.ctime(segundos_desde_epoch)
        self.fecha = hora_actual
        self.listadoCompras = listadoCompras
        self.subToal = subToal
        self.total = total