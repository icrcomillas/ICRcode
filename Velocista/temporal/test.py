import RPi.GPIO as GPIO          
from time import sleep
der = 3
izda = 5
in11 = 36
in21 = 38
en1 = 40
in12 = 37
in22 = 35
en2 = 33
lediz = 32
ledde = 26
temp1=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(der,GPIO.IN)
GPIO.setup(izda,GPIO.IN)
GPIO.setup(in11,GPIO.OUT)
GPIO.setup(in21,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(in11,GPIO.LOW)
GPIO.output(in21,GPIO.LOW)
p=GPIO.PWM(en1,1000)
p.start(50)
GPIO.setup(in12,GPIO.OUT)
GPIO.setup(in22,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in12,GPIO.LOW)
GPIO.output(in22,GPIO.LOW)
p2=GPIO.PWM(en2,1000)
p2.start(50)
GPIO.setup(lediz,GPIO.OUT)
GPIO.setup(ledde,GPIO.OUT)
GPIO.output(lediz,GPIO.LOW)
GPIO.output(ledde,GPIO.LOW)
"""
while True:
    print("\n Izda: ")
    print(GPIO.input(izda))
    sleep(0.5)
    print("\n der: ")
    print(GPIO.input(der))
    sleep(0.5)
"""    
p.ChangeDutyCycle(100)
p2.ChangeDutyCycle(20)
while True:
    if GPIO.input(der)==0 and GPIO.input(izda)==1:
        GPIO.output(in11,GPIO.LOW)
        GPIO.output(in21,GPIO.LOW)
        GPIO.output(in12,GPIO.HIGH)
        GPIO.output(in22,GPIO.LOW)
        GPIO.output(lediz,GPIO.LOW)
        GPIO.output(ledde,GPIO.HIGH)
    elif GPIO.input(der)==1 and GPIO.input(izda)==0:
        GPIO.output(in11,GPIO.HIGH)
        GPIO.output(in21,GPIO.LOW)
        GPIO.output(in12,GPIO.LOW)
        GPIO.output(in22,GPIO.LOW)
        GPIO.output(ledde,0)
        GPIO.output(lediz,1)
    elif GPIO.input(der)==0 and GPIO.input(der)==0:
        GPIO.output(in11,GPIO.HIGH)
        GPIO.output(in21,GPIO.LOW)
        GPIO.output(in12,GPIO.HIGH)
        GPIO.output(in22,GPIO.LOW)
        GPIO.output(ledde,0)
        GPIO.output(lediz,0)
    else:
        GPIO.output(in11,GPIO.LOW)
        GPIO.output(in21,GPIO.LOW)
        GPIO.output(in12,GPIO.LOW)
        GPIO.output(in22,GPIO.LOW)
        GPIO.output(ledde,1)
        GPIO.output(lediz,1)

"""
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(100)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")"""