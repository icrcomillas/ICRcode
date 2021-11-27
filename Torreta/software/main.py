import json
import numpy as np
import threading
import time
from plutoController import Controller,Operacion,Sistema,Graficas
from maquina_estados import MaquinaEstados

global longitud_datos
global controller
global sistema
global gpu

def recibirDatos():
    datosNuevos = controller.rx()
    #se diezman los datos por un valor de 2
    #datosNuevos = datosNuevos[::M_diezmado]

    datosNuevos = np.append([datosNuevos],[np.array(frecuenciaPortadoraRecv)])
    #se calcula la fft de la secuencia
    
    if gpu:
        return operacion.calcularEspectroGPU(datosNuevos)
    else:
        return operacion.calcularEspectro(datosNuevos)

    

def transmitirDatos():

    # Llamada a la funcion para generar la señal de ruido
        # media nula 
        # varianza ?
        #longitud ?
    media = 0
    varianza = 1
    longitud = 1000 # tambien se puede usar len(controller.rx())
    interferencia = sistema.generarRuido(media, varianza, longitud)

    # Se transmiten los datos 
    controller.tx(interferencia)

if __name__== '__main__':

        # Declaracion de variables

        limite_espera = 3 # Tiempo limite de espera en el estado Espera (s) (MODIFICABLE)
        limite_transmision = 3 # Tiempo limite de espera en el estado Espera (s) (MODIFICABLE)
        continuar = True
        M_diezmado = 2
        longitud_datos = 1024//M_diezmado   #Se calcula la longitud de los datos a procesar para poder saber la posicion del indice de la frecuencia de muestreo
        
        with open('configuracion.json') as json_file:
            ficheroJson = json.load(json_file)

        #se incicializan las variables iniciales
        frecuenciaPortadoraRecv = ficheroJson['c_rx_default']
        frecuenciaPortadoraTrans = ficheroJson['c_tx_default']
        samplerate = ficheroJson['samplerate']
        filtroAnalog = ficheroJson['f_analog']
        ganancia = ficheroJson['ganancia']
        threshold_1 = ficheroJson['threshold_1']
        gpu = ficheroJson['gpu']
        
        #se inicializa el controlador de la placa
        controller = Controller()
        controller.inicializarPlaca(frecuenciaPortadoraRecv,frecuenciaPortadoraTrans,samplerate,filtroAnalog,ganancia)

        #objeto para realizar las operaciones
        operacion = Operacion(samplerate)

        #objeto para la toma de decisiones
        sistema = Sistema(ficheroJson['salto_frecuencia'],ficheroJson['frecuencia_min'],ficheroJson['frecuencia_max'])
        
        #objeto de graficas
        graficas = Graficas()
        #se crea el hilo para mostrar los resultados
        hiloGraficas = threading.Thread(target=graficas.runGraficas, daemon = True)
        #se arranca el hilo
        hiloGraficas.start()
        print("Se ha inicializado el sistema")
        contradorMuestras = 0 #contador para saber si se ha detectado algo en 

        # Se crea una instancia de la máquina de estados
        maquina = MaquinaEstados()
        #tiempo para esperar a que arranque el hilo de graficas
        time.sleep(5)
        while continuar:

            #logica de control de la aplicación	

            if str(maquina.estado) == 'Arranque':
                
                

                # Si ha ido todo OK se modifica el estado
                maquina.on_event('OK')

            elif str(maquina.estado) == 'Recepcion':

                fft = recibirDatos()

                # Si ha ido todo OK se modifica el estado
                maquina.on_event('OK')

            elif str(maquina.estado) == 'EstimacionGruesa': 

                #significa que estamos en una estimacion gruesa de portadora

                graficas.updateGrafica(fft[:,0:2])
                frecuenciaPortadoraRecv,detectado = sistema.decidirFrecuenciaPortadora(frecuenciaPortadoraRecv,fft[:,0],fft[:,1],threshold_1)
                
                # Si ha ido todo OK se modifica el estado
                if detectado:
                    maquina.on_event('detectado')
                    # TODO: Aquí se debería empezar a transmitir se inicia el iterador
                    i = 0
                    
                elif not detectado:
                    maquina.on_event('no_detectado')                 
                
            elif str(maquina.estado) =='ModificacionPortadora':

                #en este caso se hace la estimacion de la frecuencia
                controller.setPortadoraRecepcion(frecuenciaPortadoraRecv)
                print("Se cambia la frecuencia de portadora de recepcion a {}".format(frecuenciaPortadoraRecv))

                # Si ha ido todo OK se modifica el estado
                maquina.on_event('OK')

            elif str(maquina.estado) == 'Espera':

                # Estado de confirmacion de que existe algo en la banda detectada
                              
                # Si ha ido todo OK se modifica el estado, en funcion del valor del temporizador de espera
                if i >= limite_espera:
                    maquina.on_event('limite_espera')
                    # TODO: empezar a transmitir
                    tiempo_inicial = time.time()
                else:
                    fft = recibirDatos()
                    graficas.updateGrafica(fft[:,0:2])
                    detectado = sistema.analizarEspectroFrecuenciaTf(fft[:,0],fft[:,1],threshold_1)
                    if detectado:
                        # Se incrementa el iterador de espera
                        i += 1
                    else:
                        maquina.on_event('no_detectado')
                
            elif str(maquina.estado) =='Transmision':

                # Estado de trasmisión
                
                # .... (logica de transmision)
                
                tiempo_pasado= time.time()-tiempo_inicial
                #print("Se transmite en la frecuencia {}".format(frecuenciaPortadoraRecv))

                # Si ha ido todo OK se modifica el estado, en funcion del valor del temporizador de trasmisión
                if tiempo_pasado >= limite_transmision:
                    # TODO se para la tansmisión
                    tiempo_inicial = time.time()
                    maquina.on_event('limite_transmision')

            elif str(maquina.estado) =='Analisis':

                # Estado de analisis
                
                # .... (logica de analisis)

                # TODO: Revisar el print
                print("Analizando el margen de frecuencias {}".format(frecuenciaPortadoraRecv))
                fft = recibirDatos()
                graficas.updateGrafica(fft[:,0:2])
                detectado = sistema.analizarEspectroFrecuenciaTf(fft[:,0],fft[:,1],threshold_1)

                # Si ha ido todo OK se modifica el estado, en funcion del valor del temporizador de trasmisión
                if detectado:
                    maquina.on_event('detectado')
                elif not detectado:
                    maquina.on_event('no_detectado')

            elif str(maquina.estado) == 'Fallo_Mortal':

                continuar = False
                
                # TODO: Incluir la lógica asociada a fallos en el maquina de estados, almacenando en la variable
                # 'estado_error' el último esatdo antes de llegar a Fallo Mortal
                print('Ha ocurrido un fallo mortal en el estado de ', estado_error)
     
        hiloGraficas.close()

        print("Hilos terminados")   
