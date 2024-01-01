from django.urls import path
from . import views



urlpatterns=[
    path('' , views.home),
    path('gestionProductos/', views.gestionProducto),
    path('eliminarClientes/<id>', views.eliminarClientes),
    path('edicionCliente/<id>', views.edicionCliente),
    path('editarClientes/', views.editarClientes),
    path('gestionCliente/', views.gestionCliente),
    path('registrarCliente/', views.registrarCliente),
    path('registrarProducto/', views.registrarProducto),
    path('edicionProducto/<id>', views.edicionProducto),
    path('editarProducto/', views.editarProducto),
    path('gestionTienda/', views.home),
    path('eliminarProducto/<id>', views.eliminarProducto),
    path('gestionFactura/', views.gestionFactura),
    
    
    # rutas de solicitud de datos
    path('getCLientes/', views.getCLientes),
    path('postFactura/', views.postFactura),
    path('getProductos/', views.getProductos),
    path('getFacturas/', views.getFacturas),
    path('postFactura', views.postFactura),
    path('sistemaFacturacion/', views.sistemaFacturacion),
]