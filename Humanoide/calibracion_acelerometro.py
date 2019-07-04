#este codigo es para calibrar el acelerometro.
#si no se obtienen resultados muy poco precisos

from mpu6050 import mpu6050
from configuracion import robot

#creamos el objeto del acelerometro

acelerometro = mpu6050(robot.direccion_giroscopio)

acelerometro.zero_mean_calibration()

print("se ha terminado el codigo")
