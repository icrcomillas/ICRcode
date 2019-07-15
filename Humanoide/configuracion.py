"""este fichero se va a utilizar como fichero de configuracion para todo el robot
en el se ponen todos los parametros que importan del robot, como por ejemplo rango_maximo.
Se puede llamar desde cualquier parte del codigo"""

import import Adafruit_PCA9685
from mpu6050 import mpu6050

class robot:
    def __init__(self,direccion_driver1, direccion_driver2,direccion_giroscopio):
        #se inicializan los objetos de los drivers, y del giroscopio
        driver1 = PCA9685(addres = direccion_driver1)
        driver2 = PCA9685(addres = direccion_driver1)
        giroscopio = mpu6050(direccion_giroscopio)

        self.rango_maximo = 600
        self.rango_minimo = 150
        self.numero_servos = 20
        self.angulo_maximo = 180
        self.angulo_minimo = 0
        self.numero_servos_driver = 13 #este es el numero de servos por dirver, empezando desde el 0

        """
        self.direccion_driver1 = direccion_driver1  #esta es la direccion default (0x40), si hiciera falta cambiarla, se hace en fisico
        self.direccion_driver2 = direccion_driver2
        self.direccion_giroscopio = direccion_giroscopio
        """
    def calcular_pulso(ang):
        #definimos la funcion lineal para calcular el pulso
        pulso = 9.166*ang + 450
        return pulso
    def mover_servo(self,servo, angulo):
        if servo > self.numero_servos:
            print("elija un servo que este conectado")
        else:
            if angulo > self.angulo_maximo or angulo < self.angulo_minimo:
                print("no se puede mover a ese angulo")
            else:
                pulso = calcular_pulso(angulo)
                pulso = int(pulso)
                if servo < self.numero_servos_driver:
                    #en este caso el servo esta en el driver 1
                    driver1.set_pwm(servo,0,pulso)
                elif servo > self.numero_servos_driver:
                    #el servo esta en el driver 2
                    servo = servo - self.numero_servos_driver
                    driver2.set_pwm(pulso)
        return

    def calibrar_giroscopio():
        giroscopio.zero_mean_calibration()
        print("se ha calibrado el giroscopio")
        return

   def acel_giro():
       aceleracion = giroscopio.get_accel_data() #leemos todas las aceleraciones del giroscopio

       x = aceleracion['x']
       y = aceleracion['y']
       z = aceleracion['z']

       return x, y,z       # los valores x , y , z son las aceleraciones en sus respectivos ejes

   def pos_giro():

       inclinacion = giroscopio.get_gyro_data()

       x = inclinacion['x']
       y = inclinacion['y']
       z = inclinacion['z']

       return x, y ,z
