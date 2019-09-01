#la gui se va a hacer con la libreria tkinter de python, que es nativa de este
from tkinter import *
from mpu6050 import mpu6050
from configuracion import robot
#creamos el objeto robot
humanoide = robot(0x40,,0x68)
#creamos la ventana

ventana = Tk()
ventana.title("controlador robot")
ventana.geometry("600x600")

#hay que mejorar la estructura de la gui notablemente, esta es una primera version
#coloco el texto
texto = Label(ventana, text = "controlador robot", font = ("Arial Bold", 30))
texto.grid(column = 4, row = 0)

#entrada se refiere a la barra para escribir
entrada = Entry(ventana, width = "10")
entrada.grid(column = 2, row = 1)
#boton para enviar la posicion del servo
boton = Button(ventana, text = "enviar")

ventana.mainloop()
