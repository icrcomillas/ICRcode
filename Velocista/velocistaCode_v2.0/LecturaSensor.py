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

"Número de lecturas"
n2=30
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

print("Pin1: \n")
for i in range(n2):
	print("t=", tiempos[i], ": out: ", valores[0][i],"\n")

print("\nPin2: \n")
for i in range(n2):
	print("t=", tiempos[i], ": out: ", valores[1][i],"\n")

print("\nPin3: \n")
for i in range(n2):
	print("t=", tiempos[i], ": out: ", valores[2][i],"\n")

print("\nPin4: \n")
for i in range(n2):
	print("t=", tiempos[i], ": out: ", valores[3][i],"\n")

print("\nPin5: \n")
for i in range(n2):
	print("t=", tiempos[i], ": out: ", valores[4][i],"\n")

print("\nPin6: \n")
for i in range(n2):
	print("t=", tiempos[i], ": out: ", valores[5][i],"\n")

print("\nPin7: \n")
for i in range(n2):
	print("t=", tiempos[i], ": out: ", valores[6][i],"\n")

print("\nPin8: \n")
for i in range(n2):
	print("t=", tiempos[i], ": out: ", valores[7][i],"\n")

"""

Resultados:



Tiempos de apagado:

Ensayo 1.1:
1: 0 (!) muy rápido por reflejarse en lápiz
2: 0.4
3: 0.76
4: 3.17
5: 3.17
6: 0.4
7: 0.4
8: 0.4

Ensayo 1.2:
1: 0 (!) muy rápido por reflejarse en lápiz
2: 0.4
3: 0.4
4: 3.16
5: 3.44
6: 0.4
7: 0.4
8: 0.4

Ensayo 2.1:
1: 0 (!) muy rápido por reflejarse en lápiz
2: 0.4
3: 0.4
4: 1.35
5: 6.13 (cinta negra)
6: 7.27 (cinta negra)
7: 2.36
8: 0.4 (por reflejarse en lápiz)

Ensayo 2.1:
1: 0.4
2: 0.4
3: 0.4
4: 1.62
5: 5.5 (cinta negra)
6: 5.5 (cinta negra)
7: 1.9
8: 0.4 (por reflejarse en lápiz)
"""
