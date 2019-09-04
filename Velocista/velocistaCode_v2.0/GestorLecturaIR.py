"""
La finalidad de esta clase es gestionar la lectura del sensor de IR.
Como atributos tiene:
 	*El tiempo de inicio de la medida (timpo_inicio_medida). Este tiempo
 	se asigna al instanciar la clase, es decir que la medida se inicializa 
 	al crear la clase. 
"""


from time import time
import RPi.GPIO as GPIO

#pines a los que se conecta los 8 pines de control del sensor de IR
pin_control_sensor=(1,2,3,4,5,6,7,8)

#tiempo en ms que equivale al 100% de negro
TIEMPO_MAX=3.5

class GestorLecturaIR():

	def __init__(self):
		#definir pines de control como salida para ponerlos a 3.3v
		for pin in pin_control_sensor:
			GPIO.setup(pin,GPIO.OUT)
		#poner a 3.3v los pines
		for pin in pin_control_sensor:
			GPIO.output(pin,GPIO.HIGH)

		#guarda el tiempo en el que se ha activado el sensor
		self.timpo_inicio_medida=time()

		#definir como entrada
		for pin in pin_control_sensor:
			GPIO.setup(pin,GPIO.IN)

		"""
		   sensor_out es la salida del sensor interpretada. Contiene un valor de 0 a 100
		   en función de la oscuridad que detecta el senso. Si contiene 100 será
		   que el sensor ha detectado 100% negro.

		"""
		self.sensor_out=[-1,-1,-1,-1,-1,-1,-1,-1]

		#guarda el estado anterior para comprobar si ha habido un flanco de bajada
		self.estado_anterior=[1,1,1,1,1,1,1,1]

	def evaluar_sensor_IR(self):
		"""
			Cada vez que se ejcuta comprueba si ha habido un flanco de bajada y por lo tanto se puede tomar una medida
		"""
		for pin in pin_control_sensor:
			#detectar si ha habido un flanco de bajada
			if self.estado_anterior[pin]==1 and self.estado_anterior[pin] != GPIO.input[pin]:
				tiempo_transcurrido=time() - timpo_inicio_medida #en segundos
				#normalizar tiempo entre 0 y 100
				tiempo_normalizado=(tiempo_transcurrido*100/TIEMPO_MAX)*100
				self.sensor_out[pin]=tiempo_normalizado

			#actualizar valores de estado_anterior
			self.estado_anterior[pin]=GPIO.input[pin]


	def leer_sensor_IR(self):
		"""
			Se ejecuta hasta que se termina de leer los 8 IR

		"""
		while -1 in self.sensor_out:
			self.evaluar_sensor_IR()

		return self.sensor_out