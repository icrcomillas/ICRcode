   
class Conectable:
    #clase que no tiene un cosntructor
    #define el comportamiento que todo objeto de tipo conectable tiene que tener
    def __init__(self, ip, puerto):
        #crea el objeto servidor, de tipo socket
        self.conexion= socket.socket()
        self.ip = ip
        self.puerto = puerto

        return 

    def RecibirMensaje(self):
        mensaje = self.conexion.recv(self.puerto)
        #hay que decodificar el mensaje recivido
        mensaje = mensaje.decode()

        return mensaje


    def EnviarMensaje(self,mensaje):

        self.conectado.send(mensaje.encode())

        print("se ha enviado el siguiente mensaje: "+ mensaje)
        return
    def Conectar(self):
        #se deja el método vacio para que luego sean los diferentes objetos los que lo machaquen
        return

    
class Servidor(Conectable):
    def __init__(self,ip,puerto):
        super().__init__(ip,puerto)
    def Conectar(self):
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

    def Aceptar(self):

            #acepta conexiones nuevas de usuarios
        
        self.cliente,addres = self.conexion.accept()
        print("se ha conectado un cliente desde la direccion: ",addres)
        super().EnviarMensaje("Conexion ok")

        return self.cliente,addres
    def CerrarConexion(self):
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