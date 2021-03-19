import json
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from operaciones import graficas
import adi 



with open('Torreta\configuracion.json') as json_file:
    ficheroJson = json.load(json_file)
    
placaPluto = adi.Pluto(ficheroJson['direccionIp'])


if ficheroJson['test']:
    #en el caso de que nos encontremos en modo de test
    
    samplerate, data = wavfile.read('Torreta\prueba.wav')
    #se crea el vector de tiempos
    vector_tiempo = np.linspace(0,len(data)/samplerate,len(data))
    
   
    #se realiza el calculo del espectro de la señal
    fft_data = fft(data)
    vector_frecuencia = fftfreq(len(data),1/samplerate)
    grafica = graficas()
    grafica.mostrarGrafica(vector_frecuencia,np.abs(fft_data),'Espectro')
    #se realiza el diezmado de la señal


def inicializarPlaca():
    #se ponen los valores por defecto a la placa, para poder recibir una señal 
    setPortadoraRecepcion(ficheroJson['c_rx_default'])
    setPortadoraTransmision(ficheroJson['c_tx_default'])
    
def setPortadoraRecepcion(frecuencia):
    placaPluto.rx_lo(frecuencia)
def setPortadoraTransmision(frecuencia):
    placaPluto.tx_lo(frecuencia)