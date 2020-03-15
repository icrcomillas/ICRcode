"""este fichero se va a utilizar como fichero de configuracion para todo el robot.
Se puede llamar desde cualquier parte del codigo"""

import Adafruit_PCA9685
from mpu6050 import mpu6050 #modulo raspberry PI
#modulo para la comunicacion
import socket
#se utiliza la libreria json para obtener la informacion de cada servo de forma fiable e individualizada
import json
#se importa la libreria servo
from movimiento import Servos

#clase que define el comportamiento de todo robot
class Robot():
    def __init__(self):
        return 
    def moverDelante(self):
        return 
    def moverAtras(self):
        return

class Humanoide(Robot):
    def __init__(self):
        #se inicializan los objetos necesarios para el funcionamiento de 
        self.giroscopio = mpu6050(0x68)
        self.servos = Servos(0x40,0x70)

    def moverServo(self,servo, angulo): #funcion que elige que servo mover
        if servo > self.numeroservos:
            print("elija un servo que este conectado")
        else:
            respuesta = self.servos.moverServo(servo,angulo)
            if respuesta  == 0:
                print("no se ha movido el servo, no es un angulo valido")
        return
    def calibrarGiroscopio(self):
        self.giroscopio.zero_mean_calibration()
        print("se ha calibrado el giroscopio")
        return

    def getAcelGiro(self):
        aceleracion = self.giroscopio.get_accel_data() #leemos todas las aceleraciones del giroscopio

        x = aceleracion['x']
        y = aceleracion['y']
        z = aceleracion['z']

        return x, y,z       # los valores x , y , z son las aceleraciones en sus respectivos ejes

    def getPosGiro(self):

        inclinacion = self.giroscopio.get_gyro_data()

        x = inclinacion['x']
        y = inclinacion['y']
        z = inclinacion['z']

        return x, y ,z
    def __str__(self):#devuelve toda la informacion del objeto # En Python el toString() de java es __str__(self)
        mensaje = + "\n numero de servos: "+ self.numerServos+ "\n numero de servos por driver: "+self.numeroServosDriver
        return super.toString() + mensaje
    def equilibrar(self):
        
        return



