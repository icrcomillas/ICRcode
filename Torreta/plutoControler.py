import json
import numpy as np
from scipy.io import wavfile
from operaciones import Sistema
import threading
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt


global data 

data = np.empty((0,1))


class Operacion():
    def __init__(self):
        super().__init__()
        #se cargan las constantes necesarias para ejecutar el modulo
        with open('Torreta\configuracion.json') as json_file:
            ficheroJson = json.load(json_file)
        self.MUESTRAS_ANALIZAR = ficheroJson['muestras_analizar']
        self.SAMPLERATE = ficheroJson['samplerate']

    def runEspectro(self):
        global data
        global fft
        while(1):
            if len(data) > self.MUESTRAS_ANALIZAR:
                datos_analizar = data[0:self.MUESTRAS_ANALIZAR]
                data = data[self.MUESTRAS_ANALIZAR:]
                fft = self.calcularEspectro(datos_analizar,self.SAMPLERATE)
  
    def calcularEspectro(self, data,samplerate):
        fft_data = fft(data)
        vector_frecuencia = fftfreq(len(data),1/samplerate)
        return np.array(fft_data, vector_frecuencia)

class Graficas():
    def __init__(self):
        super().__init__()
       
        self.primera_vez = True
    @staticmethod
    def mostrarGrafica(self,datosx,datosy,titulo):
        global fft
        if self.primera_vez == True:
            self.primera_vez = False
            plt.style.use('ggplot')
            plt.ion()
            self.fig = plt.figure(figsize=(13,6))
            self.ax = self.fig.addsubplot(111)
            self.line, = self.ax.plot(datosx,datosy)
            plt.title(titulo)
            plt.show()
        else:
            self.line.set_data(datosx,datosy)
        plt.pause(0.01)
            
       

def inicializarPlaca():
    #se ponen los valores por defecto a la placa, para poder recibir una señal 
    setPortadoraRecepcion(ficheroJson['c_rx_default'])
    setPortadoraTransmision(ficheroJson['c_tx_default'])

def setPortadoraRecepcion(frecuencia):
    placaPluto.rx_lo(frecuencia)
def setPortadoraTransmision(frecuencia):
    placaPluto.tx_lo(frecuencia)
def setGananciaRecepcion(ganancia):
    if getControladorGanancia() == "manual":
        placaPluto.rx_hardwaregain_chan0(ganancia)
def setControladorGanancia(modo):
    if modo == "slow_attack" or modo == "fast_attack" or modo == "manual":
        placaPluto.gain_control_mode_chan0(modo)
def getControladorGanancia():
    return placaPluto.gain_control_mode_chan0

def manejo():
    global data
    while(1):
        

with open('Torreta\configuracion.json') as json_file:
    ficheroJson = json.load(json_file)


if __name__== '__main__':
    if ficheroJson['test']:
        #en el caso de que nos encontremos en modo de test
        

        samplerate, data = wavfile.read('Torreta\prueba.wav')
        """
        if data.shape[1] != 0:
            data = data[:,0]
        """
        
        #se crean los hilos para el analisis de los datos
        operacion = Operacion()
        hiloControl = threading.Thread(target=manejo, daemon=True)
        hiloFft = threading.Thread(target=operacion.runEspectro, daemon=True)
        
        #se arrancan los hilos

        hiloFft.start()
        hiloControl.start()
        while(hiloControl.isAlive() and hiloFft.isAlive()):
           #logica de control de la aplicación
           pass
        print("Hilos terminados")
    else:
        import adi 

        placaPluto = adi.Pluto(ficheroJson['direccionIp'])
        inicializarPlaca()
        datos  = np.empty()
        while(1):
            datosNuevos = placaPluto.rx()
            np.append(datos,[datosNuevos])