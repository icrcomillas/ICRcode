import socket
class Conectable:
    #clase que no tiene un cosntructor
    #define el comportamiento que todo objeto de tipo conectable tiene que tener
    def __init__(self, ip, puerto):
        #crea el objeto servidor, de tipo socket
        self.conexion= socket.socket()
        self.ip = ip
        self.puerto = puerto

        return 

    def recibirMensaje(self):
        mensaje = self.conexion.recv(self.puerto)
        #hay que decodificar el mensaje recivido
        mensaje = mensaje.decode()

        return mensaje


    def enviarMensaje(self,mensaje):
        self.conectado.send(mensaje.encode())

        print("se ha enviado el siguiente mensaje: "+ mensaje)
        return
    def conectar(self):
        #se deja el método vacio para que luego sean los diferentes objetos los que lo machaquen
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
        finally:
            
            print("se ha creado el servidor")
            return True

    def aceptar(self):

        #acepta conexiones nuevas de usuarios
        self.listen()
        #deja el programa engancxhado hasta que encuentra a algun usuario que se quiera conectar
        self.cliente,addres = self.conexion.accept()
        
        print("se ha conectado un cliente desde la direccion: ",addres)
        super().EnviarMensaje("Conexion ok")

        return self.cliente,addres
    def cerrarConexion(self):
        self.conexion.close()

class Cliente(Conectable):
    def __init__(self,ip,puerto):
        super().__init__(ip,puerto)
    def Conectar(self):
        self.conexion.connect((self.ip,self.puerto))
        return
    def EnviarMensaje(self,mensaje):    #en el caso del cliente hay que hacer un override la funcion enviar mensaje, ya qye servidor elige un canal determinado y clietne lo envia por conexion
        self.conexion.send(mensaje)
        return

if __name__=='__main__':
    respuesta = input("cliente o servidor\n")
    if respuesta == "servidor":
        print("modo servidor")
        servidor = Servidor('192.168.1.40',65432)
        servidor.conectar()
        servidor.aceptar()
        while True:
            servidor.recibirMensaje()
    elif respuesta == "cliente":
        print("modo cliente")
        cliente = Cliente()
        cliente.conectar('192.168.1.40',65432)
        while True:
            mensaje = input("que quieres enviar")
            cliente.enviarMensaje(mensaje)