from configuracion import robot
from mpu6050 import mpu6050

def acel_giro():
    aceleracion = giro.get_accel_data() #leemos todas las aceleraciones del giroscopio

    x = aceleracion['x']
    y = aceleracion['y']
    z = aceleracion['z']

    return x, y,z       # los valores x , y , z son las aceleraciones en sus respectivos ejes


def pos_giro():

    inclinacion = giro.get_giro_data()

    x = inclinacion['x']
    y = inclinacion['y']
    z = inclinacion['z']

    return x, y ,z

if __name__ == '__main__':
    #declaramos el objeto giroscopio

    #creamos el objeto giroscopio
    giro = mpu6050(robot.direccion_giroscopio)
    print("se va a leer la informacion del giroscopio durante 5 segundos")


    while True:
        acel_x,acel_y,acel_z = pos_giro()
        print("las aceleraciones son: " +str(acel_x)+" "+str(acel_y)+" "+str(acel_z))
