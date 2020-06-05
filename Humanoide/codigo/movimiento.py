
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
    def moverServo(self,servo,angulo): #ESTA FUNCION SE ENCUENTRA EN PRUEBAS
        if servo > self.numeroservos:
            print("elija un servo que este conectado")
        else:
            if angulo > self.datos_servo[str(servo)]['ang_max'] or angulo < self.datos_servo[str(servo)]['ang_min']:
                print("no se puede mover a ese angulo")
                return 0    #no se ha podido mover ningun servo
            else:

                if self.datos_servo[str(servo)]['driver'] == 1:
                    #en este caso el servo esta en el driver 1

                    pulso = self.calcular_pulso(angulo)
                    pulso = int(pulso)
                    pin = self.datos_servo[str(servo)]['pin']
                    self.driver1.set_pwm(pin,0,pulso)
                    return 1  #significa que se ha movido el driver 1
                elif self.datos_servo[str(servo)]['driver'] == 2:
                    #en este caso el servo esta en el driver 2

                    pulso = self.calcular_pulso(angulo)
                    pulso = int(pulso)
                    pin = self.datos_servo[str(servo)]['pin']
                    self.driver2.set_pwm(pin,0,pulso)
                    return 2       #se ha movido el driver 2
    def calcularPulso(self,ang):
        #definimos la funcion lineal para calcular el pulso
        pulso = 9.166*ang + 450
        return pulso
        #clase referida al equilibrio del robot
