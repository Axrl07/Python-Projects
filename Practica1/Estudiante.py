class Estudiante():

    def init_DatosPersonales(self, codigo, nombre, apellido, genero):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        if genero.lower() == "masculino":
            self.genero = 'm'
        else:
            self.genero = 'f'

    def init_DatosUsac(self, correo, facultad, escuela) -> None:
        self.correo = correo
        self.facultad = facultad
        self.escuela = escuela

    def init_DatosDomicilio(self, ciudad, zona, calle, avenida) -> None:
        self.ciudad = ciudad
        self.zona = zona
        self.calle = calle
        self.avenida = avenida


a1 = Estudiante()
a1.init_DatosPersonales(100, "Juan", "Pérez", "masculino")
a1.init_DatosUsac("juan@gmail.com", "Ingenieria", "Industrial")
a1.init_DatosDomicilio("Peten", "1", "2", "3")
a2 = Estudiante()
a2.init_DatosPersonales(101, "Angel", "Alvarado", "masculino")
a2.init_DatosUsac("202209714@fiusac.gt", "Ingenieria", "Ciencias y Sistenas")
a2.init_DatosDomicilio("Guatemala", "4", "5", "6")
a3 = Estudiante()
a3.init_DatosPersonales(102, "Vanessa", "Morales", "femenino")
a3.init_DatosUsac("vanessa@yahoo.es", "Derecho", "Mercantil")
a3.init_DatosDomicilio("Guatemala", "7", "8", "9")
