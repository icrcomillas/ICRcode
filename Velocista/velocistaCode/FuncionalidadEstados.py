import conexion
import logica

def ejecucionEstados(estado):
	if estado == avanzar:
		#Ejecutar algoritmo
		m1,m2=logica.avanzar()
		#Enviar señal
		conexion.output(m1,m2)
