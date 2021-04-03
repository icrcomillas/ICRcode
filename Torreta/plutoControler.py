import json
import numpy as np
from scipy.io import wavfile
from operaciones import Sistema
import threading
from scipy.fft import fft, fftfreq, fftshift
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg


global data 
global fft_calculada
data = np.empty((0,1))


class Operacion():
    def __init__(self):
        super().__init__()
        #se cargan las constantes necesarias para ejecutar el modulo
        with open('configuracion.json') as json_file:
            ficheroJson = json.load(json_file)
        self.MUESTRAS_ANALIZAR = ficheroJson['muestras_analizar']
        self.SAMPLERATE = ficheroJson['samplerate']
        self.F_THRESHOLD = ficheroJson['f_threshold']

    def runEspectro(self):
        global data
        global fft_calculada
        while(1):
            if len(data) > self.MUESTRAS_ANALIZAR:
                datos_analizar = data[0:self.MUESTRAS_ANALIZAR]
                data = data[self.MUESTRAS_ANALIZAR:]
                fft_calculada = self.calcularEspectro(datos_analizar,self.SAMPLERATE)
    def calcularEspectro(self, datos,samplerate):
        fft_data = fft(datos)/len(datos)
        fft_data = fftshift(fft_data)
        vector_frecuencia = np.linspace(-0.5,0.5,len(datos))*samplerate
        return np.column_stack((fft_data, vector_frecuencia))

    def analizarEspectro(self, f_target, f_threshold, f_carrier, samplerate):

        f = f_target - f_carrier # frecuencia buscada 
        delta_f = samplerate / (len(datos) - 1) # intervalo entre frec. 
        pos = (f - samplerate) / delta_f # posicion del valor de la frecuencia buscado

        if fft_calculada[pos, 0] >= f_threshold:
            return True
        else:
            return False

class Graficas():
    def __init__(self):
        super().__init__()
       
        self.primera_vez = True

    def mostrarGrafica(self):
        global fft_calculada
        
       
        self.curve.setData(np.abs(fft_calculada[:,0]))                     # set the curve with this data
        self.curve.setPos(-(len(fft_calculada[:,1])/2),0)                   # set x position in the graph to 0
        QtGui.QApplication.processEvents()
        

    def runGraficas(self):
        app = QtGui.QApplication([])      

        self.win = pg.GraphicsWindow(title="Analisis espectral") # creates a window
        self.p = self.win.addPlot(title="Fft")  # creates empty space for the plot in the window
        self.curve = self.p.plot() 
        while True:
           self.mostrarGrafica()          

def inicializarPlaca():
    #se ponen los valores por defecto a la placa, para poder recibir una señal 
    setPortadoraRecepcion(ficheroJson['c_rx_default'])
    setPortadoraTransmision(ficheroJson['c_tx_default'])

def setPortadoraRecepcion(frecuencia):
    placaPluto.rx_lo=frecuencia
def setPortadoraTransmision(frecuencia):
    placaPluto.tx_lo = frecuencia
def setGananciaRecepcion(ganancia):
    if getControladorGanancia() == "manual":
        placaPluto.rx_hardwaregain_chan0 = ganancia
def setControladorGanancia(modo):
    if modo == "slow_attack" or modo == "fast_attack" or modo == "manual":
        placaPluto.gain_control_mode_chan0(modo)
def getControladorGanancia():
    return placaPluto.gain_control_mode_chan0

def manejo():
    global data
    while(1):
        pass
        

with open('configuracion.json') as json_file:
    ficheroJson = json.load(json_file)


if __name__== '__main__':
    if ficheroJson['test']:
        #en el caso de que nos encontremos en modo de test
        

        samplerate, data = wavfile.read('prueba.wav')
        """
        if data.shape[1] != 0:
            data = data[:,0]
        """
        
        #se crean los hilos para el analisis de los datos
        operacion = Operacion()
        graficas = Graficas()
        hiloControl = threading.Thread(target=manejo, daemon=True)
        hiloFft = threading.Thread(target=operacion.runEspectro, daemon=True)
        hiloGraficas = threading.Thread(target=graficas.runGraficas, daemon=True)
        #se arrancan los hilos

        hiloFft.start()
        hiloControl.start()
        hiloGraficas.start()
        while(hiloControl.isAlive() and hiloFft.isAlive()):
           #logica de control de la aplicación
           pass
        pg.QtGui.QApplication.exec_() # you MUST put this at the end
        print("Hilos terminados")
    else:
        import adi 

        placaPluto = adi.Pluto()
        inicializarPlaca()
        datos  = np.empty(1)
        while(1):
            datosNuevos = placaPluto.rx()
            np.append(datos,[datosNuevos])
