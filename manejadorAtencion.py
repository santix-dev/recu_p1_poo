import csv
from atencion import atencion
class manejadorAtencion(object):
	"""docstring for manejadorAtencion"""
	def __init__(self):
		self.__lista=[]
	def cargar(self, archivo="atenciones.csv"):
		archivo=open(archivo)
		reader=csv.reader(archivo,delimiter=";")
		i=0
		next(reader)
		for fila in reader:
			self.__lista.append(atencion(fila[0],fila[1],fila[2],fila[3],fila[4]))
	def atencionesRealizadas(self,fecha,entidad,manAfiliados):
		print(f"Atenciones    fecha:{fecha}")
		print(f"DNI      Nombre         importe")
		total=0
		for atencion in self.__lista:
			if atencion.fecha()==fecha and atencion.entidad()==entidad:
				dni=atencion.dni()
				sub=atencion.importeCobertura()
				total+=sub
				print(f"{dni}   {manAfiliados.nomAfiliado(dni)}        {sub}")
		print(f"                      total: {total}        ")
	def cantAtenciones(self,dni):
		c=0
		for atencion in self.__lista:
			if atencion.dni()==dni:
				c+=1
		print("Cantidad de atenciones: ",c)
	def noAtendido(self,dni):
		i=0
		flag=True
		while flag and i<len(self.__lista):
			if self.__lista[i].dni()==dni:
				flag=False
			else:
				i+=1
		return flag
