
import Adafruit_PCA9685
import json


class Servos():
    def __init__(self,DireccionDriver1,DireccionDriver2,NumeroServos):
        #se crean los dos drivers
        self.driver1 = Adafruit_PCA9685.PCA9685(address = DireccionDriver1)
        self.driver2 = Adafruit_PCA9685.PCA9685(address = DireccionDriver2)
        #se lee el fichero en el que se almacena toda la informacion de los servos
        with open('servos.json') as f:
            self.datos = json.load(f)
        self.insertarValoresServos(NumeroServos)

    def insertarValoresServos(self,NumeroServos):#funcion para llamar a 'configuracion.json' y cargar de cada driver su direccion y numero de servos
        for servo in range(0, NumeroServos):
            moverServo(servo,self.datos[str(servo)]['default'])

    def calcularPulso(self,ang):
        #definimos la funcion lineal para calcular el pulso
        pulso = 9.166*ang + 450
        return pulso

    def moverServo(self,n_servo,angulo):
        pulso = self.calcular_pulso(angulo)
        pulso = int(pulso)
        if angulo < datos[str(n_servo)]['ang_max'] and angulo > datos[str(n_servo)]['ang_min']:
            if self.datos[str(n_servo)]['driver'] == 1:
                driver1.set_pwm(self.datos[str(n_servo)]['pin'], 0, pulso)
                return 1
            elif self.datos[str(n_servo)]['driver'] == 2:
                driver2.set_pwm(self.datos[str(n_servo)]['pin'],0,pulso)
                return 2
        else:
            return 0
    
