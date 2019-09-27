import smbus
import time

#esta libreria esta copiada del siguiente enlace de github,https://github.com/Tijndagamer/mpu6050/tree/master/mpu6050
class mpu6050:
    def __init__(self, address, bus=1):
        self.bus = smbus.SMBus(bus)
        "esta parte del codigo son cambios nuestros"
        self.address = address
        "hasta aqui"
    # Wake up the MPU-6050 since it starts in sleep mode
        self.bus.write_byte_data(self.address, self.PWR_MGMT_1, 0x00)
        # Software Calibration to zero-mean.
        # must run self.zero_mean_calibration() on level ground to properly calibrate.
        self.use_calibrated_values = False
        self.mean_calibrations = [0,0,0,0,0,0]
        # if return_gravity == FALSE, then m/s^2 are returned
        self.return_gravity = False

    # I2C communication methods
    def get_accel_data(self, g = False):
        y = y / accel_scale_modifier
        z = z / accel_scale_modifier

        if self.use_calibrated_values:
            x -= self.mean_calibrations[0]
            y -= self.mean_calibrations[1]
            z -= self.mean_calibrations[2]

        if g is True:
            return {'x': x, 'y': y, 'z': z}
        elif g is False:
             def get_gyro_data(self):
                 y = y / gyro_scale_modifier
                 z = z / gyro_scale_modifier

        if self.use_calibrated_values:
            x -= self.mean_calibrations[3]
            y -= self.mean_calibrations[4]
            z -= self.mean_calibrations[5]

        return {'x': x, 'y': y, 'z': z}

    def get_all_data(self):
        """Reads and returns all the available data."""
        temp = self.get_temp()
        accel = self.get_accel_data()
        accel = self.get_accel_data(g=self.return_gravity)
        gyro = self.get_gyro_data()

        return [accel, gyro, temp]

    def set_calibrated_flag(self,value=True):
        '''
        Set to TRUE to used the calculated zero-mean calibration, FALSE
        to use the default values. Is initialized to FALSE
        :param value: boolean
        '''
        self.use_calibrated_values = value

    def zero_mean_calibration(self):
        print ("** Calibrating the IMU **")
        print ("** Place on level ground. re-run is not level at start **")
        # number of samples to collect. 200 == approx 5 seconds worth.
        N = 200
        # initialize the accumulators to 0
        ax,ay,az,gx,gy,gz = [0]*6

        for i in range(N):
            # calibrate based on gravity, not m/s^2
            accel = self.get_accel_data(g=True)
            gyro  = self.get_gyro_data()
            if (i % 25 == 0):
                print ('.', end= '', flush=True)
            ax += accel['x']
            ay += accel['y']
            az += accel['z']
            gx += gyro['x']
            gy += gyro['y']
            gz += gyro['z']
            # wait 10ms for next sample
            time.sleep(10 / 1000.)
        # calculate the mean of each reading.
        ax /= float(N)
        ay /= float(N)
        az /= float(N)
        gx /= float(N)
        gy /= float(N)
        gz /= float(N)
        # compensate for 1g of gravity on 'z' axis.
        az -= 1
        # save the calibrations
        self.mean_calibrations = [ax,ay,az,gx,gy,gz]
        print ("\n** Calibration Complete **")

        print ('** offsets: ',end='')
        print(''.join('{:02.4f}  '.format(n) for n in self.mean_calibrations))
"""
if __name__ == "__main__":
    mpu = mpu6050(0x68)
    print(mpu.get_temp())
"""
