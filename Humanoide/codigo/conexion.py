import socket
import json
import rospy
from std_msg.msg import Int8

class Conectable:
    #clase que no tiene un cosntructor
    #define el comportamiento que todo objeto de tipo conectable tiene que tener
    def __init__(self, ip, puerto):
        #crea el objeto servidor, de tipo socket
        self.conexion= socket.socket()
        self.ip = ip
        self.puerto = puerto

        return 
    def enviarMensaje(self,mensaje):
        self.conexion.send(mensaje.encode())

        print("se ha enviado el siguiente mensaje: "+ mensaje)
        return
    def conectar(self):
        #se deja el método vacio para que luego sean los diferentes objetos los que lo machaquen
        return
    def cerrarConexion(self):
        self.conexion.close()
        return 

    
class Servidor(Conectable):
    def __init__(self,ip,puerto):
        super().__init__(ip,puerto)
    def conectar(self):
        try:           
            #hace que el socket sea visible desde fuera de la maquina
            self.conexion.bind((self.ip,self.puerto))
          
            #define el socket como un servidor
            self.conexion.listen(5)

        except:
            print("no se ha podido crear el servidor")
            return False
     
    def aceptar(self):

        #acepta conexiones nuevas de usuarios
        self.conexion.listen()
        #deja el programa enganchado hasta que encuentra a algun usuario que se quiera conectar
        self.cliente,addres = self.conexion.accept()
        
        print("se ha conectado un cliente desde la direccion: ",addres)
      
        mensajeConfirmacion = "Conexion ok"
        self.cliente.send(mensajeConfirmacion.encode())

        return self.cliente,addres
    def recibirMensaje(self):
        mensaje = self.cliente.recv(1024).decode()          #en el caso del servidor envia los datos y recibe de cada objeto independientemente
        if mensaje == "cerrar":
            super.cerrarConexion()
        return mensaje
    def servidor(self):                     #esta va a ser la funcion que llama ros para poder ejecutar toda la rutina de comunicacion
        publisher = rospy.Publisher('recibidos',Int8)   #se establece el topic en el que se va a publicar
        rospy.init_node('Conexion', anonymous=True)     #se inicializa el nodo
        rate = rospy.Rate(10)               # 10hz
        conectado = False                   # se le asigna inicialmente el valor a falso, de forma que entre en el bucle
        while not rospy.is_shutdown():      #queda implementar condicion para comprobar si el cliente sigue conectado
            if conectado == False:
                self.aceptar()              #en el caso de que no se tenga conectado ningun cliente, el servidor trata de aceptar a otro 
                conectado = True
            else:                           #en el caso de que ya tenga un cliente conectado
                mensaje = self.recibirMensaje()
                rospy.loginfo(mensaje+"%"+rospy.get_time())
                publisher.publish(mensaje)  #se publica el mensaje en el topic
                rate.sleep()

class Cliente(Conectable):
    def __init__(self,ip,puerto):
        super().__init__(ip,puerto)
    def conectar(self):
        self.conexion.connect((self.ip,self.puerto))
        while True:
            mensajeVuelta = self.conexion.recibirMensaje()        #espera a recibir un mensaje de confirmacion
            if mensajeVuelta == "Conexion ok":
                print("Conexion realizada de forma correcta")
            else:
                print("Conexion fallida")
            break
        return
    def enviarMensaje(self,mensaje):    #en el caso del cliente hay que hacer un override la funcion enviar mensaje, ya qye servidor elige un canal determinado y clietne lo envia por conexion
        self.conexion.send(mensaje.encode())
        return
    def recibirMensaje(self):
        return self.conexion.recv(1024).decode()         #en el caso del cliente se recibe el objeto que se conecta 
    def cerrarConexion(self):
        self.enviarMensaje("cerrar")
        super().cerrarConexion()
        return 
if __name__=='__main__':
    #se crea el objeto para la conexion
    with open('servos.json') as ficheroConfiguracion:       #se carga la direccion ip y el puerto de conexion de un fichero json
            datos = json.load(ficheroConfiguracion)
    conexion = Cliente(datos["direccionIp"]["Ip"],datos["direccionIp"]["puerto"])
    try:
        conexion.servidor()
    except rospy.ROSInterruptException:
        rospy.loginfo("se ha producido un error a la hora de conectarse con el ordenador")
