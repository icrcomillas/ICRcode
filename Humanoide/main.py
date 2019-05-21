#antes de empezar tenemos que conectarnos al driver del servo, y al giroscopio
#la informacion de la libreria del driver esta aqui https://github.com/adafruit/Adafruit_Python_PCA9685
#la informacion del giroscopio está aqui https://github.com/Tijndagamer/mpu6050

#importamos la libreria del driver
import Adafruit_PCA9685
#importamos la libreria del giroscopio
import mpu6050
import time
import math #para las operaciones matematicas

#incializamos variables necesarias en nuestro codigo
direccion_driver = 0x40         #estos dos valores son orientativos, hay que cambiarlos
direccion_giroscopio = 0x81
#creamos el objeto driver
driver = Adafruit_PCA9685.PCA9685(addres = direccion_driver)
#creamos el objeto giroscopio
giro = mpu6050(addres = direccion_giroscopio )
#hay que esperar s = direiempre despues de mover un servo, para que se ponga en la posicion
time.sleep(1)
