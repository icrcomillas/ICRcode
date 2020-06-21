from giroscopio import Giroscopio
if __name__ == "__main__":      #rutina para comprobar que todo funciona correctamente
    giro = Giroscopio(0x68)     #se crea el objeto giroscopio
    giro.calibrarGriroscopio()
    while True:
        print(giroscopio.get_temp())
        accel_data = giroscopio.getAcelGiro()
        print(accel_data[0])
        print(accel_data[1])
        print(accel_data[2])
        gyro_data = giroscopio.getPosGiro()
        print(gyro_data[0])
        print(gyro_data[1])
        print(gyro_data[2])