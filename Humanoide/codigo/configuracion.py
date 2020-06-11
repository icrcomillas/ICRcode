"""este fichero se va a utilizar como fichero de configuracion para todo el robot.
Se puede llamar desde cualquier parte del codigo"""

import Adafruit_PCA9685
from giroscopio  import Giroscopio
#modulo par ale movimiento
from movimiento import Servos 
#modulo para la comunicacion
import socket
#se utiliza la libreria json para obtener la informacion de cada servo de forma fiable e individualizada
import json





