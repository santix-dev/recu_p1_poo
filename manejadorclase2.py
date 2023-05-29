import csv
from clase1 import clase1
class manejador2(object):
	"""docstring for manejador2"""
	def __init__(self):
		self.__lista=[]
	def cargar(self, archivo="archivo.csv"):
		archivo=open(archivo)
		reader=csv.reader(archivo,delimiter=",")
		i=0
		for fila in reader:
			self.__lista.append(clase1(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]))
			# if int(fila[0])!=i:
			# 	self.__lista.append(Facultad(fila[0],fila[1],fila[2],fila[3],fila[4]))
			# 	i=int(fila[0])
			# else:
			# 	self.__lista[i-1].agregarCarrera(fila[1],fila[2],fila[3],fila[4],fila[5])
