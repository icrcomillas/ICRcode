from time import time
import RPi.GPIO as GPIO

#pines a los que se conecta los 8 pines de control del sensor de IR
pin_control_sensor=(7,11,13,15,12,16,18,22)

class GestorLecturaIR():

    def __init__(self):
        #definir pines de control como salida para ponerlos a 3.3v
        for pin in pin_control_sensor:
            GPIO.setup(pin,GPIO.OUT)
        #poner a 3.3v los pines
        for pin in pin_control_sensor:
            GPIO.output(pin,GPIO.HIGH)

		#espera a la carga del condensador
		sleep(0.005)

        #guarda el tiempo en el que se ha activado el sensor
        self.tiempo_inicio_medida=time()

        #definir como entrada y comienzo de la descarga
        for pin in pin_control_sensor:
            GPIO.setup(pin,GPIO.IN)

        """
           sensor_out es la salida del sensor interpretada. Contiene un valor de 0 a 100
           en función de la oscuridad que detecta el senso. Si contiene 100 será
           que el sensor ha detectado 100% negro.

        """
        self.sensor_out=[-1,-1,-1,-1,-1,-1,-1,-1]

    def evaluar_sensor_IR(self):
    #Cada vez que se ejcuta muestra la salida de los pines
        for pin in range(len(pin_control_sensor)):
			tiempo_transcurrido=time() - self.tiempo_inicio_medida #en segundos
            self.sensor_out[pin]=GPIO.input(pin_control_sensor[pin])

    def leer_sensor_IR(self):

       #Se ejecuta hasta que se termina de leer los 8 IR
        while -1 in self.sensor_out:
            self.evaluar_sensor_IR()

        return (tiempo_transcurrido, self.sensor_out)

for i in range(1000):
	(tiempo_transcurrido, sensor_out)=leer_sensor_IR
	print("t= " + tiempo_transcurrido + ": " + sensor_out)
