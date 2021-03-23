
import numpy as np
import json




class Sistema():
    def __init__(self):
        super().__init__()
    @staticmethod
    def guardarArray(self,path,datos):
        np.savetxt(path,datos)
    @staticmethod
    def cargaraArray(self,path):
        return np.loadtxt(path)
