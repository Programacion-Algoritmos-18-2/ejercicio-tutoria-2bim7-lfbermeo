from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.persona import Persona
from paquete_combinacion.combinacion import *
#Creo mi objeto  para abrir el archivo
m = MiArchivo()

lista = m.obtener_informacion() 
#Separo de la data por ; para cada una de las lineas de la data
lista = [l.split(";") for l in lista]
#Creo una lista donde se alamcenará los datos de edades
lista_personas = []
#recorro la lista
for d in lista:
	persona = Persona(d[0], d[1], d[2])
	#Agrego a mi lista creada los objetos edad
	lista_personas.append(persona.obtenerEdad())
#creo una nueva variable donde llamo a la función y envió la lista
merge_sort_result = merge_sort(lista_personas)
print("Lista ordenada\n")
#Realizo la impresión
for i in merge_sort_result:
	
	print("Edad:%d"%(i))
#Cierro el archivo
m.cerrar_archivo()