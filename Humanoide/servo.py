from configuracion import robot
import time
import Adafruit_PCA9685

driver = Adafruit_PCA9685.PCA9685(address = robot.direccion_driver1)

def calcular_pulso(ang):
    #definimos la funcion lineal para calcular el pulso
    pulso = 2.77*ang + 150
    return pulso


def mover_servo(n_servo,angulo):
    #posicion la reciviremos en un rango de 0 a 4096

    if angulo > 180 or angulo < 0:
        print("no se puede mover ese rango, esta fuera del alcance")
    elif angulo <= 180 and angulo >= 0:

        pulso = calcular_pulso(angulo)
        driver.set_pwm(n_servo, 0, pulso)
        print("se ha movido el servo "+str(n_servo)+" a la posicion "+str(angulo))
    return

if __name__ == '__main__':
    print("se ha entrado en el modo debug")
    while True:
        servo = input("que servo quieres mover")
        angulo = input("¿a que angulo lo quieres mover?")
        mover_servo(servo,angulo)
        time.sleep(0.1)
