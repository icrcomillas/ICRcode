
import numpy as np

class Sistema():
    def __init__(self):
        super().__init__()

    def analizarEspectroFrecuencia(self,arrayDatos,arrayFrecuencias,threshold):
        frecuencia = -1
        for i in range(0,len(arrayDatos)):
            if arrayDatos[i] > threshold:
                #en el caso de que un valor sea superior al esperado, busca la frecuencia
                frecuencia = arrayFrecuencias[i]
        return frecuencia

    def analizarEspectro(self,arrayDatos,arrayFrecuencias ,f_target, f_threshold, f_carrier, samplerate):

        f = f_target - f_carrier # frecuencia buscada 
        delta_f = samplerate / (len(arrayDatos) - 1) # intervalo entre frec. 
        pos = (f - samplerate) / delta_f # posicion del valor de la frecuencia buscado

        if arrayFrecuencias(pos) >= f_threshold:
            return True
        else:
            return False
    def generarRuido(self,media,varianza,longitud):
        return np.random.normal(media,varianza,longitud)