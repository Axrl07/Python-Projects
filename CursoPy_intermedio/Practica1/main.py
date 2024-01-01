from Estudiante import Estudiante
from Estudiante import a1
from Estudiante import a2
from Estudiante import a3


class Practica1:
    ListadoEstudiantes = []

    def ejercicio1(self) -> None:
        # EJERCICIO 1
        def serieFib(n=1) -> int:
            if n >= 2:
                # caso recursivo
                return serieFib(n-1) + serieFib(n-2)
            # caso base
            return n
        try:
            max = int(
                input("Ingrese la cantidad de números de Fibonacci que desea encontrar  :"))
            for i in range(max):
                print(serieFib(n=i))
        except Exception as ex:
            print("Ingrese únicamente números enteros")

    def ejercicio2(self) -> None:
        # EJERCICIO 2
        print(" + + + Ingrese datos personales + + + ")
        while True:
            try:
                cod = int(input("Ingrese el código:  "))
                break
            except Exception as ex:
                print("Ingrese únicamente números enteros")
        nom = input("Ingrese el nombre:  ")
        ape = input("Ingrese el apellido:  ")
        gen = input("Ingrese el genero:  ")
        mail = input("Ingrese el correo:  ")
        print(" + + + Ingrese datos Universitarios + + + ")
        facu = input("Ingrese la facultad a la que pertenece:  ")
        escu = input("Ingrese la escuela a la que pertenece:  ")
        print(" + + + Ingrese datos de su Domicilio + + + ")
        ciu = input("Ingrese la ciudad en la que vive:  ")
        zone = input("Ingrese la zona:  ")
        cal = input("Ingrese la calle:  ")
        ave = input("Ingrese la avenida:  ")
        Alumno = Estudiante()
        Alumno.init_DatosPersonales(codigo=cod, nombre=nom,
                                    apellido=ape, genero=gen)
        Alumno.init_DatosUsac(correo=mail, facultad=facu, escuela=escu)
        Alumno.init_DatosDomicilio(
            ciudad=ciu, zona=zone, calle=cal, avenida=ave)
        self.ListadoEstudiantes.append(Alumno)

    def MostrarEjercicio2(self):
        if (len(self.ListadoEstudiantes) == 0):
            self.ListadoEstudiantes.append(a1)
            self.ListadoEstudiantes.append(a2)
            self.ListadoEstudiantes.append(a3)
        for es in self.ListadoEstudiantes:
            print(es.codigo, es.nombre, es.apellido, es.genero, es.correo, es.facultad, es.escuela, es.ciudad, es.zona, es.calle)

    def ejercicio3(self) -> None:
        # EJERCICIO 3
        def tabla_Multiplicar(num) -> None:
            if num >= 1 and num <= 10:
                listadoMultiplicaciones = []
                for i in range(10):
                    index = i+1
                    resultado = num * index
                    l1 = f" {num} * {index} = {resultado} "
                    listadoMultiplicaciones.append(l1)
                try:
                    nombreArchivo = f"tabla-{num}.txt"
                    with open(nombreArchivo, 'x') as archivo:
                        for linea in listadoMultiplicaciones:
                            archivo.write(linea + '\n')
                except Exception as ex:
                    print("El archivo ya existe, puede verificarlo")
                print("Finalizamos con éxito la creación del archivo")
            else:
                print("Vuelva a intentarlo ingresando números entre 1 y 10")
                print()
        try:
            numero = int(input("Ingrese un número del 1 al 10  :"))
            tabla_Multiplicar(numero)
        except Exception as ex:
            print("Ingrese únicamente números enteros")

    def menuPrincipal(self):
        # MENU PRINCIPAL
        try:
            while True:
                print(" - - - - Menú Principal - - - ")
                print(" 1. imprimir números de la serie de Fibonacci ")
                print(" 2. Crear instancias de la clase Estudiante ")
                print(" 3. Mostrar los alumnos creados (ya existen 3) ")
                print(" 4. Crear tabla de un número multiplicado de 1 a 10")
                print(" 5. Salir del programa")
                option = int(
                    input("Ingrese el número de la opción a la que desea ingresar  :"))
                if option == 1:
                    self.ejercicio1()
                elif option == 2:
                    self.ejercicio2()
                elif option == 3:
                    self.MostrarEjercicio2()
                elif option == 4:
                    self.ejercicio3()
                elif option == 5:
                    print("Saliendo del programa")
                    break
                else:
                    print(
                        "Ingrese el número correspondiente a la opción que desea seleccionar")
                    print()
        except Exception as ex:
            print("Ingrese valores numéricos")


if __name__ == '__main__':
    inicio = Practica1()
    inicio.menuPrincipal()
