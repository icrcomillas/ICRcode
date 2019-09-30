#antes de empezar tenemos que conectarnos al driver del servo, y al giroscopio
#la informacion de la libreria del driver esta aqui https://github.com/adafruit/Adafruit_Python_PCA9685
#la informacion del giroscopio está aqui https://github.com/Tijndagamer/mpu6050

from configuracion import robot
import time
#importamos las diferentes funciones de nuestro codigo



if __name__ == '__main__':
    #creamos el objeto robot

    robot = robot()
    respeusta = input("¿estamos en la feria de asociaciones? (s/n)")
    if respuesta == "s":
         #solo se va a utilizar el driver 1
        print("se ha entrado en el modo automatico del robot")
        print("se van a mover los servos de los brazos automaticamente")
        while True:
            #los servos de las manos, serán el 1 y 2, se mueven 180 grados los dos
            robot.mover_servo(1,0)
            robot.mover_servo(2,0)
            time.sleep(1)
            robot.mover_servo(1,180)
            robot.mover_servo(2,180)
            time.sleep(1)
            robot.mover_servo(1,90)
            robot.mover_servo(2,90)
            time.sleep(1)
            #los servos de los hombros serán el 5 y el 6
            robot.mover_servo(5,0)
            robot.mover_servo(6,0)
            time.sleep(1)
            robot.mover_servo(5,180)
            robot.mover_servo(6,180)
            time.sleep(1)
            robot.mover_servo(5,90)
            robot.mover_servo(6,90)
            time.sleep(1)
            #los servos del codo serán el 3 y el 4
            robot.mover_servo(3,60)
            robot.mover_servo(4,60)
            time.sleep(1)
            robot.mover_servo(3,120)
            robot.mover_servo(4,120)
            time.sleep(1)
            robot.mover_servo(3,90)
            robot.mover_servo(4,90)
            time.sleep(1)

    else:
        respuesta = input("¿quiere calibrar el giroscopio? (s/n)")
        if respuesta == "s":
            print("coloque el ")
            time.sleep(1)
            robot.calibrar_giroscopio()
        else:
            print("no se va a calibrar el dispositivo")


        print("se han inicializado todos los equipos sin problema")




        time.sleep(1)
