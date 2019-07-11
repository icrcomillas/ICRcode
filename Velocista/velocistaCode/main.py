import conexion
from DefinirEstados import  definirEstado
from FuncionalidadEstados import ejecucionEstados

def setup():
	pass	
def loop():
	while True:
		#Leer entrada
		s1,s2 = conexion.read()

		#Evalua en que estado se localiza
		estado=definirEstado(s1,s2)
		#Implementa los estados
		ejecucionEstados(estado)

#Ejecutar las funciones
setup()
loop()
