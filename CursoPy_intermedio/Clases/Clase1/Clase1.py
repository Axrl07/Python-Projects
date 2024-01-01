# esto es una función
def sumar(num1, num2) -> int:
    res = num1 + num2
    return res


def restar(num1, num2) -> None:
    res = num1 + num2
    return res


def dividir(numerador, denominador) -> float:
    res = numerador/denominador
    return res


# CLAVE = VALOR forma precisa de ingresar datos a los parametros
aux = dividir(denominador=3, numerador=6)
print(aux)

# usando clave=valor podemos definir datos predeterminados si no se envia nada a la función


def multiplicar(num1=5, num2=10) -> int:
    res = num1 * num2
    return res


def lista_utiles(*utiles) -> list:
    print("el tamaño de la lista es", len(utiles))
    lista = []
    for util in utiles:
        lista.append(util)
    return lista


lista_nueva = lista_utiles("libro", "cuaderno", "lápiz", "borrador")
print(lista_utiles)
