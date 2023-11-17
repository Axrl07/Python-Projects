class Nodo:
    def __init__(self, nombre, apellido, telefono, correo, contraseña, rol, fav=None):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol
        self.telefono = telefono
        self.fav = fav
        self.siguiente = None