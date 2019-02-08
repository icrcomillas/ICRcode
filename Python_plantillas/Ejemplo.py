
#Programa principal:
import conexion
import logica

def setup():
	pass
def loop():
	while True:
		# Leer entrada
		s1,s2 = conexion.read()

		# Ejecutar algoritmo
		m1,m2=logica.avanzar(s1,s2)

		# Enviar señal
		conexion.output(m1,m2)

# Ejecutar las funciones
setup()
loop()
