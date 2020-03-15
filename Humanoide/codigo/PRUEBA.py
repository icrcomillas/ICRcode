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
  
class Driver(): #clase para crear cada uno de los drivers. Cada driver tendra una direccion y un numero de servos
    def __init__(self,_direccion,_num_servos):
        self.direccion = _direccion
        self.num_servos = _num_servos
    def getDireccion(self):
        return self.direccion
    def getNumServos(self):
        return self.num_servos
    def __str__(self):
        return "Direccion: "+str(self.direccion)+"\t NumeroServos: "+str(self.num_servos)


class Humanoide(Robot):
    def __init__(self):
        self.insertDefault()
        #variables propias del robot
        self.numeroServos = 20
        self.numeroServosDriver = 16 #este es el numero de servos por driver, empezando desde el 0

        #se inicializan los objetos de los drivers, y del giroscopio
        #self.driver1 = Adafruit_PCA9685.PCA9685(address = self.driver1_info.direccion)
        #self.driver2 = Adafruit_PCA9685.PCA9685(address = self.driver2_info.direccion)
        #self.giroscopio = mpu6050(self.direccion_giroscopio)

    def insertDefault(self):
        with open('configuracion.json') as f:
            drivers_dict = json.load(f)

        self.driver1_info = Driver(drivers_dict['driver1']['direccion'],drivers_dict['driver1']['numeroServos'])
        self.driver2_info = Driver(drivers_dict['driver2']['direccion'],drivers_dict['driver2']['numeroServos'])
        self.direccion_giroscopio = drivers_dict['giroscopio']['direccion']

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

if __name__=='__main__':
    miHumanoide = Humanoide()
    print(miHumanoide.driver1_info)
    
    print(miHumanoide.direccion_giroscopio)