import csv
from clase1 import clase1
class manejador1(object):
	"""docstring for manejador1"""
	def __init__(self):
		self.__lista=[]
	def cargar(self, archivo="archivo.csv"):
		archivo=open(archivo)
		reader=csv.reader(archivo,delimiter=",")
		i=0
		for fila in reader:
			self.__lista.append(clase1(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]))