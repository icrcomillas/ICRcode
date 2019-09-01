from GestorLectura import GestorLectura
from GestorMotores import GestorMotores
import time
import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BOARD)
    pass

def loop():
    #GestorMotores().cambiar_potencia(15)
    while True:
        #Leer sensores
        sensor_out_IR = GestorLectura().lectura_sensores()
        if sensor_out_IR == 'recto':
            GestorMotores().mover_adelante()
        elif sensor_out_IR == 'izquierda':
            GestorMotores().girar_izquierda()
        elif sensor_out_IR == 'derecha':
            GestorMotores().girar_derecha()
        elif sensor_out_IR == 'fuera':
            GestorMotores().salida_de_pista()
        
        #print(sensor_out_IR)


#Ejecutar las funciones
setup()
loop()

