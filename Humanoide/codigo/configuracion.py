"""este fichero se va a utilizar como fichero de configuracion para todo el robot.
Se puede llamar desde cualquier parte del codigo"""

import Adafruit_PCA9685
from mpu6050 import mpu6050
#modulo para la comunicacion
import socket
#se utiliza la libreria json para obtener la informacion de cada servo de forma fiable e individualizada
import json

#clase que define el comportamiento de todo robot
class Robot():
    def __init__(self):
        return 
    def moverDelante(self):
        return 
    def moverAtras(self):
        return 
    def cargarConfiguracion(self):
        #se abre el fichero json y se carga en una variable
        with open("configuracion.json") as fichero:
            self.datos_servo = json.load(fichero)
        return
  


class Humanoide(Robot):
    def __init__(self):

        #variables de la direccion de los driver y el giroscopio
        self.direccion_driver1 = 0x40
        self.direccion_driver2 = 0x70
        self.direccion_giroscopio = 0x68

        #variables propias del robot
        self.numeroServos = 20
        self.numeroServosDriver = 16 #este es el numero de servos por driver, empezando desde el 0

        #se inicializan los objetos de los drivers, y del giroscopio
        self.driver1 = Adafruit_PCA9685.PCA9685(address = self.direccion_driver1)
        self.driver2 = Adafruit_PCA9685.PCA9685(address = self.direccion_driver2)
        self.giroscopio = mpu6050(self.direccion_giroscopio)

    def moverServo(self,servo, angulo): #ESTA FUNCION SE ENCUENTRA EN PRUEBAS
        if servo > self.numeroservos:
            print("elija un servo que este conectado")
        else:
            if angulo > self.datos_servo[str(servo)]['ang_max'] or angulo < self.datos_servo[str(servo)]['ang_min']:
                print("no se puede mover a ese angulo")
            else:

                if self.datos_servo[str(servo)]['driver'] == 1:
                    #en este caso el servo esta en el driver 1

                    pulso = self.calcular_pulso(angulo)
                    pulso = int(pulso)
                    pin = self.datos_servo[str(servo)]['pin']
                    self.driver1.set_pwm(pin,0,pulso)

                if self.datos_servo[str(servo)]['driver'] == 2:
                    #en este caso el servo esta en el driver 2

                    pulso = self.calcular_pulso(angulo)
                    pulso = int(pulso)
                    pin = self.datos_servo[str(servo)]['pin']
                    self.driver2.set_pwm(pin,0,pulso)
        return
    def calcularPulso(self,ang):
        #definimos la funcion lineal para calcular el pulso
        pulso = 9.166*ang + 450
        return pulso


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
    def toString(self):#devuelve toda la informacion del objeto
        mensaje = + "\n numero de servos: "+ self.numerServos+ "\n numero de servos por driver: "+self.numeroServosDriver
        return super.toString() + mensaje
    def equilibrar(self):
        
        return



