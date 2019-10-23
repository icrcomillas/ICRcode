"""este fichero se va a utilizar como fichero de configuracion para todo el robot.
Se puede llamar desde cualquier parte del codigo"""

import Adafruit_PCA9685
from mpu6050 import mpu6050
#modulo para la comunicacion
import socket
#se utiliza la libreria json para obtener la informacion de cada servo de forma fiable e individualizada
import json

class robot:
    def __init__(self):

        #variables de la direccion de los driver y el giroscopio
        self.direccion_driver1 = 0x40
        self.direccion_driver2 = 0x70
        self.direccion_giroscopio = 0x68

        #variables propias del robot
        self.numero_servos = 20
        self.numero_servos_driver = 16 #este es el numero de servos por driver, empezando desde el 0

        #se inicializan los objetos de los drivers, y del giroscopio
        self.driver1 = Adafruit_PCA9685.PCA9685(address = self.direccion_driver1)
        self.driver2 = Adafruit_PCA9685.PCA9685(address = self.direccion_driver2)
        self.giroscopio = mpu6050(self.direccion_giroscopio)

        #se abre el fichero json y se carga en una variable
        with open("configuracion.json") as fichero:
            self.datos_servos = json.load(fichero)


    def conexion(self):
        try:
            #crea el objeto servidor, de tipo socket
            self.servidor = socket.socket()
            #hace que el socket sea visible desde fuera de la maquina
            self.servidor.bind(self.servidor.getsockname())
            #define el socket como un servidor
            self.servidor.listen(5)
            respuesta = true
        except:
            respuesta = false
        finally:
            return respuesta

    def aceptar(self):

            #acepta conexiones nuevas de usuarios
        (cliente,addres) = self.server.acept()

        return cliente,addres

    def recivir_mensaje(cliente):
        mensaje = cliente.receive()
        #hay que decodificar el mensaje recivido
        mensaje = mensaje.decode()

        return mensaje


    def enviar_informacion(self,mensaje):

        self.servidor.send(mensaje.encode())

        print("se ha enviado el siguiente mensaje: "+ mensaje)
        return

    def mover_servo(self,servo, angulo):#ESTA FUNCION SE ENCUENTRA EN PRUEBAS
        if servo > self.numero_servos:
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

    def calcular_pulso(self,ang):
        #definimos la funcion lineal para calcular el pulso
        pulso = 9.166*ang + 450
        return pulso


    def calibrar_giroscopio(self):
        self.giroscopio.zero_mean_calibration()
        print("se ha calibrado el giroscopio")
        return

    def acel_giro():
        aceleracion = self.giroscopio.get_accel_data() #leemos todas las aceleraciones del giroscopio

        x = aceleracion['x']
        y = aceleracion['y']
        z = aceleracion['z']

        return x, y,z       # los valores x , y , z son las aceleraciones en sus respectivos ejes

    def pos_giro():

        inclinacion = self.giroscopio.get_gyro_data()

        x = inclinacion['x']
        y = inclinacion['y']
        z = inclinacion['z']

        return x, y ,z
