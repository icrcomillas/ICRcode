
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

if '__name__' == '__main__':
    #declaramos el objeto giroscopio
    direccion_giroscopio = 0x81  #estos valores son orientativos, hay que cambiarlos
    #creamos el objeto giroscopio
    giro = mpu6050(addres = direccion_giroscopio)
    print("se va a leer la informacion del giroscopio durante 5 segundos")

    continuar = True
    while continuar == True:
        
