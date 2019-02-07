BOARD = 1
OUT = 1
IN = 1
import RPi.GPIO as pwm

def setmode(a):
   print (a)
def setup(a, b):
   print (a)
def output(a, b):
   print (a)
def cleanup():
   print ('a')
def setwarnings(flag):
   print ('False')

#Añadidos:
def PWM(a,b):
   print ('Pin:',a,'Señal',b)

pwm.PWM(a)
pwm.PWM(a)
