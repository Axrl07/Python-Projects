from django.shortcuts import render
from Tienda.codigo.clases import *
from Tienda.codigo.funciones import *
from Tienda.codigo.appData import *

# Create your views here.

#------------------Home----------------------
def home(request):
    # if len(productos) == 0 and len(clientes) == 0 and len(facturas) == 0:
    #     leer_xml("Tienda/data/listado_productos.xml", Producto)
    #     leer_xml("Tienda/data/listado_clientes.xml", Cliente)
    #     leer_xml("Tienda/data/listado_facturas.xml", Factura)
    return render(request,"gestionTienda.html")

#----------------Producto--------------------
def gestionProducto(request):
    productos
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
    productos
    productos.append(x)

    return render(request,'gestionProductos.html',{"productos":productos})

def edicionProducto(request, id):
    productos
    x= None

    for p in productos:
        if  p.id == id:
            x = p    
    print(x.nombre)        
    return render(request, "editarProducto.html", {"producto":x})

def editarProducto(request):
    productos

    for p in productos:
        if p.id == request.POST['txtId']:
            p.nombre = request.POST['txtNombre']
            p.descripcion= request.POST['txtDescripcion']
            p.precio = request.POST['numPrecio']
            p.precio = request.POST['numStock']
    print(p.nombre)        

    return render(request,'gestionProductos.html',{"productos":productos})      

def eliminarProducto(request, id):
    productos
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
    x= Cliente(nombre,direccion,nit,telefono)
    clientes
    clientes.append(x)

    return render(request,'gestionCliente.html',{"clientes":clientes})

def edicionCliente(request, id):
    clientes
    x= None

    for p in clientes:
        if  p.id == id:
            x = p    
    print(x.nombre)        
    return render(request, "editarCliente.html", {"cliente":x})

def editarCliente(request):
    clientes

    for p in clientes:
        if p.id == request.POST['txtId']:
            p.nombre = request.POST['txtNombre']
            p.direccion= request.POST['txtDireccion']
            p.nit = request.POST['numNit']
            p.telefono = request.POST['numTelefono']
    print(p.nombre)        

    return render(request,'gestionProductos.html',{"clientes":clientes})      