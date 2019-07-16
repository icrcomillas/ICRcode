"""
La finalidad de esta clase es gestionar la lectura del sensor de IR.
Como atributos tiene:
 	*El tiempo de inicio de la medida (timpoInicioMedida). Este tiempo
 	se asigna al instanciar la clase, es decir que la medida se inicializa 
 	al crear la clase. 
"""


from time import time
import RPi.GPIO as GPIO

#pines a los que se conecta los 8 pines de control del sensor de IR
pinControlSensor=(1,2,3,4,5,6,7,8)

#tiempo en ms que equivale al 100% de negro
TIEMPO_MAX=3.5

class GestorLecturaIR():

	def __init__(self):
		#definir pines de control como salida para ponerlos a 3.3v
		for pin in pinControlSensor:
			GPIO.setup(pin,GPIO.OUT)
		#poner a 3.3v los pines
		for pin in pinControlSensor:
			GPIO.output(pin,GPIO.HIGH)

		#guarda el tiempo en el que se ha activado el sensor
		self.timpoInicioMedida=time()

		#definir como entrada
		for pin in pinControlSensor:
			GPIO.setup(pin,GPIO.IN)

		"""
		   sensorOut es la salida del sensor interpretada. Contiene un valor de 0 a 100
		   en función de la oscuridad que detecta el senso. Si contiene 100 será
		   que el sensor ha detectado 100% negro.

		"""
		self.sensorOut=[-1,-1,-1,-1,-1,-1,-1,-1]

		#guarda el estado anterior para comprobar si ha habido un flanco de bajada
		self.estadoAnterior=[1,1,1,1,1,1,1,1]

	def medirSensorIR(self):
	"""
		Cada vez que se ejcuta comprueba si ha habido un flanco de bajada y por lo tanto se puede tomar una medida
	"""
		for pin in pinControlSensor:
			#detectar si ha habido un flanco de bajada
			if self.estadoAnterior(pin)==1 && self.estadoAnterior(pin)!=GPIO.input(pin):
				tiempoTranscurrido=time() - timpoInicioMedida #en segundos

				#normalizar tiempo entre 0 y 100
				tiempoNormalizado=(tiempoTranscurrido*100/TIEMPO_MAX)*100
				self.sensorOut(pin)=tiempoNormalizado

		if -1 in self.sensorOut:
			return -1
		else:
			return self.sensorOut