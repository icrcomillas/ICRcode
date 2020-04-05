
import pybullet as p
import numpy as np
from collections import deque
import time
import random
import os
import numpy as np
from dqn_keras import Agent
from utils import plotLearning



# Environment settings
NUMERO_EPISODIOS = 200000
RECOMPENSA_ITERACION = 1 #recompensa que se da por cumplir cada iteración
MARGEN_CAIDA = 0.5 #altura a la que se considera que ha caido el robot ###cambiado a 0.5
ID_ROOT = 1 #id del link utilizado para coger la velocidad total del objeto
POSICION_INICIAL = [0,0,0.5]
ORIENTACION_INICIAL=[0,0,0,45]
PENALIZACION = 10
NOMBRE_FICHERO_EVAL = 'datos\q_eval.h5',      #ficheros en los que se guardan los modelos de la red neuronal
NOMBRE_FICHERO_TARGET='datos\q_next.h5'
FICHERO = "grafica_rendimiento.png"     #fichero que guarda el rendimiento de la red neuronal
FUERZA_MAXIMA =500              #fuerza máxima que se aplicada a cada union
INCREMENTO_UNION = 0.1          #cuanto se suma o se resta a cada unión

GUI = True                      #para decidir si poner gui o no

#clase del entorno de simulacion
class entorno():
    DIMENSION_OBSERVACION = 41
    DIMENSION_ACCION= 3
    def __init__(self):
        #self.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
        if GUI == True :
            self.entorno = p.connect(p.GUI)
        else:
            self.entorno = p.connect(p.DIRECT)
         #cargo el plano
        self.plano = p.loadURDF("plane.urdf")
        p.setGravity(0,0,-9.8)
        p.setRealTimeSimulation(0)
        #se añade un slider para determinar la probabilidad de que reciba un golpe
        self.probabilidad = p.addUserDebugParameter("Probabilidad de fuerza",0,1,0.5)

        #indice del servo en el array de estados
        self.indiceServo = entorno.DIMENSION_OBSERVACION -1 
        self.indiceCaido = entorno.DIMENSION_OBSERVACION -2
        return
    def cargarRobot(self,posicion_inicial,orientacion_inicial):    
       
        #cargo el fichero del robot
       
        self.robot = p.loadURDF("humanoid.urdf", [0,0,1.3], [0,0,0,45])
        self.numeroServos = p.getNumJoints(self.robot)
        #array para guardar las posiciones de las uniones
        self.angulos = np.zeros((self.numeroServos,),dtype = float)
        
        for jointIndex in range (p.getNumJoints(self.robot)):
	        p.resetJointState(self.robot,jointIndex,self.angulos[jointIndex])

        return self.numeroServos

    def reset(self):
        #se resetea 
        p.resetSimulation() 
        p.setGravity(0,0,-9.8)
        p.setRealTimeSimulation(0)
        self.plano = p.loadURDF("plane.urdf")   
        #se carga el robot de nuevo
        self.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
        self.iteracion = 0
        estado = self.estado()
        self.time = time.time()     #cogemos el tiempo cuando se resetea el entorno
        #se resetean todas las uniones
        for jointIndex in range (p.getNumJoints(self.robot)):            
	        p.resetJointState(self.robot,jointIndex,self. angulos[jointIndex])
        return estado

    def step(self,accion,servo):
        self.iteracion = self.iteracion +1
        self.accion(accion,servo)
        p.stepSimulation()
        
        #vemos el estado del entorno despues de ejecutar la accion
        estadoActual= self.estado()

        #se carga el servo actual en el array de estado
        estadoActual[self.indiceServo] = servo

        score = self.reward(estadoActual)
        #se aplica una fuerza aleatoria, en el caso de que el numero que sale sea mayor que 0,5
     

        #el ultimo return indica si se ha caido el robot o no (es el flag de la inteligencia artificial)
        return score,estadoActual,estadoActual[self.indiceCaido]

    def aplicarFuerzaExterna(self):
        link = random.randint(0,self.numeroServos-1)
        fuerzaAplicada = [random.randint(0,1000),random.randint(0,1000),random.randint(0,1000)]
        punto = [random.random(),random.random(),random.random()]
        if random.random() > p.readUserDebugParameter(self.probabilidad):
            print("se va a aplicar puerza externa")
            p.applyExternalForce(self.robot, link,fuerzaAplicada,punto,p.WORLD_FRAME)
            #se va a dibujar una linea indicando el vector de fuerza
            punto2 = [punto[0]+fuerzaAplicada[0],punto[1]+fuerzaAplicada[1],punto[2]+fuerzaAplicada[2]]
            p.addUserDebugLine(punto,punto2,[1,0,0],1,0,5)
        return
        #el ultimo return indica si se ha caido el robot o no (es el flag de la inteligencia artificial)
        
    def accion(self,accion, servo):
        estado = self.estado()
        #indice del angulo del servo seleccionado, en el array de posiciones
        indice = servo
       
       
        
        if accion == 0:
           posicion = self.angulos[indice] + INCREMENTO_UNION         #mira la posicion el momento y la aumenta
           self.angulos[indice] = posicion                                    #guarda el nuevo angulo 
        elif accion == 2:
            posicion = self.angulos[indice]-INCREMENTO_UNION          #mira la posicion el momento y la diminuye
            self.angulos[indice] = posicion                                    #guarda el nuevo angulo 
        elif accion == 1:
            posicion = self.angulos[indice]                           #no se hace nada, se mantiene la posiciobn del servo
        
        
        p.setJointMotorControl2(self.robot, jointIndex = servo,controlMode = p.POSITION_CONTROL,targetPosition = posicion,force =FUERZA_MAXIMA)
        
        return
    def reward(self,estado):
        tiempo= (time.time() - self.time)               #tiempo que se ha estado dentro del mismo
        if estado[self.indiceCaido] == 1:#se ha caido el robot, el indice hay que cambiarlo
            score = -20000
        else:
            #score =  tiempo*tiempo*RECOMPENSA_ITERACION - sum(estado[0:3])*PENALIZACION #resta la aceleracion
            score =  self.iteracion*RECOMPENSA_ITERACION - sum(estado[0:3])*PENALIZACION #resta la aceleracion
        
        return score
    def estado(self):
        

        #creo el array para meter la informacion de velocidad y posicion de las uniones
        posicion = np.zeros((self.numeroServos),dtype= float)
        torque = np.zeros((self.numeroServos),dtype= float)
        
        arrayAceleracion = np.zeros((3),dtype = float)
            
        #para conseguir la velocidad del centro de masa, considero como centro de masa el "link" del pecho        
        WorldPosition = p.getLinkState(self.robot,2,ID_ROOT)[0]
        WorldOrientation = p.getLinkState(self.robot,2,ID_ROOT)[1]
        aceleracion = p.getLinkState(self.robot,2,ID_ROOT)[7]
        
        #logica para decidir si se ha caido o no el robot
        if WorldPosition[2] < MARGEN_CAIDA or WorldPosition[0] >5 or WorldPosition[0]<-5 or WorldPosition[1] >5 or WorldPosition[1]<-5 or WorldPosition[1] >5 or WorldPosition[1]<-5  :
            caido = 1
            
        else: 
            caido = 0

        #posicion del cuerpo para posteriormente ajustar la camara
        self.posicion = WorldPosition

        #se introduce en todas las iteraciones un valor de servo a cero, para luego poder sobreescribirlo, es una forma de no tener que modificar dimensiones de arrays
        servo = 0

        #se crea un array de aceleraciones, para luego poder pasar todas las aceleraciones a la vez a la ai
        arrayAceleracion = [aceleracion[0], aceleracion[1],aceleracion[2]]

        #se junta toda la informacion a enviar, aceleraciones, orientacion, angulo de los servos, si se ha caido o no, y el servo que se esta tratando
        info_uniones = np.hstack((arrayAceleracion,WorldOrientation[0:3],self.angulos,caido,servo))
        info_uniones = np.around(info_uniones,2)
        
    
        return info_uniones
    def CambiarCamara(self):#funcion que permite ajustar la camara de visualización
        p.resetDebugVisualizerCamera(5,50,-35,self.posicion)
        return
 
    def CerrarEntorno(self):
        p.disconnect()

        return


if __name__ == '__main__':
    #se crea el entorno a utilizar, y se carga el robot en el 
    env = entorno()
    numero_servos =env.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
    contadorEpisodios = 0

    best_score = 10000
    agent = Agent(gamma=0.99, epsilon=0.2, alpha=0.0001,
                  input_dims=(env.DIMENSION_OBSERVACION,), n_actions=env.DIMENSION_ACCION, mem_size=25000,batch_size=32, replace=1000, eps_dec=1e-5)
                  

    if os.path.isdir("datos"):
        for fichero in os.listdir("datos"):
            if fichero == 'q_eval.h5' or fichero == 'q_target.h5':
                load_checkpoint = True
                agent.load_models()
                print("se van a cargar los modelos de memoria")
        
    else:
        os.mkdir("datos")
    load_checkpoint = False
    

        

    scores, eps_history = [], []
    n_steps = 0
    env.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
    
    for i in range(NUMERO_EPISODIOS):
        done = False
        observation = env.reset()
        score = 0
        
      
        contadorEpisodios += 1
        while not done:
            env.aplicarFuerzaExterna()
            for servo in range(numero_servos):      #vamos a hacer que se itere por cada servo de forma independiente
                action = agent.choose_action(observation)
                reward, observation_, done = env.step(action,servo)
                env.CambiarCamara()     #se cambia la camara para poder ver mejor el objeto
                n_steps += 1
                score += reward
                
                
                if not load_checkpoint:
                    agent.store_transition(observation, action,reward, observation_, int(done))
                    agent.learn()
            
                observation = observation_

            scores.append(score)
            #se guarda el episodio
        if contadorEpisodios == 3:
            agent.save_models()
            print("se van a guardar los modelos en memoria")
            contadorEpisodios = 0

        avg_score = np.mean(scores[-100:])
        print('episode: ', i,'score: ', score,
             ' average score %.3f' % avg_score,
            'epsilon %.2f' % agent.epsilon, 'steps', n_steps)
        if avg_score > best_score:
            agent.save_models()
            print('avg score %.2f better than best score %.2f, saving model' % (
                  avg_score, best_score))
            best_score = avg_score

        eps_history.append(agent.epsilon)
    env.CerrarEntorno()
    x = [i+1 for i in range(NUMERO_EPISODIOS)]
    #scores.pop(0)       #se borra el primer elemento ya que por razones desconocinas el programa introduce un elemento de más
    plotLearning(x, scores, eps_history, FICHERO)
         