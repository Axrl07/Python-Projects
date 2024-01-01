from Tienda.codigo.funciones import *
import time

# clase padre (información base de los objetos)
class Prop:
    def __init__(self, nombre):
        self.id = generadorId()
        self.nombre = nombre
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }

# clases hijas (información especifica de productos, clientes y facturas)
class Producto(Prop):
    def __init__(self, nombre, descripcion,precio,stock):
        super().__init__(nombre)
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.contador = 0
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock,
            'contador': self.contador
        }

class Cliente(Prop):
    def __init__(self, nombre, correo, telefono, nit="CF"):
        super().__init__(nombre)
        self.nit = nit
        self.correo = correo
        self.telefono = telefono
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nit': self.nit,
            'correo': self.correo,
            'telefono': self.telefono
        }

class Factura(Prop):
    def _init_(self,Cliente, Producto, Cantidad, Precio ):
        super()._init_(Cliente)
        self.Producto=Producto
        self.Cantidad=Cantidad
        self.Precio=Precio
        
# class Factura(Prop):
#     def __init__(self, nit, nombre, listadoCompras, subTotal):
#         super().__init__(nombre)
#         self.nit = nit
#         segundos_desde_epoch = time.time()
#         hora_actual = time.ctime(segundos_desde_epoch)
#         self.fecha = hora_actual
#         self.listadoCompras = listadoCompras
#         self.subTotal = subTotal
#         self.impuesto = subTotal * 0.12
#         self.total = subTotal + self.impuesto
    
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'nombre': self.nombre,
#             'nit': self.nit,
#             'fecha': self.fecha,
#             'listadoCompras': self.listadoCompras,
#             'subTotal': self.subTotal,
#             'impuesto': self.impuesto,
#             'total': self.total
#         }