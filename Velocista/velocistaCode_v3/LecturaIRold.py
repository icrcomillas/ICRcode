import time
import RPi.GPIO as GPIO


class Sensor():

    def __init__(self, pines):
        GPIO.setmode(GPIO.BOARD)
        self.pin_control_sensor = pines

        "Declaración de variables"
        self.tiempos = []
        self.valores = [[], [], [], [], [], [], [], []]
"""
     	self.pin1 = []
        self.pin2 = []
        self.pin3 = []
        self.pin4 = []
        self.pin5 = []
        self.pin6 = []
        self.pin7 = []
        self.pin8 = []
"""
        self.tiemposPin = []
        self.sensor_out = []

    def evaluar_sensor_IR(self):
        "Cada vez que se ejecuta muestra la salida de los pines"
        for pin in range(len(self.pin_control_sensor)):
            self.tiempo_transcurrido = time.time() - self.tiempo_inicio_medida  # en segundos
            self.sensor_out[pin] = GPIO.input(self.pin_control_sensor[pin])

    def leer_sensor_IR(self):
        self.sensor_out = [-1, -1, -1, -1, -1, -1, -1, -1]
        "Se ejecuta hasta que se termina de leer los 8 IR"
        while -1 in self.sensor_out:
            self.evaluar_sensor_IR()

    def descarga(self):
		"Carga"

		"Definir pines de control como salida para ponerlos a 3.3v"
        for pin in self.pin_control_sensor:
            GPIO.setup(pin, GPIO.OUT)

        "Poner a 3.3v los pines"
        for pin in self.pin_control_sensor:
            GPIO.output(pin, GPIO.HIGH)

        "Espera a la carga del condensador"
        time.sleep(0.05)

		"Descarga"

		 "Guarda el tiempo en el que se ha activado el sensor"
         self.tiempo_inicio_medida = time.time()

         "Definir como entrada y comienzo de la descarga"
         for pin in self.pin_control_sensor:
             GPIO.setup(pin, GPIO.IN)

        "Estudio de la descarga"
        while self.sensor_out != [0, 0, 0, 0, 0, 0, 0, 0]:
            self.leer_sensor_IR()
            self.tiempos.append(self.tiempo_transcurrido*1000)
			for i in range(8):
	            self.valores[i].append(self.sensor_out[i])
        #     self.pin1.append(self.sensor_out[0])
        #     self.pin2.append(self.sensor_out[1])
        #     self.pin3.append(self.sensor_out[2])
        #     self.pin4.append(self.sensor_out[3])
        #     self.pin5.append(self.sensor_out[4])
        #     self.pin6.append(self.sensor_out[5])
        #     self.pin7.append(self.sensor_out[6])
        #     self.pin8.append(self.sensor_out[7])

        # self.valores = [self.pin1, self.pin2, self.pin3, self.pin4,
        #                 self.pin5, self.pin6, self.pin7, self.pin8]



        for i in range(8):
            for j in range(len(self.tiempos)):
                if self.valores[i][j] == 0 and j != 0:
                    self.tiemposPin.append(
                        (self.tiempos[j]+self.tiempos[j-1])/2)
                    break

# for i in range(8):
#     print(tiemposPin[i])

pin_control_sensor = (7, 11, 13, 15, 12, 16, 18, 22)
sensor = Sensor(pin_control_sensor)
sensor.descarga()
salida = sensor.tiemposPin

#PRUEBA RASPBERRY GITHUB
