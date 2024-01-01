from Registrar_Usuario import AñadirUsuario
from Listado_Pelis import ListadoPelis
from ListaFavoritos import Favoritos
from Boletos import DatosBoletos    
from MenuAdmin import MenuAdmin
Admin = MenuAdmin()
Datos = DatosBoletos()
Fav = Favoritos()

class InfoPelis:
    def PelisFav(self):
        comprobar = int (input("Desea agregar una Película como favorita: 1.Si 2.No   "))
        if comprobar == 1:
            id = input("Ingrese el ID de su película favorita: ")
            existe = ListadoPelis.ComprobarID(id)
            if existe == True:
                Fav.AgregarFav
                Fav.Imprimir
            else:
                print("Ingrese el nombre correctamente")
            
        else: 
            print("Película no encontrada")


    def VerInfo(self):
        while True:
            opcion = int(input("¿Desea ver la información de la película? 1.Si 2.No     "))
            if opcion == 1:
                id = input("Escriba el ID de la película: ")
                existe = ListadoPelis.ComprobarID(id)
                if existe == True:
                    ListadoPelis.ImprimirPeli(id)
                    self.PelisFav()
                else: 
                    print("Película no encontrada")

            elif opcion == 2:
                print("Volviendo al Menú")
                break

class Compra:
    def comprar(self):
        ListadoPelis.ImprimirInformacion()
        id = input("¿Para que película desea comprar boletos? (Ingrese el ID): ")
        existe = ListadoPelis.ComprobarID(id)
        if existe == True:
            boletos = int(input("Ingrese la cantidad de Boletos deseados: "))
            sala = int(input("Ingrese el número de sala: "))
            asientos= int(input("Ingrese el número de asientos "))
            total = boletos*42
            print("El total a pagar es: Q.", total)
            print("-------------------------")
            op = int(input("¿Desea ingrear NIT? 1.Si 2. No "))

            if op == 1:
                nombre = input("Ingrese su nombre: ")
                nit = int(input("Ingrese número de NIT: "))
                direccion = input("Ingrese su dirección: ")
                print("-------------------------")
                Datos.AgregarCompra(nombre, nit, direccion, boletos, sala, asientos, total)
                Datos.Imprimir(nombre, boletos)

            elif op == 2:
                nombre = input("Ingrese su nombre: ")
                nit = "CF"
                direccion = input("Ingrese su dirección: ")
                print("-------------------------")
                Datos.AgregarCompra(nombre, nit, direccion, boletos, sala, asientos, total)
                Datos.Imprimir(nombre, boletos)
            else:
                print("Sin opción")
        else: 
            print("Película no encontrada")

class Cliente(): 
    def MenuCliente(self):
        while True:
            print("---------Bienvenido Al Menú---------")
            print("1. Ver listado de peliculas")
            print("2. Listado de peliculas favoritas")
            print("3. Comprar boletos")
            print("4. Historial de boletos comprados")
            print("0. Volver al Menú principal")
            opcion = int (input("Ingrese el número de la opción deseada: "))
            print("---------------------------")
            if opcion == 1:
                print("-----------------------")
                ListadoPelis.imprimir()
                info = InfoPelis()
                info.VerInfo()
                
            elif opcion == 2:
                Fav.Imprimir()

            elif opcion == 3:
                menu = Compra()
                menu.comprar()

            elif opcion == 4:
                nombre = input("Ingrese el nombre: ")
                Datos.ImprimirPorNombre(nombre)

            elif opcion == 0:
                print("Volviendo al Menú Principal")
                break

            else:
                print("Opción invalida")

class inicio():
    def iniciar(self, correo, contraseña):
        comprobar = AñadirUsuario.ComprobarDatos(correo, contraseña)
        comprobarRol = AñadirUsuario.ComprobarRol(correo)
        menu = Cliente()
        if comprobar is True and comprobarRol == "Cliente":
            print("Inicio de sesión exitoso")
            menu.MenuCliente()
        elif comprobar is True and comprobarRol == "Administrador":
            Admin.Menu()
        else:
            print("Usuario no existente")