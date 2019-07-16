"""
	Esta clase es la encargada de gestionar el control de los motores.
	En esta clase se engloba todas las acciones posibles relacionadas con los motores:
		*mover_adelant()
		*girar_izquierda()
		*girar_derecha()
		*reducir_velocidd()

"""

import RPi.GPIO as GPIO

class GestorMotores():

	def __init__(self):

		#definir pines de los motores
		self.pin_motor_izq = 36
		self.pin_motor_der = 38
		self.pin_enable = 40

		GPIO.setup(pin_motor_izq,GPIO.OUT)
		GPIO.setup(pin_motor_der,GPIO.OUT)
		GPIO.setup(pin_enable,GPIO.OUT)
		GPIO.output(pin_motor_izq,GPIO.LOW)
		GPIO.output(pin_motor_der,GPIO.LOW)

		#configurar funcion controladora de los motores
		self.pwm_controlador=GPIO.PWM(pin_controlador,1000)

		#velocidad inicial 0
		pwm_controlador.start(0)

	def mover_adelante(self, potencia):
	"""
		Esta funcion asigna la misma potencia a los dos motores.
		La potencia es configurable mediante el parámetro de entrada de la
		función.

	"""
		pwm_controlador.ChangeDutyCycle(potencia)