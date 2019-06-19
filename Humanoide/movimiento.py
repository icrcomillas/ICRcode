import time
import Adafruit_PCA9685
import servo
from configuracion import robot


def andar_delante():
    #codigo de la funcion para andar hacia delante
    print("hola mundo")
def andar_detras():
    #codigo para andar hacia detras
    print("hola mundo")
def girar():
    #codigo para girar
    print("hola mundo")
def ataque():
    #codigo de ataque
    print("hola mundo")
def defensa():
    #codigo de defensa
    print("hola mundo")





if __name__ == '__main__':
    #creamos el objeto driver
    driver = Adafruit_PCA9685.PCA9685(addres = robot.direccion_driver1)
    print("se ha entrado en el modo debug")
    #esperamos dos segundos
    time.sleep(2)
    print("se van a mover los servos")
    #movemos todos los servos, hasta su rango maximo
    for i in range(0,robot.numero_servos-1):
        for j in range(robot.angulo_minimo, robot.angulo_maximo):
            #print("se ha movido el servo "+str(i)+" a la posicion "+ str(j))
            servo.mover_servo(i,j)
            time.sleep(0.1)

    print("se han terminado de mover los servos")
