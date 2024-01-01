# las tuplas no pueden ser modificadas
tupla1 = (2988764180101, "Angel Enrique Alvarado Ruiz")
print(tupla1)
tupla2 = 202209714, "AEAR"
print(tupla2)
tupla3_incorrecto = (1)     # No es tupla
tupla3 = (1,)               # Si no se pone la coma, no es tupla
print(tupla3_incorrecto, type(tupla3_incorrecto))
print(tupla3, type(tupla3))

tupla4 = tupla1, tupla2, tupla3     # tupla de tuplas (3 elementos)
# anidación de tuplas (todos los elementos de todas las tuplas)
tupla5 = tupla1 + tupla2 + tupla3
tupla6 = ()                 # Tupla vacia


# longitud de una tupla
size = len(tupla6)
print(size)
