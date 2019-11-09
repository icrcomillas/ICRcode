from LecturaIR import Sensor
import time
import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BOARD)
    pin_control_sensor = (7, 11, 13, 15, 12, 16, 18, 22)
	sensibilidad = 1
	sensor = Sensor(pin_control_sensor, sensibilidad)
    pass

def loop():
    while True:
        #Leer sensores
		sensor.descarga()
		salida = sensor.tiemposPin
        time.sleep(1)
        #Implementa los estados
        """ *esperaInicio
            *moverAdelante
            *cambiarCarril
        """

        """
            estado=gestor_entorno.get_estado()
            if estado == "esperaInicio" :
                time.sleep(5)
                estado=="moverAdelante"

            #actualizo el estado
            gestorEntorno.set_estado(estado)
        """

        #cargar salidas
        #GestorMotores().mover_adelante(75)

#Ejecutar las funciones
setup()
loop()
