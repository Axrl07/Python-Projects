import xml.etree.ElementTree as ET
import random
from Tienda.codigo.clases import *

# generador de id
def generadorId() -> str:
    resultadoId = ''
    caracteres = 'abcdefghijkmnlopqrstuvwxyz0123456789'
    for i in range(14):
        if len(resultadoId) == 4 or len(resultadoId) == 9:
            resultadoId += '-'
        resultadoId += caracteres[random.randint(0, 35)]
        if len(resultadoId) == 14:
            return resultadoId
# se usa de forma automatica en la clase Prop

# guardar xml
def guardar_xml(nombreArchivo, lista, nombreLista="data"):
    root = ET.Element(f'listado_{nombreLista.lower()}')
    
    for item in lista:
        elemento = ET.SubElement(root, item.__class__.__name__)
        for attr, value in vars(item).items():
            ET.SubElement(elemento, attr).text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(nombreArchivo)
    print(f"Datos guardados en {nombreArchivo}")

# leer xml
def leer_xml(nombreArchivo, clase_objeto) -> list:
        root = ET.parse(nombreArchivo).getroot()
        resultado = []

        for elemento in root.findall(clase_objeto.__name__):
            atributos = {hijo.tag: hijo.text for hijo in elemento}
            objeto = clase_objeto(**atributos)
            resultado.append(objeto)

        print(f"Datos de {nombreArchivo} fueron leidos")
        return resultado

# actualizar xml
def actualizar_xml(nombreArchivo, listado):
        # Leer el archivo XML
        root = ET.parse(nombreArchivo).getroot()

        # Borrar todos los elementos existentes del tipo de datos
        for elem in root.findall(listado[0].__class__.__name__):
            root.remove(elem)

        # Agregar nuevos elementos actualizados
        for item in listado:
            elemento = ET.SubElement(root, item.__class__.__name__)
            for attr, value in vars(item).items():
                ET.SubElement(elemento, attr).text = str(value)

        # Escribir la estructura actualizada en el archivo XML
        tree = ET.ElementTree(root)
        tree.write(nombreArchivo)
        print(f"Datos actualizados en {nombreArchivo}")

# Ejemplo de uso:
# AppData.guardar_xml("facturas.xml", facturas, facturas)
# facturas = AppData.leer_xml("facturas.xml", Factura)
# AppData.actualizar_xml("facturas.xml", facturas)