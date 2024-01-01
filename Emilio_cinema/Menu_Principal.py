from Iniciar_Sesion import inicio
from Registrar_Usuario import AñadirUsuario
from Listado_Pelis import ListadoPelis
iniciar = inicio()

class menuPrincipal:

    def registro(self):
        nombre = input ("Ingrese su nombre: ")
        apellido = input ("Ingrese su apellido: ")
        telefono = input ("Ingrese su número de teléfono: ")
        correo = input("Ingrese su correo electrónico: ")
        contraseña = input ("Ingrese su contraseña: ")
        print("--------------------------")
        comprobar = AñadirUsuario.ComprobarDatos(correo, contraseña)

        if comprobar == False:
            AñadirUsuario.Agregar(nombre, apellido, telefono, correo, contraseña, "Cliente")
            AñadirUsuario.GuardarXML("Usuarios.xml")
        else:
            print("El correo ya esta asociado a otro usuario")

    def menu(self):
        AñadirUsuario.Agregar("Emilio", "Rivera", "58725886", "lemilioriveray@gmail.com", "123456", "Administrador")
        ListadoPelis.Agregar("1","Star Wars: El Imperio Contraataca", "8/06/2023", "2:00 PM", "Ciencia Ficcion")
        ListadoPelis.Agregar("2","E.T", "8/06/2023", "3:00 PM", "Ciencia Ficcion")
        ListadoPelis.Agregar("3","Batman", "8/06/2023", "5:00 PM", "Accion")
        ListadoPelis.Agregar("4","Spiderman", "8/06/2023", "6:00 PM", "Accion")


        while True:
            print("---------- MENÚ -----------")
            print("1. Iniciar Sesión")
            print("2. Registrar Usuario")
            print("3. Listado de Películas")
            print("0. Salir")

            opcion = int(input("Selecciona una opción: "))
            print("---------------------------")

            if opcion == 1:
                correo = input("Ingrese su correo: ")
                contraseña = input("Ingrese su contraseña: ")
                iniciar.iniciar(correo, contraseña)

            elif opcion == 2:
                self.registro()

            elif opcion == 3:
                ListadoPelis.imprimir()

            elif opcion == 0:
                print("Cerrando Programa")
                break

            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == '__main__':
    inicio = menuPrincipal()
    inicio.menu()