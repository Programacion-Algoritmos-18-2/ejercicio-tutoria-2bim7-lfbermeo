import codecs
import sys

class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        #"data..."hace referencia la ruta del archico y con "r" lo lee
        self.archivo = codecs.open("data/ejemplo.txt", "r")

    def obtener_informacion(self):
        #readlines retorna los valores de archivo y las corre
        return self.archivo.readlines()

    def cerrar_archivo(self):
        #cierra el programa
        self.archivo.close()
