import servo
import acelerometro


def kinect_2d(x,y): #x e y son las coordenadas del punto al que nos queremos mover en coordenadas cartesianas
                    #la funcion nos devolvera los angulos de los servos de la pierna, EN GRADOS

    x0= 0           #supongamos que el putno 0,0 de la pierna se encuentra en el 0,5
    y0=5
    l1 = 10         #esta es la distancia que mide el muslo (desde la cadera a rodilla)
    l2 = 10         #esta es la distancia que mide desde la rodilla hasta el pie

    #calculamos el vector hasta el punto que queremos movernos
    vx = x-x0
    vy = y-y0
    #calculamos el modulo de dicho vector
    dis = sqrt(vx^2+vy^2)
    #a , b,c son los angulos del muslo, rodilla, y en el de la espinilla con dis (este angulo no nos aporta nada)

    #sabemos que todos los angulos suman 180, y aplicando el teorema del seno
    # se nos queda el siguiente sistema de ecuaciones:
    #a+b+c = 180
    #180-a-b = arcosin((l1*sin(a))/l2)-> b= -arcosin((l1*sin(a))/l2)+180-a
    print("la distancia es:")
    print(dis)
    a = var('a')
    #b  = -math.asin((l1*math.sin(a))/l2)+180-a
    ecuacion =  asin((sin(-asin((l1*sin(a))/l2)+180-a)*l2)/dis)-a
    solucion= nsolve((ecuacion),(a))                       #solo nos va a dar la solucion de a

    return solucion








#creamos un modo de debug para poder arrancar todas las funciones
#sin necesidad de llamar a todo el codigo
from sympy import var,nsolve, sin , asin, sqrt


if '__name__' == '__main__':


    import time
    import mpu6050
    import Adafruit_PCA9685

    direccion_driver = 0x40         #estos dos valores son orientativos, hay que cambiarlos


    #creamos el objeto driver
    driver = Adafruit_PCA9685.PCA9685(addres = direccion_driver)
    #creamos el objeto giroscopio


    print("se ha entrado en el modo debug")
    #esperamos dos segundos
    time.sleep(2)

    NUMERO_SERVOS = 2       #este será el numero de servos que tendremos en nuestro robot
    RANGO_MAXIMO = 20      #este será el angulo maximo al que se moveran los servos
    RANGO_MINIMO = 0        #rango minimo al que se mueven los servos


    #movemos todos los servos, hasta su rango maximo
    for i in range(0,NUMERO_SERVOS):
        for j in range(RANGO_MINIMO, RANGO_MAXIMO):
            servo.mover_servo(i,j)
            time.sleep(0.1)

    print("se han terminado de mover los servos")
