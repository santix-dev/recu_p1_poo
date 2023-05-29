class atencion(object):
	"""docstring for atencion"""
	def __init__(self, dni,fecha,importe,entidad,porc):
		self.__dni = str(dni)
		self.__fecha = str(fecha)
		self.__importe = float(importe)
		self.__entidad = str(entidad).lower()
		self.__porc_cobertura = float(porc)
	def dni(self):
		return self.__dni
	def fecha(self):
		return self.__fecha
	def entidad(self):
		return self.__entidad
	def importe(self):
		return self.__importe
	def importeCobertura(self):
		return self.__importe-(self.__importe*(self.__porc_cobertura/100))