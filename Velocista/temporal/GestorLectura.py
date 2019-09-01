"""
    Esta es la clase PROVISIONAL de lectura de los infrarrojos (dos sensores).
    En esta version todavia no esta funcional el array de sensores
"""

import RPi.GPIO as GPIO

class GestorLectura():

    def __init__(self):

        #definir pines de los infrarrojos
        self.ir_derecha = 3
        self.ir_izquierda = 5
        
        GPIO.setup(self.ir_derecha,GPIO.IN)
        GPIO.setup(self.ir_izquierda,GPIO.IN)

    def lectura_sensores(self):
        izquierda = GPIO.input(self.ir_izquierda)
        derecha = GPIO.input(self.ir_derecha)
        retorno = 'fuera'
        
        if izquierda == 0 and derecha == 0:
            retorno = 'recto'
        elif izquierda == 1 and derecha == 0:
            retorno = 'izquierda'
        elif izquierda == 0 and derecha == 1:
            retorno = 'derecha'
            
        return retorno