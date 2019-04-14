#antes de empezar tenemos que conectarnos al driver del servo, y al giroscopio
#la informacion de la libreria del driver esta aqui https://github.com/adafruit/Adafruit_Python_PCA9685
#llamamos al fichero de funciones
import funciones
#importamos la libreria del driver
import Adafruit_PCA9685
import time


#incializamos variables necesarias en nuestro codigo
direccion_driver = 0x41

#creamos el objeto driver
driver = Adafruit_PCA9685.PCA9685(addres = direccion_driver)
funciones.mover_servo(n_servo = 4, posicion = 200)
#hay que esperar siempre despues de mover un servo, para que se ponga en la posicion
time.sleep(1)
