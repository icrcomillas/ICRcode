from GestorLecturaIR import GestorLecturaIR
from GestorEntorno import GestorEntorno
import logica
import time

def setup():
	GPIO.setmode(GPIO.BOARD)
	pass

def loop(gestorEntorno):
	while True:
		estado=gestorEntorno.getEstado()
		#Implementa los estados
"""
	*esperaInicio
	*leerIR
	*leerDistancia
	*cambiarVelocidad
	*cambiarCarril
"""		
		if estado == "leerIR" :
			
			time.sleep(5)
			estado=cambiarVelocidad
		#actualizo el estado
		gestorEntorno.setEstado(estado)


#Ejecutar las funciones
setup()
gestorEntorno=GestorEntorno()
loop(gestorEntorno)
