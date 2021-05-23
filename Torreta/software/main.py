import json
import numpy as np
from plutoController import Controller,Operacion,Sistema

global longitud_datos
if __name__== '__main__':
        continuar =True
        M_diezmado = 2
        longitud_datos = 1024/M_diezmado   #Se calcula la longitud de los datos a procesar para poder saber la posicion del indice de la frecuencia de muestreo

        
        with open('configuracion.json') as json_file:
            ficheroJson = json.load(json_file)

        #se incicializan las variables iniciales
        frecuenciaPortadoraRecv = ficheroJson['c_rx_default']
        frecuenciaPortadoraTrans = ficheroJson['c_tx_default']
        samplerate = ficheroJson['samplerate']
        filtroAnalog = ficheroJson['f_analog']
        ganancia = ficheroJson['ganancia']
        threshold = ficheroJson['threshold']
	
        #se inicializa el controlador de la placa
        controller = Controller()
        controller.inicializarPlaca(frecuenciaPortadoraRecv,frecuenciaPortadoraTrans,samplerate,filtroAnalog,ganancia)

        #objeto para realizar las operaciones
        operacion = Operacion(samplerate)

        #objeto para la toma de decisiones
        sistema =Sistema(ficheroJson['salto_frecuencia'],ficheroJson['frecuencia_min'],ficheroJson['frecuencia_max'])
        
        data  = np.zeros(1)
             
        while(continuar ==True):
           #logica de control de la aplicación	
            datosNuevos = controller.rx()
            #se diezman los datos por un valor de 2
            datosNuevos = datosNuevos[:-M_diezmado:M_diezmado]
            datosNuevos =np.append([datosNuevos],[np.array(frecuenciaPortadoraRecv)])
            data= np.append([data],[datosNuevos])
            #se calcula la fft de la secuencia
            fft = operacion.calcularEspectro(datosNuevos)
            sistema.decidirFrecuenciaPortadora(fft[:,0],fft[:,1],threshold)

        #pg.QtGui.QApplication.exec_() # you MUST put this at the end
        print("Hilos terminados")   

	    
