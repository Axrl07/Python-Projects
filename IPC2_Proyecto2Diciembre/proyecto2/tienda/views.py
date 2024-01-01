import json
from django.http import JsonResponse
from django.shortcuts import render, redirect

from Tienda.codigo.appData import *
from Tienda.codigo.funciones import *
from Tienda.codigo.clases import *

#----------------Home--------------------
def home(request):
    global facturas, productos, clientes
    guardar_xml("Facultad.xml", facturas, "listadoFacturas")
    guardar_xml("Productos.xml", productos, "listadoProductos")
    guardar_xml("Clientes.xml", clientes, "listadoClientes")
    return render(request,"gestionTienda.html")

#----------------Producto--------------------
def gestionProducto(request):
    global productos
    return render(request,'gestionProductos.html',{"productos": productos})    

def registrarProducto(request):
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['numPrecio']
    stock = request.POST['numStock']

    print(nombre)
    print(descripcion)
    print(precio)
    print(stock)
    x= Producto(nombre,descripcion,precio,stock)
    global productos
    productos.append(x)

    return render(request,'gestionProductos.html',{"productos":productos})

def edicionProducto(request, id):
    global productos
    x= None

    for p in productos:
        if  p.id == id:
            x = p    
    print(x.nombre)        
    return render(request, "editarProducto.html", {"producto":x})

def editarProducto(request):
    global productos

    for p in productos:
        if p.id == request.POST['txtId']:
            p.nombre = request.POST['txtNombre']
            p.descripcion= request.POST['txtDescripcion']
            p.precio = request.POST['numPrecio']
            p.precio = request.POST['numStock']
    print(p.nombre)        

    return render(request,'gestionProductos.html',{"productos":productos})      

def eliminarProducto(request, id):
    global productos
    for p in productos:
        if p.id == id:
            productos.remove(p)
    return render(request,'gestionProductos.html',{"productos":productos})        

#----------------Cliente--------------------
def gestionCliente(request):
    return render(request,'gestionCliente.html')    

def registrarCliente(request):
    nombre = request.POST['txtNombre']
    direccion = request.POST['txtDireccion']
    nit = request.POST['numNit']
    telefono = request.POST['numTelefono']
    #self, nombre, direccion,nit, telefono

    print(nombre)
    print(direccion)
    print(nit)
    print(telefono)
    x = Cliente(nombre,direccion,telefono, nit)
    global clientes
    clientes.append(x)

    return render(request,'gestionCliente.html',{"clientes":clientes})

def eliminarClientes(request, id):
    global clientes
    for p in clientes:
        if p.id == id:
            clientes.remove(p)
    return render(request,'gestionCliente.html',{"clientes":clientes})        

def edicionCliente(request, id):
    global clientes
    x= None

    for p in clientes:
        if  p.id == id:
            x = p    
    print(x.nombre)        
    return render(request, "editarClientes.html", {"clientes":x})

def editarClientes(request):
    global clientes

    for p in clientes:
        if p.id == request.POST['txtId']:
            p.nombre = request.POST['txtNombre']
            p.direccion= request.POST['txDireccion']
            p.nit = request.POST['numNit']
            p.telefono = request.POST['numTelefono']
    print(p.nombre)        

    return render(request,'gestionCliente.html',{"clientes":clientes})      

#    def __init__(self, nombre, direccion,nit, telefono):

#----------------Factura--------------------

def gestionFactura(request):
    global productos
    return render(request,'gestionFactura.html')
    
def postFactura(request):
    global facturas
    if request == "POST":
        # recibiendo los datos del formulario
        data = json.loads(request.body.decode('utf-8'))
        nit = data.get('txtNit')
        nombre = data.get('txtNombre')
        subTotal = data.get('numCantidad')
        
        # # Esto será una cadena JSON
        listadoCompras_str = data.get('txtProducto')
        listadoCompras = json.loads(listadoCompras_str) 
        
        factura_objeto = Factura(nit, nombre, listadoCompras, subTotal)
        facturas.append(factura_objeto)
        
        factura_objeto = [nit, nombre]
        if len(factura_objeto) == 2:
            return JsonResponse({ 'msg': 'se subió la factura con exito'}, status=200)
        else:
            return JsonResponse({ 'msg': 'error al subir la factura'}, status=400)

def sistemaFacturacion(request):
    cliente = request.POST['Cliente']
    producto = request.POST['Productoo']
    cantidad = request.POST['cantidad']
    precio =request.POST['precioPro']


    print(cliente)
    print(producto)
    print(cantidad)
    print(precio)
    x = Factura(cliente,producto,cantidad, precio)
    global facturas
    facturas.append(x)


    return render(request,'gestionFactura.html',{"facturas":facturas})

# metodos para obtener datos

def getCLientes(request):
    global clientes
    diccionario = []
    for clien in clientes:
        diccionario.append(clien.to_dict())
    if request.method == "GET":
        return JsonResponse(diccionario, status=200)
    
def getProductos(request):
    global productos
    diccionario = []
    for produc in productos:
        diccionario.append(produc.to_dict())
    if request.method == "GET":
        return JsonResponse(diccionario, status=200)
    
def getFacturas(request):
    global facturas
    diccionario = []
    for fact in facturas:
        diccionario.append(fact.to_dict())
    if request.method == "GET":
        return JsonResponse(diccionario, status=200)