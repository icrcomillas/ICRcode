"""este fichero se va a utilizar como fichero de configuracion para todo el robot
en el se ponen todos los parametros que importan del robot, como por ejemplo rango_maximo.
Se puede llamar desde cualquier parte del codigo"""

class robot:
    rango_maximo = 200
    rango_minimo = 150
    numero_servos = 5
    direccion_driver1 = 0x40 #esta es la direccion default, si hiciera falta cambiarla, se hace en fisico
    direccion_driver2 = 0x50
    direccion_giroscopio = 0x60 #este valor hay que cambiarlo
    angulo_maximo = 180
    angulo_minimo = 0
