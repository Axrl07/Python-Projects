class ejercicio1:

    def CalculoIMC(self, peso: float, altura: float) -> float:
        imc = peso / (altura ** 2)
        return imc

    def SolicitudDatos(self) -> None:
        print(" + + + + + Cálculo de IMC + + + + + ")
        nombre = input(" Ingrese el nombre que desea utilizar como usuario : ")
        while True:
            try:
                peso = float(input(" Ingrese su peso (en Kilogramos) : "))
                altura = float(input(" Ingrese su altura (en Metros) : "))
                if (peso > 0 and altura > 0):
                    break
            except Exception as ex:
                print("Ingrese únicamente números reales mayores a cero")
        imc = self.CalculoIMC(peso, altura)
        diccionario = {"nombre": nombre, "peso": peso,
                       "altura": altura, "imc": imc}
        lista.append(diccionario)

    def MostrarDatos(self) -> None:
        '''
        Recordemos que el imc tiene las siguientes categorías:
        Bajo peso = < 18.5
        Normal = 18.5 – 24.9
        Sobrepeso = 25 – 29.9
        Obesidad = >30
        '''
        print(" + + + + + Datos de los usuarios + + + + + ")
        for i in lista:
            if (i["imc"] < 18.5):
                print(
                    f'{i["nombre"]} tiene un imc de {i["imc"]:.2f} y se encuentra en la categoría de Bajo peso')
            elif (i["imc"] >= 18.5 and i["imc"] <= 24.9):
                print(
                    f'{i["nombre"]} tiene un imc de {i["imc"]:.2f} y se encuentra en la categoría de Normal')
            elif (i["imc"] >= 25 and i["imc"] <= 29.9):
                print(
                    f'{i["nombre"]} tiene un imc de {i["imc"]:.2f} y se encuentra en la categoría de Sobrepeso')
            else:
                print(
                    f'{i["nombre"]} tiene un imc de {i["imc"]:.2f} y se encuentra en la categoría de Obesidad')


def CalculoVocales() -> None:
    print(" + + + + + Calculo de Vocales + + + + + ")
    palabra = input("Ingrese una palabra : ")
    diccionario = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for i in palabra.lower():
        if i in diccionario:
            diccionario[i] += 1
    print(f'De la palabra ingresada "{palabra}" obtuvimos :')
    print(diccionario)


if __name__ == '__main__':
    lista = []
    ejercicio1 = ejercicio1()
    # MENU PRINCIPAL
    while True:
        print(" - - - - Menú Principal - - - ")
        print(" 1. Ingrese los datos de un usuario para calcular su IMC ")
        print(" 2. Mostrar datos de los usuarios ")
        print(" 3. Calcular la cantidad de vocales en una palabra")
        print(" 4. Salir del programa")
        while True:
            try:
                option = int(
                    input("Ingrese el número de la opción a la que desea ingresar  :"))
                print()
                break
            except Exception as ex:
                print("Ingrese únicamente números enteros")
                print()
        if option == 1:
            ejercicio1.SolicitudDatos()
            print()
        elif option == 2:
            ejercicio1.MostrarDatos()
            print()
        elif option == 3:
            CalculoVocales()
            print()
        elif option == 4:
            print("Saliendo del programa")
            print()
            break
        else:
            print(
                "Ingrese el número correspondiente a la opción que desea seleccionar")
            print()
