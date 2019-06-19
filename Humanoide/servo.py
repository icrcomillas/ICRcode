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

    if angulo > robot.angulo_maximo or angulo < robot.angulo_minimo:
        print("no se puede mover ese rango, esta fuera del alcance")
    elif angulo <= robot.angulo_maximo and angulo >= robot.angulo_minimo:

        pulso = calcular_pulso(angulo)
        pulso = int(pulso)
        driver.set_pwm(n_servo, 0, 600)
        print("se ha movido el servo "+str(n_servo)+" a la posicion "+str(angulo))
    return

if __name__ == '__main__':
    print("se ha entrado en el modo debug")
    while True:
        servo = input("que servo quieres mover")
        servo = int(servo)
        angulo = input("¿a que angulo lo quieres mover?")
        angulo = float(angulo) #aqui se convierte el numero de entrada a un tipo float, si no da error
        mover_servo(servo,angulo)
        time.sleep(0.1)
