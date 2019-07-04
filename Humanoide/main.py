#antes de empezar tenemos que conectarnos al driver del servo, y al giroscopio
#la informacion de la libreria del driver esta aqui https://github.com/adafruit/Adafruit_Python_PCA9685
#la informacion del giroscopio está aqui https://github.com/Tijndagamer/mpu6050

#importamos la libreria del driver
import Adafruit_PCA9685
#importamos la libreria del giroscopio
from mpu6050 import mpu6050

import time
#importamos las diferentes funciones de nuestro codigo
from configuracion import robot

if __name__ == '__main__':
    #inicializamos variables necesarias en nuestro codigo
    print("se ha entrado en el modo automatico del robot")

    #creamos el objeto driver
    driver = Adafruit_PCA9685.PCA9685(address = robot.direccion_driver)
    #creamos el objeto giroscopio
    giro = mpu6050(robot.direccion_giroscopio )

    respuesta = input("¿quiere calibrar el giroscopio? (s/n)")
    if respuesta == "s":
        print("coloque el ")
        time.sleep(1)
        giro.zero_mean_calibration()
    else:
        print("no se va a calibrar el dispositivo")


    print("se han inicializado todos los equipos sin problema")




    time.sleep(1)
