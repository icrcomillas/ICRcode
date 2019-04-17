def mover_servo(n_servo,pos):
    #posicion la reciviremos en un rango de 0 a 4096
    RANGO_MAXIMO = 4096
    if pos > RANGO_MAXIMO:
        print("no se puede mover ese rango, esta fuera del alcance")
    elif pos< RANGO_MAXIMO:
        driver.set_pwm(n_servo, 0, pos)
    return

def acel_giro():
    aceleracion = giro.get_accel_data() #leemos todas las aceleraciones del giroscopio
    x = aceleracion['x']
    y = aceleracion['y']
    z = aceleracion['z']
    return x, y,z       # los valores x , y , z son las aceleraciones en sus respectivos ejes

def pos_giro():

    inclinacion = get_giro_data()
    x = inclinacion['x']
    y = inclinacion['y']
    z = inclinacion['z']


    return x, y ,z



#creamos un modo de debug para poder arrancar todas las funciones
#sin necesidad de llamar a todo el codigo

if '__name__' == '__main__':
    import time
    import mpu6050
    import Adafruit_PCA9685

    #creamos el objeto driver
    driver = Adafruit_PCA9685.PCA9685(addres = direccion_driver)
    #creamos el objeto giroscopio
    giro = mpu6050(addres = direccion_giroscopio )
    print("se ha entrado en el modo debug")
    #esperamos dos segundos
    time.sleep(2)
    NUMERO_SERVOS = 2       #este será el numero de servos que tendremos en nuestro robot
    RANGO_MAXIMO = 200      #este será el angulo maximo al que se moveran los servos
    RANGO_MINIMO = 0        #rango minimo al que se mueven los servos


    #movemos todos los servos, hasta su rango maximo
    for i in range(1,NUMERO_SERVOS):
        for j in range(RANGO_MINIMO, RANGO_MAXIMO):
            mover_servo(i,j)
            time.sleep(0.1)

    print("se han terminado de mover los servos")
    print("se van a recibir los datos del giroscopio")

    acelx, acely, acelz = acel_giro()
    posx, posy, posz = pos_giro()

    print("las aceleraciones son "+string(acelx)+ " en x "+string(acely)+" en y "+string(acelz)+" en z"

    print("las posiciones son "+string(posx)+ " en x "+string(posy)+" en y "+string(posz)+" en z"
