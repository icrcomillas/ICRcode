import matplotlib.pyplot as plt
import numpy as np
import json


class Graficas():
    def __init__(self):
        super().__init__()
        
    @staticmethod
    def mostrarGrafica(self,datosx,datosy,titulo):
        fig, ax = plt.subplots()
        #se realiza el calculo del espectro de la señal
        ax.plot(datosx,datosy)
        ax.set_title(titulo)
        plt.show()

class Sistema():
    def __init__(self):
        super().__init__()
    @staticmethod
    def guardarArray(self,path,datos):
        np.save(path,datos)
    @staticmethod
    def cargaraArray(self,path):
        return np.load(path)
