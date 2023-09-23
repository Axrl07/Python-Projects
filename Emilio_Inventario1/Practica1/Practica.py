productos = []

class Practica:
    def carga(self, archivoInv):
        print("----------*Cargando Inventario*----------")
        try:
            with open(archivoInv, 'r') as archivo:
                lineas = archivo.readlines()
                datosInv = {} #Creamos un diccionario para los datos de los productos
                for i in lineas:
                    partes = i.strip().split(';')
                    if len(partes) == 4:
                        detalles = partes[0].split() #Separamos "crear_producto" de nombre
                        if len(detalles) == 2 and detalles[0] == "crear_producto":
                            nombre = detalles[1]
                            cantidad = partes[1]
                            precio_unitario = partes[2]
                            valor_total = float(cantidad) *float(precio_unitario)
                            ubicacion = partes[3]
                            datosInv = {"nombre": nombre, "cantidad": cantidad, "precio_unitario": precio_unitario,
                                        "total": valor_total, "ubicacion": ubicacion}
                            productos.append (datosInv)

                    else:
                        print("Error al cargar el inventario")

                print("Carga realizada con éxito")
                print("Volviendo al Menú")

                return productos
        except Exception as e:
            print(f"Error: {e}")
            print()

    def Instrucciones(self, archivoMov):
        print("----------*Cargando Instrucciones*----------")
        try:
            with open(archivoMov, 'r') as archivo:
                lineas = archivo.readlines()
                for i in lineas:
                    partes = i.strip().split(';')
                    
                    if len(partes) == 3:
                        detalles = partes[0].split() #Separamos lainstrucción del nombre del producto
                        #Para agregar_stock
                        if len(detalles) == 2 and detalles[0] == "agregar_stock":
                            nombre = detalles[1]
                            cantidad = partes[1]
                            ubicacion = partes[2]
                            for lista in productos:
                                cantidadInV = int (cantidad)
                                nombreInv = lista["nombre"]
                                ubicacionInv = lista["ubicacion"]
                                if nombre == nombreInv and ubicacion == ubicacionInv:
                                    actualCantidad = int(lista["cantidad"])
                                    nuevaCantidad = actualCantidad + cantidadInV
                                    lista["cantidad"] = str(nuevaCantidad)
                                    Precio = int(lista["precio_unitario"])
                                    nuevoTotal = Precio * nuevaCantidad
                                    lista["total"] = str(nuevoTotal)
                                else:
                                    print("Error al querer agregar stock de producto")

                        elif len(detalles) == 2 and detalles[0] == "vender_producto":
                            nombreVen = detalles[1]
                            cantidadVen = partes[1]
                            ubicacionVen = partes[2]

                            for lista in productos:
                                nombreInv = lista["nombre"]
                                cantidadInV = lista["cantidad"]
                                ubicacionInv = lista["ubicacion"]
                                
                                if nombreVen == nombreInv and ubicacionVen == ubicacionInv and cantidadVen <= cantidadInV:
                                    #Actualizando la cantidad de productos
                                    actualCantidad = int(cantidadInV)
                                    actualVenta = int(cantidadVen)
                                    nuevaCantidad = actualCantidad - actualVenta
                                    lista["cantidad"] = str(nuevaCantidad)
                                    print(lista["nombre"])
                                    print(lista["cantidad"])
                                    print("Producto vendido")
                                else:
                                    print("Producto erroneo")

                        else:
                            print("")

                    else:
                        print("Error 2")
        except Exception as e:
            print(e)

    def archivo(self):
        print("----------*Cargando datos al archivo .txt*----------")
        print("")
        try:
            with open("Practica1/Informe.txt", "w+") as Informe:
                Informe.write("Informe de Inventario:\n")
                Informe.write("{:<12} {:<10} {:<17} {:<12} {}\n".format("Producto", "Cantidad", "Precio Unitario", "Valor total", "Ubicacion"))
                Informe.write("-" * 64 + "\n")

                for lista in productos:
                    Informe.write("{:<12} {:<10} {:<17} {:<12.2f} {}\n".format(lista["nombre"], lista["cantidad"],
                                lista["precio_unitario"], lista["total"], lista["ubicacion"]))
            print("----------*Datos cargados*----------")
            print("")
        except Exception as e:
            print(e)
            
    def opciones(self):

        while True:
            print("----------*Sistema de Inventario*----------")
            print("1. Cargar Inventario Inicial")
            print("2. Cargar Instrucciones de movimiento")
            print("3. Crear Informe de Inventario")
            print("4. Salir")
            print("")
            op = int(input("Ingrese el número de la opción deseada:"))
            print()

            if op == 1:
                archivoInv = input("Ingrese la ruta del archivo a cargar (con extension .inv): ")
                self.carga(archivoInv)
            
            elif op == 2:
                archivoMov = input("Ingrese la ruta del archivo a cargar (con extension .mov): ")
                self.Instrucciones(archivoMov)

            elif op == 3:
                self.archivo()
            
            elif op == 4:
                print("Cerrando Programa")
                break
            else:
                print("Ingrese el número correctamente")
                print()


if __name__ == '__main__':
    inicio = Practica()
    inicio.opciones()