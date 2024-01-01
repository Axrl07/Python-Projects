

def exportarHTML(listado):
    listado.linkearIndices()
    try:
        nombreArchivo = "reporteHTML.html"
        with open(nombreArchivo, 'w') as archivo:
            archivo.write(f"<!DOCTYPE html>\n")
            archivo.write(f'\t<html lang="en">\n')
            archivo.write(f"\t\t<head>\n")
            archivo.write(f'\t\t\t<meta charset="UTF-8">\n')
            archivo.write(f'\t\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
            archivo.write(f'\t\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
            archivo.write(f"\t\t\t<title>Reporte de Canciones</title>\n")
            archivo.write(f"\t\t</head>\n")
            archivo.write(f"\t\t<body>\n")
            archivo.write(f"\t\t\t<h1>Reporte de Canciones</h1>\n")
            archivo.write(f'\t\t\t<table border="1">\n')
            archivo.write(f"\t\t\t\t<thead>\n")
            archivo.write(f"\t\t\t\t\t<tr>\n")
            archivo.write(f"\t\t\t\t\t\t<th>Nombre</th>\n")
            archivo.write(f"\t\t\t\t\t\t<th>Artista</th>\n")
            archivo.write(f"\t\t\t\t\t\t<th>Veces Reproducida</th>\n")
            archivo.write(f"\t\t\t\t\t</tr>\n")
            archivo.write(f"\t\t\t\t</thead>\n")
            archivo.write(f"\t\t\t\t<tbody>\n")
            for x in range(listado.tamanio):
                nodo = listado.obtenerNodoIndex(x).dato
                archivo.write(f"\t\t\t\t\t<tr>\n")
                archivo.write(f"\t\t\t\t\t\t<th>{nodo.nombre}</th>\n")
                archivo.write(f"\t\t\t\t\t\t<th>{nodo.artista}</th>\n")
                archivo.write(f"\t\t\t\t\t\t<th>{nodo.contador}</th>\n")
                archivo.write(f"\t\t\t\t\t</tr>\n")
            archivo.write(f"\t\t\t\t</tbody>\n")
            archivo.write(f"\t\t\t</table>\n")
            archivo.write(f"\t\t</body>\n")
            archivo.write(f"\t</html>\n")
    except Exception as ex:
        print("Error al crear el archivo HTML")
    print("Finalizamos con éxito la creación del archivo HTML")

def exportarXML(listado):
    # linkeando el listado de listas de reproduccion
    listado.linkearIndices()
    try:
        nombreArchivo = "exportacionXML.xml"
        with open(nombreArchivo, 'w') as archivo:
            archivo.write(f'<?xml version="1.0" encoding="UTF-8"?>\n')
            archivo.write(f'<ListasReproduccion>\n')
            # for iterativo de las listas de reproduccion
            for x in range(listado.tamanio):
                # valor del nodo iterativo
                nodo = listado.obtenerNodoIndex(x).dato
                # linkeando el listado de las propias canciones
                listadoAux = nodo.listadoCanciones
                listadoAux.linkearIndices()
                
                archivo.write(f'\t<ListaReproduccion nombre="{nodo.nombre}">\n')
                
                # for iterativo de las canciones
                for y in range(listadoAux.tamanio):
                    nodoAux = listadoAux.obtenerNodoIndex(y).dato
                    
                    archivo.write(f'\t\t<Cancion nombre="{nodoAux.nombre}">\n')
                    archivo.write(f'\t\t\t<Artista>{nodoAux.artista}</Artista>\n')
                    archivo.write(f'\t\t\t<Album>{nodoAux.album}</Album>\n')
                    archivo.write(f'\t\t\t<Imagen>{nodoAux.imagen}</Imagen>\n')
                    archivo.write(f'\t\t\t<Ruta>{nodoAux.ruta}</Ruta>\n')
                    archivo.write(f'\t\t\t<VecesReproducida>{nodoAux.contador}</VecesReproducida>\n')
                    archivo.write(f'\t\t</Cancion>\n')
                
                archivo.write(f'\t</ListaReproduccion>\n')
            archivo.write(f'</ListasReproduccion>\n')
    except Exception as ex:
        print("Error al crear el archivo XML")
    print("Finalizamos con éxito la creación del archivo XML")

from tkinter import messagebox as mb
import subprocess

def write_graphviz(lista):
    # nombre del archivo DOT
    nameTxt = "img.dot"

    # nombre del archivo JPG de salida
    nameImg = "img.jpg"

    if lista.primero == None:
         mb.showerror("Error","No hay sistemas de drones en el registro")
    else:
        f = open(nameTxt,'w')     
        contador = 0
        f.write('digraph g {\nfontname="Helvetica,Arial,sans-serif"\nnode [fontname="Helvetica,Arial,sans-serif"]\nedge [fontname="Helvetica,Arial,sans-serif"]\ngraph [\n')
        f.write('rankdir = "LF"\n];\nnode [\nfontsize = "10"\nshape = "ellipse"\n];\nedge [\n];\n')
                
        apuntador = lista.primero
      
        while apuntador:
            if apuntador == lista.ultimo:
                
                try:
                    f.write(f'"node{contador}" [\n')
                    
                    contador+=1
                    f.write(f'label = "<f0>{apuntador.dato.nombre}|<f1>{apuntador.dato.album}|<f2>{apuntador.dato.artista}|<f3>{apuntador.dato.contador}"\n')
                    f.write('shape = "record"\n];\n')
                except :
                    f.close()
                finally:
                    break
            else:
                try:
                    f.write(f'"node{contador}" [\nlabel = ')
                    contador+=1
                    
                    f.write(f'"{apuntador.dato.nombre}|{apuntador.dato.album}|{apuntador.dato.artista}|{apuntador.dato.contador}"\n')
                    f.write('shape = "record"\n];\n')
                except:
                    print("bandera final")

            apuntador = apuntador.siguiente
        contador = 0
        f.write('"Inicio"->\n')
        apuntador = lista.primero         
        while apuntador:
            if apuntador == lista.ultimo:
                try:
                    f.write(f'"node{contador}" -> "Final" [\n\n];\n')
                    contador +=1
                except:
                    f.close()
                finally:
                    break
            else:
                try:
                    f.write(f'"node{contador}" -> "node{contador+1}" [\n\n];\n')
                    contador +=1
                except:
                    f.close()
            apuntador = apuntador.siguiente        

        f.write("}")  
        f.close()
        command = ['dot', '-Tjpg', nameTxt, '-o', nameImg]
        subprocess.call(command)   