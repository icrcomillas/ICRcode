import json
import numpy as np
import threading
from plutoController import Controller,Operacion,Sistema,Graficas

global longitud_datos
global datosMostrar
if __name__== '__main__':
        continuar =True
        M_diezmado = 2
        longitud_datos = 1024/M_diezmado   #Se calcula la longitud de los datos a procesar para poder saber la posicion del indice de la frecuencia de muestreo
        estado ='grueso' 

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
        
        #objeto de graficas
        graficasFFt = Graficas()
        #se crea el hilo para mostrar los resultados
        hiloGraficas = threading.Thread(target=graficasFFt.runGraficas, daemon = True)
        #se arranca el hilo
        hiloGraficas.start()
        print("Se ha inicializado el sistema")
        contradorMuestras = 0 #contador para saber si se ha detectado algo en 
        while(continuar ==True):
            #logica de control de la aplicación	
            
            if estado == 'recepcion':
                datosNuevos = controller.rx()
                #se diezman los datos por un valor de 2
                datosNuevos = datosNuevos[:-M_diezmado:M_diezmado]
                datosNuevos =np.append([datosNuevos],[np.array(frecuenciaPortadoraRecv)])
                
                #se calcula la fft de la secuencia
                fft = operacion.calcularEspectro(datosNuevos)
            if estado =='gruesa': #significa que estamos en una estimacion gruesa de portadora
                datosMostrar = fft[:,0:1]
                frecuenciaPortadoraRecv,detectado = sistema.decidirFrecuenciaPortadora(fft[:,0],fft[:,1],threshold)
                
                if detectado:
                    estado = 'espera'
                else:
                    estado = 'portadora'                   
                
            elif estado =='portadora':
                #en este caso se hace la estimacion de la frecuencia
                controller.setPortadoraRecepcion(frecuenciaPortadoraRecv)
                print("Se cambia la frecuencia de portadora de recepcion a {}".format(frecuenciaPortadoraRecv))
            elif estado =='espera':
                print("se ha encontrado algo en la frecuencia {}".format(frecuenciaPortadoraRecv))
                
            elif estado =='transmision':
                #en este caso se hace la estimacion de la frecuencia
                a = 1
            elif estado =='analisis':
                #en este caso se hace la estimacion de la frecuencia
                a = 1

        
        hiloGraficas.close()

        print("Hilos terminados")   

	    
