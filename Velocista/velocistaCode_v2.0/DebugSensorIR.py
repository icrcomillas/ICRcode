import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#pines a los que se conecta los 8 pines de control del sensor de IR
pin_control_sensor=(7,11,13,15,12)

"Uso solo 5 pins porque me faltan cables, pero debería ser lo mismo"

class GestorLecturaIR():

    def __init__(self):
        self.sensor_out=[-1,-1,-1,-1,-1]

    def evaluar_sensor_IR(self):
    #Cada vez que se ejcuta muestra la salida de los pines
        for pin in range(len(pin_control_sensor)):
            tiempo_transcurrido=time.time() - tiempo_inicio_medida #en segundos
            self.sensor_out[pin]=GPIO.input(pin_control_sensor[pin])
        return (tiempo_transcurrido, self.sensor_out)

    def leer_sensor_IR(self):

       #Se ejecuta hasta que se termina de leer los 8 IR
        while -1 in self.sensor_out:
            (tiempo_transcurrido, self.sensor_out)=self.evaluar_sensor_IR()

        return (tiempo_transcurrido, self.sensor_out)

#definir pines de control como salida para ponerlos a 3.3v
for pin in pin_control_sensor:
    GPIO.setup(pin,GPIO.OUT)
#poner a 3.3v los pines
for pin in pin_control_sensor:
    GPIO.output(pin,GPIO.HIGH)

#espera a la carga del condensador
time.sleep(0.05)

#guarda el tiempo en el que se ha activado el sensor
tiempo_inicio_medida=time.time()

#definir como entrada y comienzo de la descarga
for pin in pin_control_sensor:
    GPIO.setup(pin,GPIO.IN)

#estudio de la descarga
for i in range(6):
    (tiempo_transcurrido, sensor_out)=GestorLecturaIR().leer_sensor_IR()
    print("t(ms)= ", tiempo_transcurrido*1000, ": ", sensor_out)




"""
Resultados:
t(ms)=  0.3390312194824219 :  [1, 1, 1, 1, 1]
t(ms)=  55.25636672973633 :  [1, 1, 1, 1, 1]
t(ms)=  92.13519096374512 :  [0, 0, 0, 0, 0]
t(ms)=  98.0679988861084 :  [1, 1, 1, 1, 1]
t(ms)=  119.43578720092773 :  [0, 0, 0, 0, 0]
t(ms)=  156.29172325134277 :  [1, 1, 1, 1, 1]

¿Tiempo de respuesta de la raspberry muy lento? Unos 40ms entre cálculo y
cálculo. Los condensadores se descargan en menos de 4ms para 100% negro.
¿Necesitamos mejor procesador? ¿Mi código está mal? No sé. Help.
"""
