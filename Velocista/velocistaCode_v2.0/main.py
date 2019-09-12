from GestorLecturaIR import GestorLecturaIR
from GestorMotores import GestorMotores
import time
import RPi.GPIO as GPIO  

def setup():
    GPIO.setmode(GPIO.BOARD)
    pass

def loop():
    while True:
        #Leer sensores
        sensor_out_IR = GestorLecturaIR().leer_sensor_IR()
        print(sensor_out_IR)
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
