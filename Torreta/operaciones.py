import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

class graficas():
    def __init__(self):
        super().__init__()
        
    @staticmethod
    def mostrarGrafica(self,datosx,datosy,titulo):
        fig, ax = plt.subplots()
        #se realiza el calculo del espectro de la señal
        ax.plot(datosx,datosy)
        ax.set_title(titulo)
        plt.show()
class operacion():
    def __init__(self):
        super().__init__()
    @staticmethod
    def calcularEspectro(self, data,samplerate):
        fft_data = fft(data)
        vector_frecuencia = fftfreq(len(data),1/samplerate)
        return fft_data, vector_frecuencia
class sistema():
    def __init__(self):
        super().__init__()
    @staticmethod
    def guardarArray(self,path,datos):
        np.save(path,datos)
    @staticmethod
    def cargaraArray(self,path):
        return np.load(path)
