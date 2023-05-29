class afiliado(object):
	"""docstring for afiliado"""
	def __init__(self, dni,nombre,unidad):
		self.__dni = str(dni)
		self.__nya = str(nombre).lower()
		self.__unidad = str(unidad).lower()
	def nombre(self):
		return self.__nya
	def dni(self):
		return self.__dni
	def __lt__(self,otro):
		this=(self.__unidad+" "+self.__nya)
		other=(otro.__unidad+" "+otro.__nya)
		return this<other
	def __str__(self):
		return f"{self.__unidad}   {self.__nya}    {self.__dni}"