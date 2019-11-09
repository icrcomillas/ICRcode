import time
import RPi.GPIO as GPIO


class Sensor():

    def __init__(self, pines, sensibilidad):
        GPIO.setmode(GPIO.BOARD)
        self.pin_control_sensor = pines

        "Declaración de variables"
        self.tiempos = []
		self.negros = []
		self.sensibilidad = sensibilidad
        self.sensor_out = []

    def evaluar_sensor_IR(self):
        "Cada vez que se ejecuta muestra la salida de los pines"
        for pin in range(len(self.pin_control_sensor)):
            self.sensor_out[pin] = GPIO.input(self.pin_control_sensor[pin])

    def leer_sensor_IR(self):
        self.sensor_out = [-1, -1, -1, -1, -1, -1, -1, -1]
        "Se ejecuta hasta que se termina de leer los 8 IR"
        while -1 in self.sensor_out:
            self.evaluar_sensor_IR()

	def carga():

		"Definir pines de control como salida para ponerlos a 3.3v"
        for pin in self.pin_control_sensor:
            GPIO.setup(pin, GPIO.OUT)

        "Poner a 3.3v los pines"
        for pin in self.pin_control_sensor:
            GPIO.output(pin, GPIO.HIGH)

        "Espera a la carga del condensador"
        time.sleep(0.05)


    def lecturaTiempos(self):
		"Carga"
		self.carga()

		"Descarga"

		 "Guarda el tiempo en el que se ha activado el sensor"
         self.tiempo_inicio_medida = time.time()

         "Definir como entrada y comienzo de la descarga"
         for pin in self.pin_control_sensor:
             GPIO.setup(pin, GPIO.IN)

        "Estudio de la descarga"
		self.tiempos=[-1, -1, -1, -1, -1, -1, -1, -1]
		while -1 in self.tiempos:
			self.leer_sensor_IR()
			for i in self.sensor_out:
				if self.sensor_out[i]==0 and self.tiempos[i]==-1:
					self.tiempos[i]=(time.time()-self.tiempo_inicio_medida)*1000

	def lecturaNegro():
		self.lecturaTiempos()
		for tiempo in self.tiempos:
			self.negros.append(tiempo/self.sensibilidad)






pin_control_sensor = (7, 11, 13, 15, 12, 16, 18, 22)
sensibilidad=1
sensor = Sensor(pin_control_sensor, sensibilidad)
sensor.lecturaNegro()
salida = sensor.tiempos

print(salida)
