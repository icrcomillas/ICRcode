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
        #deja el programa engancxhado hasta que encuentra a algun usuario que se quiera conectar
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

class Cliente(Conectable):
    def __init__(self,ip,puerto):
        super().__init__(ip,puerto)
    def conectar(self):
        self.conexion.connect((self.ip,self.puerto))
        while True:
            mensajeVuelta = cliente.recibirMensaje()        #espera a recibir un mensaje de confirmacion
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
    respuesta = input("cliente o servidor\n")
    if respuesta == "servidor":
        print("modo servidor")
        servidor = Servidor('192.168.1.25',65432)
        servidor.conectar()
        servidor.aceptar()
        while True:
            mensajeVuelta = servidor.recibirMensaje()
            print(mensajeVuelta)
    elif respuesta == "cliente":
        print("modo cliente")
        cliente = Cliente('192.168.1.25',65432)
        cliente.conectar()
        while True:
            mensaje = input("que quieres enviar, o cerrar\n")
            if mensaje == "cerrar":
                cliente.cerrarConexion()
            else:
                cliente.enviarMensaje(mensaje)