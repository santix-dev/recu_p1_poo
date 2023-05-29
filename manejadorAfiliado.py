import csv
from afiliado import afiliado
class manejadorAfiliado(object):
	"""docstring for manejador1"""
	def __init__(self):
		self.__lista=[]
	def cargar(self, archivo="afiliados.csv"):
		archivo=open(archivo)
		reader=csv.reader(archivo,delimiter=";")
		i=0
		next(reader)
		for fila in reader:
			self.__lista.append(afiliado(fila[0],fila[1],fila[2]))
	def nomAfiliado(self,dni):
		i=0
		flag=False
		while not flag and i<len(self.__lista):
			if self.__lista[i].dni()==dni:
				nom=self.__lista[i].nombre()
				flag=True
			else:
				i+=1
		return nom
	def listarOrdenado(self):
		self.__lista.sort()
		for afiliado in self.__lista:
			print(afiliado)
	def listarNoAtendidos(self,manAtenciones):
		print("no se atendieron:")
		for afiliado in self.__lista:
			if manAtenciones.noAtendido(afiliado.dni()):
				print(afiliado.nombre())