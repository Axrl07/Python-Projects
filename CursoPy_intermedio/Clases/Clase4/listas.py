# lista homogenea (todo de un mismo tipo)
lista1 = [1, 2, 3,]
# lista heterogenea (tiene mezclas de valores)
lista2 = ["uno", 2, True, (), [1.5, 2.5, 3.5]]

print("lista 1 homogenea", lista1)
print("lista 2 heterogenea", lista2)

# anidación de listas

# lista que tiene 2 elemntos
lista3 = [lista1, lista2]
print(lista3)
# lista que contenga los elementos lista1 y lista2
lista4 = lista1 + lista2
print(lista4)

lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index =   0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# negat = -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# obteniendo elementos de una lista
indice = -1
indice2 = 9
valor = lista5[indice]
valor2 = lista5[indice2]
print(valor, valor2)
indice_exterior = 1
indice_interior = -1
valorAnidado = lista3[indice_exterior][indice_interior]
print(valorAnidado)

# rangos (intervalo) [indice que queremos -1: indice que queremos +1]
sub_lista5_1 = lista5[:5]
'''
print(sub_lista5_1)
'''
# .append(valor) agrega algo al final de la lista
sub_lista5_1[-1] = "Cinco"
sub_lista5_1[0] = False
sub_lista5_1.append("seis")
'''
print(sub_lista5_1)
'''
# .insert(indice,valor) elimina el último elemento de la lista
sub_lista5_1.insert(0, True)
sub_lista5_1.insert(2, 1)
sub_lista5_1.insert(8, "siete")
sub_lista5_1.append(True)
sub_lista5_1.append(False)
'''
print(sub_lista5_1)
'''
# .remove() elimina un elemento de la lista (el que aparezca primero)
sub_lista5_1.remove(True)
sub_lista5_1.remove(False)
'''
print(sub_lista5_1)
'''
# .pop() elimina el último elemento de la lista
sub_lista5_1.pop()
sub_lista5_1.pop(6)
sub_lista5_1.append(False)
print(sub_lista5_1)

# .index(valor) me devuelve el indice del elemento que busco
Vbuscado = 4
indice = sub_lista5_1.index(Vbuscado)
print(
    f"el valor buscado \"{Vbuscado}\" se encuentra en el indice {indice} de la sub lista {sub_lista5_1}")
