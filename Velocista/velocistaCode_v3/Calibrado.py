from LecturaIR import Sensor
import time
import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BOARD)
    pin_control_sensor = (7, 11, 13, 15, 12, 16, 18, 22)
	sensor = Sensor(pin_control_sensor,sensibilidad)
    pass

def loop():
    while True:
        #Leer sensores
		sensor.descarga()
		salida = sensor.tiemposPin
        time.sleep(1)

setup()
loop()
