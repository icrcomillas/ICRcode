import json
import rospy
from std_msg.msg import Int8MultiArray

from movimiento import Servos
from equilibrio import Equilibrio

tipos_movimientos = {"adelante" : 1, "derecha" : 2, "atras" : 3, "izquierda" : 4, "ataque" : 5, "defender" : 6}

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

    # def servoAngTransform(self,direccion):
        #funcion encargada de transformar la prediccion en un angulo del los servos

    def callback(self, data):
        if data[0] < 10:    #Si la instruccion es de movimineto, del diccionario sacamos los angulos pertinentes
            self.instruccion_servos = self.posibles_movimientos[data[0]]
        else:
            # Como queremos mover un solo servo, restamos 10 y sacamos cual y en la segunda posicion de data tenemos el angulo
            self.instruccion_servos[(data[0]-10)] = data[1]
        arrayPublicado = Int8MultiArray(self.instruccion_servos)    #Preparacion para mandar el array
        self.publisher.publish(arrayPublicado)   #publicamos el array
        
    def listener(self):
        rospy.Subscriber("recibidos", Int8MultiArray, self.callback)
        rospy.loginfo("Control Subscribers set")

        self.publisher = rospy.Publisher("angulos",Int8MultiArray)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

if __name__ == '__main__':
    # Leemos el JSON y lo pasamos a un diccionario "más bonito" con el codigo de movimiento
    # como clave y de valor un array con el valor de los angulos de los servos
    with open('control.json') as control:
        self.control = json.load(control)
    for key in control.keys():
        servos = []
        for value in control[key].values():
            servos.append(value) 
        self.posibles_movimientos[tipos_movimientos[key]] = servos
    
    control = Control()
    rospy.init_node('Control', anonymous=True)
    control.listener()