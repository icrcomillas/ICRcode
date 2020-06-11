from movimiento import Servos
from equilibrio import Equilibrio
import rospy
from msg import mensajeRaul
from ros.msg import teleop

class Control():        #clase encargada de controlar todo lo referido al movimiento del robot
    def __init__(self):
        #QUEDA POR HACER HASTA IMPLEMENTAR ROS
        DIRECCION_DRIVER1 = 0X70        #A REVISAR, BUSCAR FORMA DE CARGARLOS DESDE JSON
        DIRECCION_DRIVER2 = 0X68
        NUMERO_SERVOS = 20
     
    def equilibrar(self):
        #hay que equilibrar tanto en la direccion alante atras, izquierda derecha
        alante_atras = Equilibrio(0)        #en ambos casos se busca que el angulo de inclinacion sea de 0 grados
        derecha_izquierda = Equilibrio(0)
        while True:
            prediccionAA = alante_atras.predecir()
            prediccionDI = derecha_izquierda.predecir()

    def servoAngTransform(self,direccion)
        #funcion encargada de transformar la prediccion en un angulo del los servos


