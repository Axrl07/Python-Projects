import os

'''
# MODO DE CREACION (x) crea el archivo y si ya existe tira error
try:
    archivo = open("file.txt", "x")
    archivo.close()
except Exception as e:
    print("el archivo ya existe")

# MODO LECTURA (r) si no existe tira error y solamente lee
try:
    archivo = open("file.txt")
    print(archivo.read())
    archivo.close()
except Exception as e:
    print("El archivo no existe")

# MODO DE ESCRITURA (w) Vacía el contenido del archivo y escribe
archivo = open("file.txt", "w")
archivo.close()

# MODO DE AGREGAR (a) mantiene datos antiguos y agrega
archivo = open("file.txt", "a")
archivo.close()

# REMOVER ARCHIVO: para ello importamos (os)

archivo = "file.txt"
# os.remove(archivo) tira error de FileNotFoundError si archivo no existe

# Manejo del error
if os.path.exists(archivo):
    os.remove(archivo)
else:
    print("El archivo no existe")
'''

# lectura de archivos
ruta = "file.txt"
# apretura de archivos
archivo = open(ruta)

'''
# lectura de todo el contenido del archivo
contenido = archivo.read()
print(contenido)
'''
'''
# lectura en partes del archivo

contenido_1 = archivo.read(14 + 1).strip()
# 14 es nombre completo de la primera linea + 1 porque el ENTER es un caracter
contenido_2 = archivo.read(13 + 1).strip()
# 14 caracteres componen el nombre rebeca

print(contenido_1)
print(contenido_2)
'''

# cerrar el archivo
archivo.close()
