import time
import RPi.GPIO as GPIO
import array as arr
GPIO.setmode(GPIO.BOARD)
#pines a los que se conecta los 8 pines de control del sensor de IR
pin_control_sensor=(7,11,13,15,12,16,18,22)



class GestorLecturaIR():

    def __init__(self):
        self.sensor_out=[-1,-1,-1,-1,-1, -1, -1, -1]

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

tiemposMediosTotales = 0

#ensayos
"Número de ensayos"
n1=50
for i in range(n1):

	"definir pines de control como salida para ponerlos a 3.3v"
	for pin in pin_control_sensor:
	    GPIO.setup(pin,GPIO.OUT)

	"poner a 3.3v los pines"
	for pin in pin_control_sensor:
	    GPIO.output(pin,GPIO.HIGH)

	"espera a la carga del condensador"
	time.sleep(0.05)

	"Declaración de variables"
	tiempos = arr.array('f', [])
	valores = []
	pin1 = arr.array('i', [])
	pin2 = arr.array('i', [])
	pin3 = arr.array('i', [])
	pin4 = arr.array('i', [])
	pin5 = arr.array('i', [])
	pin6 = arr.array('i', [])
	pin7 = arr.array('i', [])
	pin8 = arr.array('i', [])

	"guarda el tiempo en el que se ha activado el sensor"
	tiempo_inicio_medida=time.time()

	"definir como entrada y comienzo de la descarga"
	for pin in pin_control_sensor:
	    GPIO.setup(pin,GPIO.IN)

	"Número de lecturas por ensayo"
    n2=200
    "estudio de la descarga"
    for j in range(n2):
        (tiempo_transcurrido, sensor_out)=GestorLecturaIR().leer_sensor_IR()
        tiempos.append(tiempo_transcurrido*1000)
        pin1.append(sensor_out[0])
        pin2.append(sensor_out[1])
        pin3.append(sensor_out[2])
        pin4.append(sensor_out[3])
        pin5.append(sensor_out[4])
        pin6.append(sensor_out[5])
        pin7.append(sensor_out[6])
        pin8.append(sensor_out[7])
    valores = [pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8]
    #print(tiempos, "\n",valores) "por si se quieren ver los valores concretos"
    print("El tiempo de ejecución medio del ensayo", i+1, "es: ", tiempos[n2-1]/n2, "ms")
	tiemposMediosTotales+=tiempos[n2-1]/n2
print("El tiempo de ejecución medio total es: ", tiemposMediosTotales/n1, "ms")


"""
Primeros Resultados:
t(ms)=  0.3390312194824219 :  [1, 1, 1, 1, 1]
t(ms)=  55.25636672973633 :  [1, 1, 1, 1, 1]
t(ms)=  92.13519096374512 :  [0, 0, 0, 0, 0]
t(ms)=  98.0679988861084 :  [1, 1, 1, 1, 1]
t(ms)=  119.43578720092773 :  [0, 0, 0, 0, 0]
t(ms)=  156.29172325134277 :  [1, 1, 1, 1, 1]

Segundos resultados:
El tiempo de ejecución medio del ensayo 1 es:  0.7019996643066406 ms
El tiempo de ejecución medio del ensayo 2 es:  0.7425797271728516 ms
...omitimos...
El tiempo de ejecución medio del ensayo 49 es:  0.7427024841308594 ms
El tiempo de ejecución medio del ensayo 50 es:  0.7020616149902343 ms
El tiempo de ejecución medio total es:  0.7449918479919435 ms
"""
