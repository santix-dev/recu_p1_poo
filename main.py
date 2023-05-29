import csv
from afiliado import afiliado
from atencion import atencion
from manejadorAfiliado import manejadorAfiliado
from manejadorAtencion import manejadorAtencion

if __name__ == '__main__':
	afiliados=manejadorAfiliado()
	atenciones=manejadorAtencion()
	afiliados.cargar()
	atenciones.cargar()
	print("1) mostrar atenciones realizadas en una fecha por una entidad")
	print("2) leer dni y mostrar nombre y cantidad de atenciones")
	print("3) listar afiliados de menor a mayor por unidad y nombre")
	print("4) listar afiliados que no tuvieron ninguna atencion")
	opc=int(input(""))
	while opc!=0:
		match opc:
			case 1:
				fecha="2/4/2023"#input("Ingrese fecha: ")
				entidad="clinica de ojos"#input("Ingrese entidad: ")
				atenciones.atencionesRealizadas(fecha,entidad,afiliados)
			case 2:
				dni=str(input("Ingrese dni: "))	
				print(afiliados.nomAfiliado(dni))
				atenciones.cantAtenciones(dni)
			case 3:
				afiliados.listarOrdenado()
			case 4:
				afiliados.listarNoAtendidos(atenciones)
		print("1) mostrar atenciones realizadas en una fecha por una entidad")
		print("2) leer dni y mostrar nombre y cantidad de atenciones")
		print("3) listar afiliados de menor a mayor por unidad y nombre")
		print("4) listar afiliados que no tuvieron ninguna atencion")
		opc=int(input(""))