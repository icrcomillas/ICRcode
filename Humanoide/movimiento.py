import time
import Adafruit_PCA9685
import servo


#direccion_driver = 0x60         #estos dos valores son orientativos, hay que cambiarlos


#creamos el objeto driver
driver = Adafruit_PCA9685.PCA9685(addres = 0x40)



print("se ha entrado en el modo debug")
#esperamos dos segundos
time.sleep(2)

NUMERO_SERVOS = 2       #este será el numero de servos que tendremos en nuestro robot
RANGO_MAXIMO = 20      #este será el angulo maximo al que se moveran los servos
RANGO_MINIMO = 0        #rango minimo al que se mueven los servos

driver.set_pwm(0, 0, 0)
time.sleep(1)
driver.set_pwm(0, 0,90)
#movemos todos los servos, hasta su rango maximo
"""for i in range(0,NUMERO_SERVOS):
    for j in range(RANGO_MINIMO, RANGO_MAXIMO):
        servo.mover_servo(i,j)
        time.sleep(0.1)
"""
print("se han terminado de mover los servos")
