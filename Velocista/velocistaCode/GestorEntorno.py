"""

	Gestiona las variables de entorno del coche en cada instante.
	Además guarda el estado actual y las salidas.

	Estados definidos de momento:
	*esperaInicio
	*leerIR
	*leerDistancia
	*cambiarVelocidad
	*cambiarCarril
	
"""
class GestorEstado():

	def __init__(self):
		
		#entrada del sensor de IR
		#almacena de 0 a 100 el porcentage de negro
		self.sensorIROut=[-1,-1,-1,-1,-1,-1,-1,-1]

		#entrada sensor distancia. Partimos de un diseño con 3 sensores
		#almacena la distancia en cm
		self.sensorDistancia=[-1,-1,-1]

		#salida potencia motores. Es un valor que va de 0 a 100.
		#un vector que almacena la potencia actual de los dos motores.
		self.pwmMotores=[0,0]

		#estado actual de la maquina de estados.
		#al inicio será  esperaInicio
		self.estado="esperaInicio"

	#las funciones reciven una lista
	def setSensorIROut (self,sensorIROut):
		self.sensorIROut=sensorIROut

	def setSensorDistancia (self,sensorDistancia):
		self.sensorDistancia=sensorDistancia

	def setPwmMotores (self,pwmMotores):
		self.pwmMotores=pwmMotores

	#recive un string
	def setEstado (self,estado):
		self.estado=estado

	
	#las funciones reciven una lista
	def getSensorIROut (self):
		return self.sensorIROut

	def getSensorDistancia (self):
		return self.sensorDistancia

	def getPwmMotores (self):
		return self.pwmMotores

	#recive un string
	def getEstado (self):
		return self.estado
