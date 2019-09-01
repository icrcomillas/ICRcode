"""
    Esta clase es la encargada de gestionar el control de los motores.
    En esta clase se engloba todas las acciones posibles relacionadas con los motores:
        *mover_adelante()
        *girar_izquierda()
        *girar_derecha()
        *cambiar_potencia()
        *salida_de_pista()

"""

import RPi.GPIO as GPIO

class GestorMotores():

    def __init__(self):

        #definir pines de los motores
        #MOTOR izda = Motor 1
        self.in1_motor1 = 36
        self.in2_motor1 = 38
        self.enable_motor1 = 40
        #MOTOR der = Motor 2
        self.in1_motor2 = 37
        self.in2_motor2 = 35
        self.enable_motor2 = 33
        
        #Setup motor 1
        GPIO.setup(self.in1_motor1,GPIO.OUT)
        GPIO.setup(self.in2_motor1,GPIO.OUT)
        GPIO.setup(self.enable_motor1,GPIO.OUT)
        GPIO.output(self.in1_motor1,GPIO.LOW)
        GPIO.output(self.in2_motor1,GPIO.LOW)
        #Setup motor 2
        GPIO.setup(self.in1_motor2,GPIO.OUT)
        GPIO.setup(self.in2_motor2,GPIO.OUT)
        GPIO.setup(self.enable_motor2,GPIO.OUT)
        GPIO.output(self.in1_motor2,GPIO.LOW)
        GPIO.output(self.in2_motor2,GPIO.LOW)

        #configurar funcion controladora de los motores
        self.pwm_controlador_motor1 = GPIO.PWM(self.enable_motor1,1000)
        self.pwm_controlador_motor2 = GPIO.PWM(self.enable_motor2,1000)

        #velocidad inicial de ambos motores 0
        self.pwm_controlador_motor1.start(50)
        self.pwm_controlador_motor2.start(50)

    def cambiar_potencia(self, potencia):
        """
            Esta funcion asigna la misma potencia a los dos motores.
            La potencia es configurable mediante el parámetro de entrada de la
            función.

        """
        self.pwm_controlador_motor1.ChangeDutyCycle(potencia)
        self.pwm_controlador_motor2.ChangeDutyCycle(potencia)
    #===================================================================================#
        #FUNCIONES PROVISIONALES DE GIRO CON POTENCIA FIJA Y MOTOR CONTRARIO PARADO
    def girar_derecha(self):
        """
            Esta funcion realiza el giro hacia la derecha, parando el motor
            derecho y continua activo el motor izquierdo.
        """
        
        GPIO.output(self.in1_motor1,GPIO.HIGH)
        GPIO.output(self.in2_motor1,GPIO.LOW)
        GPIO.output(self.in1_motor2,GPIO.LOW)
        GPIO.output(self.in2_motor2,GPIO.LOW)
        
    def girar_izquierda(self):
        """
            Esta funcion realiza el giro hacia la izquierda, parando el motor
            izquierdo y continua activo el motor derecho.
        """
    
        GPIO.output(self.in1_motor1,GPIO.LOW)
        GPIO.output(self.in2_motor1,GPIO.LOW)
        GPIO.output(self.in1_motor2,GPIO.HIGH)
        GPIO.output(self.in2_motor2,GPIO.LOW)
        
    def mover_adelante(self):
        """
            Esta funcion pone los dos motores a funcionar a la vez para ir recto.
        """
    
        GPIO.output(self.in1_motor1,GPIO.HIGH)
        GPIO.output(self.in2_motor1,GPIO.LOW)
        GPIO.output(self.in1_motor2,GPIO.HIGH)
        GPIO.output(self.in2_motor2,GPIO.LOW)
    
    def salida_de_pista(self):
        """
            Esta funcion para los dos motores. Sirve para cuenado el
            coche se ha salido de la pista y no se quede dando vueltas.
        """
    
        GPIO.output(self.in1_motor1,GPIO.LOW)
        GPIO.output(self.in2_motor1,GPIO.LOW)
        GPIO.output(self.in1_motor2,GPIO.LOW)
        GPIO.output(self.in2_motor2,GPIO.LOW)