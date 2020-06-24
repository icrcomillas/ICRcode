#antes de empezar tenemos que conectarnos al driver del servo, y al giroscopio
#la informacion de la libreria del driver esta aqui https://github.com/adafruit/Adafruit_Python_PCA9685
#la informacion del giroscopio está aqui https://github.com/Tijndagamer/mpu6050
import time
import rospy
#importamos las diferentes funciones de nuestro codigo
 
 
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
       #se inicializa el objeto y se crea el objeto para el movimento
       servos = Servos(DIRECCION_DRIVER1, DIRECCION_DRIVER2,NUMERO_SERVOS)
    def listener():
    def llamadaComunicacion():

if __name__ == '__main__':
    #creamos el objeto robot

    robot = robot()
    respuesta = input("¿estamos en la feria de asociaciones? (s/n)")
    if respuesta == "s":
         #solo se va a utilizar el driver 1
        print("se ha entrado en el modo automatico del robot")
        print("se van a mover los servos de los brazos automaticamente")
        while True:
            #los servos de las manos, serán el 1 y 2, se mueven 180 grados los dos
            robot.mover_servo(0,0)
            robot.mover_servo(1,0)
            time.sleep(1)
            robot.mover_servo(0,180)
            robot.mover_servo(1,180)
            time.sleep(1)
            robot.mover_servo(0,90)
            robot.mover_servo(1,90)
            time.sleep(1)
            #los servos del hombro serán el 2 y el 3
            robot.mover_servo(2,180)
            robot.mover_servo(3,180)
            time.sleep(1)
            robot.mover_servo(2,0)
            robot.mover_servo(3,0)
            time.sleep(1)
            robot.mover_servo(2,90)
            robot.mover_servo(3,90)
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
