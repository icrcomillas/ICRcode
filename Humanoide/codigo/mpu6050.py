import smbus
import time

#esta libreria esta copiada del siguiente enlace de github,https://github.com/Tijndagamer/mpu6050/tree/master/mpu6050
class mpu6050:
        # Global Variables
    GRAVITIY_MS2 = 9.80665
    address = None
    bus = None

    # Scale Modifiers
    ACCEL_SCALE_MODIFIER_2G = 16384.0
    ACCEL_SCALE_MODIFIER_4G = 8192.0
    ACCEL_SCALE_MODIFIER_8G = 4096.0
    ACCEL_SCALE_MODIFIER_16G = 2048.0

    GYRO_SCALE_MODIFIER_250DEG = 131.0
    GYRO_SCALE_MODIFIER_500DEG = 65.5
    GYRO_SCALE_MODIFIER_1000DEG = 32.8
    GYRO_SCALE_MODIFIER_2000DEG = 16.4

    # Pre-defined ranges
    ACCEL_RANGE_2G = 0x00
    ACCEL_RANGE_4G = 0x08
    ACCEL_RANGE_8G = 0x10
    ACCEL_RANGE_16G = 0x18

    GYRO_RANGE_250DEG = 0x00
    GYRO_RANGE_500DEG = 0x08
    GYRO_RANGE_1000DEG = 0x10
    GYRO_RANGE_2000DEG = 0x18

    # MPU-6050 Registers
    PWR_MGMT_1 = 0x6B
    PWR_MGMT_2 = 0x6C

    ACCEL_XOUT0 = 0x3B
    ACCEL_YOUT0 = 0x3D
    ACCEL_ZOUT0 = 0x3F

    TEMP_OUT0 = 0x41

    GYRO_XOUT0 = 0x43
    GYRO_YOUT0 = 0x45
    GYRO_ZOUT0 = 0x47

    ACCEL_CONFIG = 0x1C
    GYRO_CONFIG = 0x1B
    def __init__(self, address, bus=1):
        self.bus = smbus.SMBus(bus)
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
