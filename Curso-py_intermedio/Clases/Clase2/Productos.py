import datetime
# clase


class Producto:
    pass


# Instancias
p1 = Producto()
p2 = Producto()


class Producto:
    codigo = "001"
    nombre = "laptop dell inspiron 3000"
    marca = "dell"
    modelo = "Inspiron 3000"
    precio = 5000


# Instancias
p1 = Producto()
p2 = Producto()

'''
print(p1.nombre, p1.codigo, p1.precio)
print(p2.nombre, p2.codigo, p2.precio)
'''

p2.codigo = "002"
p2.nombre = "laptop dell G5"
p2.modelo = "G5"
p2.precio = 7000

'''
print("------------------------------")
print(p1.nombre, p1.codigo, p1.precio)
print(p2.nombre, p2.codigo, p2.precio)
'''


class Producto():
    def __init__(self, codigo, nombre, marca, precio, modelo=None) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.modelo = modelo
        self.precio_iva = precio*1.12
        self.fecha_creacion = datetime.date.today()

    def presentacion(self, lema=""):
        print(self.nombre, lema)

    def calcular_total(self, unidades=1) -> float:
        resultado = self.precio_iva*unidades
        return resultado


p1 = Producto("001", "laptop Dell Inspiron 3000",
              "DELL", 10000, "Inspiron 3000")
p2 = Producto("002", "laptop HP Pavilion 15", "HP", 8000, "Pavilion 15")
p3 = Producto("003", "laptop Lenovo ThinkPad", "Lenovo", 4500)

'''
print(p1.nombre, p1.codigo, p1.precio)
print(p2.nombre, p2.codigo, p2.precio)
print(p3.nombre, p3.codigo, p3.precio)
# p1.presentacion("La mejor Laptop del munodo")
# p2.presentacion("La mejor Laptop del munodo")
# p3.presentacion("La mejor Laptop del munodo")
'''

unidades = 3
total = p3.calcular_total(unidades)
print("Por la compra de", unidades, "unidades de", p3.nombre, "es", total)
