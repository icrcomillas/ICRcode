import json
import numpy as np
from scipy.io import wavfile
from operaciones import graficas, operacion
import adi 



with open('Torreta\configuracion.json') as json_file:
    ficheroJson = json.load(json_file)
    


if ficheroJson['test']:
    #en el caso de que nos encontremos en modo de test
    grafica = graficas()
    computador = operacion()

    samplerate, data = wavfile.read('Torreta\prueba.wav')
    #se crea el vector de tiempos
    vector_tiempo = np.linspace(0,len(data)/samplerate,len(data))
    
   
    #se realiza el calculo del espectro de la señal
    
    
    grafica.mostrarGrafica(vector_frecuencia,np.abs(fft_data),'Espectro')
    #se realiza el diezmado de la señal
else:
    placaPluto = adi.Pluto(ficheroJson['direccionIp'])
    inicializarPlaca()


def inicializarPlaca():
    #se ponen los valores por defecto a la placa, para poder recibir una señal 
    setPortadoraRecepcion(ficheroJson['c_rx_default'])
    setPortadoraTransmision(ficheroJson['c_tx_default'])

def setPortadoraRecepcion(frecuencia):
    placaPluto.rx_lo(frecuencia)
def setPortadoraTransmision(frecuencia):
    placaPluto.tx_lo(frecuencia)
<<<<<<< HEAD
def setGanancia(ganancia)
    placaPluto.rx_hardwaregain_chan0(ganancia)
=======
def setGanancia(ganancia):
    placaPluto.rx_hardwaregain_chan0(ganancia)
>>>>>>> cd828389ba71d33b5b0b02abb09c98637daa927c
