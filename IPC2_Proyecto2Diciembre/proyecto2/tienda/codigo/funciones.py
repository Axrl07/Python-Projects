import xml.etree.ElementTree as ET
import random

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
