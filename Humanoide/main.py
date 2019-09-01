#antes de empezar tenemos que conectarnos al driver del servo, y al giroscopio
#la informacion de la libreria del driver esta aqui https://github.com/adafruit/Adafruit_Python_PCA9685
#la informacion del giroscopio está aqui https://github.com/Tijndagamer/mpu6050

from configuracion import robot
import time
#importamos las diferentes funciones de nuestro codigo


if __name__ == '__main__':
    #inicializamos variables necesarias en nuestro codigo
    robot = robot()
    print("se ha entrado en el modo automatico del robot")

    #creamos el objeto robot


    respuesta = input("¿quiere calibrar el giroscopio? (s/n)")
    if respuesta == "s":
        print("coloque el ")
        time.sleep(1)
        robot.calibrar_giroscopio()
    else:
        print("no se va a calibrar el dispositivo")


    print("se han inicializado todos los equipos sin problema")




    time.sleep(1)
