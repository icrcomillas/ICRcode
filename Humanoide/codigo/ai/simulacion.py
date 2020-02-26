''
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
MARGEN_CAIDA = 1 #altura a la que se considera que ha caido el robot
ID_ROOT = 1 #id del link utilizado para coger la velocidad total del objeto
POSICION_INICIAL = [0,0,1.5]
ORIENTACION_INICIAL=[0,0,0,45]
PENALIZACION = 100
NOMBRE_FICHERO_EVAL = 'datos\q_eval.h5',      #ficheros en los que se guardan los modelos de la red neuronal
NOMBRE_FICHERO_TARGET='datos\q_next.h5'
FICHERO = "grafica_rendimiento.png"     #fichero que guarda el rendimiento de la red neuronal
FUERZA_MAXIMA =500              #FUERZA MÁXIMA QUE SE APLICA EN CADA UNION
INCREMENTO_UNION = 0.1          #CUANTO SE SUMO RESTA CADA UNION EN CADA ITERACION

GUI = True                      #para decidir si poner gui o no
#clase del entorno de simulacion
class entorno():
    DIMENSION_OBSERVACION = 104
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
        p.setRealTimeSimulation(1)
        #se nombra una variable de iteración para ver cuantos segundos lleva el robot de pie, y así premiarlo
        self.iteracion = 0
        
        return
    def cargarRobot(self,posicion_inicial,orientacion_inicial):
             
        #pongo gravedad
    
        
       
        #cargo el fichero del robot
       
        self.robot = p.loadURDF("humanoid.urdf", posicion_inicial, orientacion_inicial)
        numero_servos = p.getNumJoints(self.robot)
        return numero_servos
    def reset(self):
        #p.removeBody(self.robot)
        p.resetSimulation() 
        p.setGravity(0,0,-9.8)
        p.setRealTimeSimulation(1)
        self.plano = p.loadURDF("plane.urdf")   
        #se carga el robot de nuevo
        self.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
        self.iteracion = 0
        estado = self.estado()
        self.time = time.time()     #cogemos el tiempo cuando se resetea el entorno
        return estado
    def step(self,accion,servo):
        self.iteracion = self.iteracion +1
        self.accion(accion,servo)
        #p.stepSimulation()
        
        #vemos el estado del entorno despues de ejecutar la accion
        estado_actual= self.estado()
        estado_actual[103] = servo
      

        score = self.reward(estado_actual)
        if estado_actual[102] ==1:
            flag = True
        else:
            flag = False  #booleano utilizado para establecer si se ha llegado al final del proceso o no

        return score,estado_actual,flag
    def accion(self,accion, servo):
        estado = self.estado()
        indice = servo-1
       
        #print(accion)
        
        if accion == 0:
           posicion = estado[indice] + INCREMENTO_UNION         #mira la posicion el momento y la aumenta
        elif accion == 2:
            posicion = estado[indice]-INCREMENTO_UNION          #mira la posicion el momento y la diminuye
        elif accion == 1:
            posicion = estado[indice]
        
        
        p.setJointMotorControl2(self.robot, jointIndex = servo,controlMode = p.POSITION_CONTROL,targetPosition = posicion,force =FUERZA_MAXIMA)
        
        return
    def reward(self,estado):
        tiempo= (time.time() - self.time)               #tiempo que se ha estado dentro del mismo
        if estado[102] == 1:#se ha caido el robot, el indice hay que cambiarlo
            score = -200000
        else:
            score =  tiempo*RECOMPENSA_ITERACION - sum(estado[0:self.num_uniones])*PENALIZACION -sum(estado[self.num_uniones:2*self.num_uniones])*PENALIZACION #resta el torque y las velocidades al reward
        
        return score
    def estado(self):
        self.num_uniones = p.getNumJoints(self.robot)
        #creo el array para meter la informacion de velocidad y posicion de las uniones
        posicion = np.zeros((p.getNumJoints(self.robot)),dtype= float)
        velocidad = np.zeros((p.getNumJoints(self.robot)),dtype= float)
        torque = np.zeros((p.getNumJoints(self.robot)),dtype= float)#fuerza aplicada por cada union

        for i in range(p.getNumJoints(self.robot)):
            
            #recibo los datos de cada uno, posicion y velocidad
            velocidad[i], posicion[i],fuerzas, torque[i] = p.getJointState(self.robot,i)
            
        #para conseguir la velocidad del centro de masa, considero como centro de masa el "link" del pecho
        WorldPosition,WorldOrientation,localInertialFramePosition,localInertialFrameOrientation,LinkFramePosition,LinkFrameOrientation,velocidad_general,aceleracion = p.getLinkState(self.robot,2,ID_ROOT)
        if WorldPosition[2] < MARGEN_CAIDA or WorldPosition[0] >5 or WorldPosition[0]<-5 or WorldPosition[1] >5 or WorldPosition[1]<-5 or WorldPosition[1] >5 or WorldPosition[1]<-5  :
            caido = 1
            
        else: 
            caido = 0
        #permite saber la posiocion del cuerpo para posteriormente ajustar la camara
        self.posicion = WorldPosition
        #ver si los dos pies estás paralelos (opcional)
        servo = 0
        info_uniones = np.hstack((posicion,velocidad,torque,WorldOrientation[0:3],caido,servo))
        info_uniones = np.around(info_uniones,1)
    
        return info_uniones
    def CambiarCamara(self):#funcion que permite ajustar la camara de visualización
        p.resetDebugVisualizerCamera(5,50,-35,self.posicion)
        return
 
    def CerrarEntorno(self):
        p.disconnect()

        return


if __name__ == '__main__':
    env = entorno()
    numero_servos =env.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
    contador_episodios = 0

    if os.path.isdir("datos"):
        a = 1
    else:
        os.mkdir("datos")
    load_checkpoint = False
    for fichero in os.listdir("datos"):
        if fichero == 'q_eval.h5' or fichero == 'q_target.h5':
            load_checkpoint = True
            print("se van a cargar los modelos de memoria")
    best_score = 10000
    agent = Agent(gamma=0.99, epsilon=1.0, alpha=0.0001,
                  input_dims=(env.DIMENSION_OBSERVACION,), n_actions=env.DIMENSION_ACCION, mem_size=25000,
                  eps_min=0.02, batch_size=32, replace=1000, eps_dec=1e-5)
                  

    if load_checkpoint:
        agent.load_models()

    scores, eps_history = [], []
    n_steps = 0
    env.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
    
    for i in range(NUMERO_EPISODIOS):
        done = False
        observation = env.reset()
        score = 0
        
        time.sleep(2)
        while not done:
            for servo in range(numero_servos):      #vamos a hacer que se itere por cada servo de forma independiente
                action = agent.choose_action(observation)
                reward, observation_, done = env.step(action,servo)
                env.CambiarCamara()     #se cambia la camara para poder ver mejor el objeto
                n_steps += 1
                score += reward
                contador_episodios += 1
                if contador_episodios == 50:
                    agent.save_models()
                    print("se van a guardar los modelos en memoria")
                if not load_checkpoint:
                    agent.store_transition(observation, action,reward, observation_, int(done))
                    agent.learn()
            
                observation = observation_

            scores.append(score)
        
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
         