class Persona(object):
    """
    """
    
    def __init__(self, n, a, e):
        """
        """
        #declaro mis variables a utilizar
        self.nombres = n
        self.apellido = a
        self.edad = int(e)
        #Realizo los metodos agregar y obtener para cada una de las variables
    def agregarNombres(self, n):
        """
        """
        self.nombres = n

    def obtenerNombres(self):
        """
        """
        return self.nombres

    def agregarApellido(self, n):
        """
        """
        self.apellido = n

    def obtenerApellido(self):
        """
        """
        return self.apellido

    def agregarEdad(self, n):
        """
        """
        self.edad = int(n)

    def obtenerEdad(self):
        """
        """
        return self.edad

