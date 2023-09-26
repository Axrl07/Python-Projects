# Comandos
# ctrl + k + c (comentar un bloque de codigo)
# ctrl + k + u (para descomentar bloque de codigo)

def cuentaRegresiva(i, s):
    if s > i:
        print(s)
        s -= 1
        cuentaRegresiva(i, s)
    else:
        print(s)
        print("fin cuenta regresiva")


cuentaRegresiva(0, 10)

'''
def factorial(numero) -> int:
    if numero == 0:
        numero = 1
    elif numero < 0:
        numero = "No puede calcularse el factorial de un número negativo"
    else:
        numero *= factorial(numero-1)
    return numero
mi_factorial = factorial(4)
print("Resultado del factorial es:", mi_factorial)
'''
