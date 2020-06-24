from simple_pid import PID
class Equilibrio():     #clase encargada del equilibrio del robot https://github.com/m-lundberg/simple-pid
    def __init_(self,objetivo):
        #se cargan los valores iniciales
        P = 1
        I = 0.1
        D =  0.05

        self.pid = PID(P,I,D)
    def predecir(self,angulo):        #funcion que se va a encargar de predecir el estado futuro de los servos para equilibrar
        prediccion = self.pid(angulo)
        return prediccion