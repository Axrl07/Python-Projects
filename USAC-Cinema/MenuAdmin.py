from Registrar_Usuario import AñadirUsuario
from Registrar_Usuario import ListaUsuarios
from Listado_Pelis import ListadoPelis
from Salas import ListaSalas

class Opciones:
    def GestionUsuarios(self):
        while True:
            print("--------Gestión de Usuarios--------")
            print("1. Agregar Usuario")
            print("2. Mostrar Usuarios")
            print("3. Modificar Usuarios")
            print("4. Eliminar Usuarios")
            print("5. Crear Archivo XML")
            print("0. Volver al Menu de Selección")
            print("--------------------------")
            opcion = int(input("Seleccione la opción deseada: "))

            if opcion == 1:
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

            elif opcion == 2:
                AñadirUsuario.ImprimirTodo()
            elif opcion == 3:
                correo = input("Ingrese el correo del usuario que desea modificar:")
                
                comprobar = AñadirUsuario.ComprobarCorreo(correo)

                if comprobar == True:
                    nombre_nuevo = input ("Ingrese nuevo nombre: ")
                    apellido_nuevo = input ("Ingrese nuevo apellido: ")
                    telefono_nuevo = input ("Ingrese nuevo número de teléfono: ")
                    correo_nuevo = input("Ingrese nuevo correo electrónico: ")
                    contraseña_nueva = input ("Ingrese nuevo contraseña: ")
                    rol_nuevo = input("Ingrese un rol: ")
                    AñadirUsuario.Modificar(correo, nombre_nuevo, apellido_nuevo, telefono_nuevo, correo_nuevo, contraseña_nueva, rol_nuevo)
                    AñadirUsuario.GuardarXML("Usuarios.xml")
                    print("Usuario modificado")
                else:
                    print("El correo no existe")
                print("--------------------------")
            elif opcion == 4:
                print("--------------------------")
                correo = input("Ingrese el correo electrónico del usuario deseado: ")
                
                comprobar = AñadirUsuario.ComprobarCorreo(correo)
                if comprobar == True:
                    AñadirUsuario.GuardarXML("Usuarios.xml")
                    AñadirUsuario.Eliminar(correo)
                else:
                    print("El usuario no existe")

            elif opcion == 5:
                AñadirUsuario.GuardarXML("Usuarios.xml")
                print("Archivo Generado Con Exito")

            elif opcion == 6:
                NuevaLista = ListaUsuarios()
                NuevaLista.cargar_desde_xml("Usuarios.xml")

            elif opcion == 0:
                print("Volviendo al Menú...")
                break
            else: 
                print("Opción Incorrecta")

    def GestionPeliculas(self):
        while True:
            print("--------Gestión de Categorías y Películas--------")
            print("1. Agregar Película")
            print("2. Mostrar Películas")
            print("3. Modificar Películas")
            print("4. Eliminar Películas")
            print("5. Guardar en XML")
            print("0. Volver al Menu de Selección")
            print("--------------------------")
            opcion = int(input("Seleccione la opción deseada: "))
            if opcion == 1:
                id = input ("Ingrese su ID: ")
                nombre = input ("Ingrese el Nombre: ")
                fecha = input ("Ingrese fecha de la función: ")
                hora = input("Ingrese hora de la función: ")
                categoria = input ("Ingrese la categoria: ")
                print("--------------------------")
                comprobar = ListadoPelis.ComprobarID(id)

                if comprobar == False:
                    ListadoPelis.Agregar(id, nombre, fecha, hora, categoria)
                    ListadoPelis.guardar_en_xml("Películas.xml")
                else:
                    print("El correo ya esta asociado a otro usuario")

            elif opcion == 2:
                ListadoPelis.ImprimirInformacion()
            elif opcion == 3:
                id = input("Ingrese el ID de la película que desea modificar:")
                
                comprobar = ListadoPelis.ComprobarID(id)

                if comprobar == True:
                    ID_nuevo = input ("Ingrese nuevo ID: ")
                    nombre_nuevo = input ("Ingrese nuevo nombre: ")
                    fecha_nuevo = input ("Ingrese la nueva fecha de función: ")
                    hora_nuevo = input("Ingrese nueva hora de la función: ")
                    categoria_nueva = input ("Ingrese nueva categoría: ")
                    ListadoPelis.Modificar(id, ID_nuevo, nombre_nuevo, fecha_nuevo, hora_nuevo, categoria_nueva)
                    ListadoPelis.guardar_en_xml("Películas.xml")
                    print("Película modificada")
                else:
                    print("El correo no existe")
                print("--------------------------")
            elif opcion == 4:
                print("--------------------------")
                id = input("Ingrese el ID de la película que desea borrar: ")
                
                comprobar = ListadoPelis.ComprobarID(id)
                if comprobar == True:
                    ListadoPelis.Eliminar(id)
                    ListadoPelis.guardar_en_xml("Películas.xml")
                    print("Película eliminada")
                else:
                    print("Película no encontrada")

            elif opcion == 5:
                ListadoPelis.guardar_en_xml("Películas.xml")
                print("Archivo Generado Con Exito")
                
            elif opcion == 0:
                print("Volviendo al Menú...")
                break
            else: 
                print("Opción Incorrecta")

    def GestionSalas(self):
        while True: 
            print("--------Gestión de Salas--------")
            print("1. Agregar Sala")
            print("2. Mostrar Salas")
            print("3. Modificar Sala")
            print("4. Eliminar Salas")
            print("5. Guardar en XML")
            print("0. Volver al Menu de Selección")
            print("--------------------------")
            opcion = int(input("Seleccione la opción deseada: "))
    
            if opcion == 1:
                N_sala = input ("Ingrese Número de Sala: ")
                N_asientos = input ("Ingrese el Número de Asientos: ")
                print("--------------------------")
                comprobar = ListaSalas.Comprobar(N_sala)

                if comprobar == False:
                    ListaSalas.agregar(N_sala, N_asientos)
                    ListaSalas.GuardarXML("Salas.xml")
                else:
                    print("La sala ya existe")

            elif opcion == 2:
                ListaSalas.imprimir()
            elif opcion == 3:
                N_sala = input("Ingrese el Número de Sala a Modificar:")
                
                comprobar = ListaSalas.Comprobar(N_sala)

                if comprobar == True:
                    N_salaNuevo = input ("Ingrese nuevonúmero de sala: ")
                    N_asientosNuevos = input ("Ingrese nuevo número de asientos: ")
                    ListaSalas.Modificar(N_sala, N_salaNuevo, N_asientosNuevos)
                    ListaSalas.GuardarXML("Salas.xml")
                    print("Sala modificada")
                else:
                    print("La sala no existe")
                print("--------------------------")
            elif opcion == 4:
                print("--------------------------")
                N_sala = input("Ingrese el número de sala que desee modificar: ")
                
                comprobar = ListaSalas.Comprobar(N_sala)
                if comprobar == True:
                    ListaSalas.Eliminar(N_sala)
                    ListaSalas.GuardarXML("Salas.xml")
                    print("Sala eliminada")
                else:
                    print("Sala no encontrada")

            elif opcion == 5:
                ListaSalas.GuardarXML("Salas.xml")
                print("Archivo Generado Con Exito")

            elif opcion == 0:
                print("Volviendo al Menú...")
                break
            else: 
                print("Opción Incorrecta")

class MenuAdmin:
    def Menu(self):
        op = Opciones()
        while True:
            print("--------Bienvenido Administrador--------")
            print("1. Gestionar Usuarios")
            print("2. Gestionar Categorías y Películas")
            print("3. Gestionar Salas")
            print("0. Cerrar Sesion")
            print("--------------------------")
            opcion = int(input("Seleccione la opcion deseada: "))

            if opcion == 1:
                print("--------------------------")
                op.GestionUsuarios()
            elif opcion == 2:
                print("--------------------------")
                op.GestionPeliculas()
            elif opcion == 3:
                print("--------------------------")
                op.GestionSalas()
            elif opcion == 0:
                print("Cerrando Sesión...")
                break
            else:
                print("Opción Incorrecta")