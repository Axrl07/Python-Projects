lista = []
# creacion del diccionariop
diccionario1 = {"codigo": 202209714, "nombre": "angel",
                "DPI": 2988, "matriculado": True}
lista.append(diccionario1)
diccionario2 = {"codigo": 298846851, "nombre": "enrique",
                "DPI": 4080, "matriculado": False}
lista.append(diccionario2)


class main:
    def ingresoDatos(self) -> None:
        name = input("Ingrese su nombre")
        while True:
            try:
                code = int(input("Ingrese su carnet"))
                dpi = int(input("Ingrese su DPI"))
                break
            except:
                print("Ingrese un valor numerico")
        matriculado = input(
            "ingrese \"si\" si esta matriculado, en caso contrario ingrese\"no\". ")
        if (matriculado.lower() == "si"):
            matricula = True
        else:
            matricula = False
        # asignacion de valores al diccionario
        diccionario3 = {"codigo": code, "nombre": name,
                        "DPI": dpi, "matriculado": matricula}
        lista.append(diccionario3)


if __name__ == "__main__":
    main = main()
    main.ingresoDatos()
    main.mostrarDatos()
