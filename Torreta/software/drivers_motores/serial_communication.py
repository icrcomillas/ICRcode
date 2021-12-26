import serial



arduino = serial.Serial('/dev/ttyUSB0',115200)
print("Se ha abierto el puerto serial con el arduino")
print(arduino.name)

while True:
	#Se ordena que se mueva un grado a los motores
	mensaje = "001,1,001,1)"
	arduino.write(mensaje.encode())