#   Python QTR-8RC sensor library
#   Atuhor: Tom Broughton (@dpolymath)
#   Date: 20/03/2017
#
#   Reads the Pololu QTR-8RC IR sensor array
#   https://www.pololu.com/docs/pdf/0J12/QTR-8x.pdf
#
#   Hardware setup (changing pins can be managed in init):
#   LEDON pin connected to GPIO 21
#   3V3 to Pi GPIO rail and GND (bypass soldered on qtr-8rc for 3V3 option)
#   Pins 22 - 29 to each IR LED/phototransitor pair
#    - This version does not work with PWM for LEDON_PIN
#
# #############################################################################
#   MIT License
#
#   Copyright (c) 2017 Tom Broughton 
#
#   Permission is hereby granted, free vof charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.
###############################################################################
 
import wiringpi as wp
 
class MrBit_QTR_8RC:
    """ Class for reading values from Pololu QT8-8RC sensor array.
        Requires wiringpi https://github.com/WiringPi/WiringPi-Python
    """
 
    def __init__(self):
        """ Initialises class constants and variables - pins defined here.
        """
 
        self.wp = wp
        self.wp.wiringPiSetup()
 
        self.LEDON_PIN = 29
        self.SENSOR_PINS = [7,11,13,15,12,16,18,22]
        self.NUM_SENSORS = len(self.SENSOR_PINS)
        self.CHARGE_TIME = 10 #us to charge the capacitors
        self.READING_TIMEOUT = 1000 #us, assume reading is black
 
        self.sensorValues = []
        self.calibratedMax = []
        self.calibratedMin = []
        self.lastValue = 0
        self.init_pins()
 
 
    def init_pins(self):
        """ Sets up the GPIO pins and also ensures the correct number of items
            in sensors values and calibration lists to store readings.
        """
        for pin in self.SENSOR_PINS:
            self.sensorValues.append(0)
            self.calibratedMax.append(0)
            self.calibratedMin.append(0)
            self.wp.pullUpDnControl(pin, self.wp.PUD_DOWN)
        self.wp.pinMode(self.LEDON_PIN, self.wp.OUTPUT)
 
 
    def emitters_on(self):
        """ Turns the LEDON pin on so that the IR LEDs can be turned on.
            If there is nothing wired to LEDON emitters will always be on.
            Use emitters_on and emitters_off to conserve power consumption.
        """
        self.wp.digitalWrite(self.LEDON_PIN, self.wp.HIGH)
        self.wp.delayMicroseconds(20)
 
 
    def emitters_off(self):
        """ Turns the LEDON pin off so that the IR LEDs can be turned off.
            If there is nothing wired to LEDON emitters will always be on.
            Use emitters_on and emitters_off to conserve power consumption.
        """
        self.wp.digitalWrite(self.LEDON_PIN, self.wp.LOW)
        self.wp.delayMicroseconds(20)
 
 
    def print_sensor_values(self, values):
        """ Params: values - a list of sensor values to print
            Prints out the sensor and it's current recorded reading.
        """
        for i in range(0, self.NUM_SENSORS):
            print("sensor %d, reading %d" % (i, values[i]))
 
 
    def initialise_calibration(self):
        """ Resets (inverse) max and min thresholds prior to calibration
            so that calibration readings can be correctly stored.
        """
        for i in range(0, self.NUM_SENSORS):
            self.calibratedMax[i] = 0
            self.calibratedMin[i] = self.READING_TIMEOUT
 
 
    def calibrate_sensors(self):
        """ Takes readings across all sensors and sets max and min readings
            typical use of this function is to call several times with delay
            such that a total of x seconds pass.  (e.g. 100 calls, with 20ms
            delays = 2 seconds for calibration).  When running this move the
            sensor over the line several times to calbriate contrasting surface.
        """
        for j in range(0, 10):
            self.read_sensors()
            for i in range(0, self.NUM_SENSORS):
                if self.calibratedMax[i] < self.sensorValues[i]:
                    self.calibratedMax[i] = self.sensorValues[i]
                if self.calibratedMin[i] > self.sensorValues[i] and self.sensorValues[i] > 30:
                    self.calibratedMin[i] = self.sensorValues[i]
 
 
    def read_line(self):
        """ Reads all calibrated sensors and returns a value representing a
            position on a line.  The values range from 0 - 7000, values == 0 and
            values == 7000 mean sensors are not on line and may have left the
            line from the right or left respectively.  Values between 0 - 7000
            refer to the position of sensor, 3500 referring to centre, lower val
            to the right and higher to the left (if following pin set up in init).
        """
        self.read_calibrated()
 
        avg = 0
        summ = 0
        online = False
 
        for i in range(0, self.NUM_SENSORS):
            val = self.sensorValues[i]
            if val > 500: online = True
            if val > 50:
                multiplier = i * 1000
                avg += val * multiplier
                summ +=  val
 
        if online == False:
            if self.lastValue < (self.NUM_SENSORS-1)*1000/2:
                return 0
            else:
                return (self.NUM_SENSORS-1)*1000
 
        self.lastValue = avg/summ
        return self.lastValue
 
 
    def read_calibrated(self):
        """ Reads the calibrated values for each sensor.
        """
 
        self.read_sensors()
 
        print("uncalibrated readings")
        self.print_sensor_values(self.sensorValues)
 
        for i in range(0, self.NUM_SENSORS):
            denominator = self.calibratedMax[i] - self.calibratedMin[i]
            val = 0
            if denominator != 0:
                val = (self.sensorValues[i] - self.calibratedMin[i]) * 1000 / denominator
            if val < 0:
                val = 0
            elif val > 1000:
                val = 1000
            self.sensorValues[i] = val
 
        print("calibrated readings")
        self.print_sensor_values(self.sensorValues)
 
 
    def read_sensors(self):
        """ Follows the Pololu guidance for reading capacitor discharge/sensors:
            1. Set the I/O line to an output and drive it high.
            2. Allow at least 10 us for the sensor output to rise.
            3. Make the I/O line an input (high impedance).
            4. Measure the time for the voltage to decay by waiting for the I/O
                line to go low.
            Stores values in sensor values list, higher vals = darker surfaces.
        """
        for i in range(0, self.NUM_SENSORS):
            self.sensorValues[i] = self.READING_TIMEOUT
 
        for sensorPin in self.SENSOR_PINS:
            self.wp.pinMode(sensorPin, self.wp.OUTPUT)
            self.wp.digitalWrite(sensorPin, self.wp.HIGH)
 
        self.wp.delayMicroseconds(self.CHARGE_TIME)
 
        for sensorPin in self.SENSOR_PINS:
            self.wp.pinMode(sensorPin, self.wp.INPUT)
            #important: ensure pins are pulled down
            self.wp.digitalWrite(sensorPin, self.wp.LOW)
 
        startTime = self.wp.micros()
        while self.wp.micros() - startTime < self.READING_TIMEOUT:
            time = self.wp.micros() - startTime
            for i in range(0, self.NUM_SENSORS):
                if self.wp.digitalRead(self.SENSOR_PINS[i]) == 0 and time < self.sensorValues[i]:
                    self.sensorValues[i] = time
 
 
 
 
#Example ussage:
if __name__ == "__main__":
    #'__name__' es un atributo que tiene los modulos de python al ejecutarse. Si el modulo se ejecuta como
    #programa principal este atributo recibe el valor de  '__main__'. Si el modulo se importa desde otro modulo
    #recibe su propio nombre, en este caso 'libraryIR'.
    try:
        #crea gestor de lectura
        qtr = MrBit_QTR_8RC()
 
        approveCal = False
        while not approveCal:
            print("calibrating")
            qtr.initialise_calibration()
            print("1")
            qtr.emitters_on()
            print("2")
            
            for i in range(0, 250):
                qtr.calibrate_sensors()
                print("3")
                wp.delay(20)
            qtr.emitters_off()
 
            print("calibration complete")
            print ("max vals")
            qtr.print_sensor_values(qtr.calibratedMax)
            print ("calibration complete")
            print ("min vals")
            qtr.print_sensor_values(qtr.calibratedMin)
            approved = raw_input("happy with calibrtion (Y/n)? ")
            if approved == "Y": approveCal = True
    except Exception as e:
        qtr.emitters_off()
        print(str(e))
    try:
        while 1:
            qtr.emitters_on()
            print(qtr.read_line())
            qtr.emitters_off()
            wp.delay(20)
 
    except KeyboardInterrupt:
        qtr.emitters_off()
 
    except Exception as e:
        print(str(e))