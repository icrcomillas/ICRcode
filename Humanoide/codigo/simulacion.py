
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
NUMERO_EPISODIOS = 20_000
RECOMPENSA_ITERACION = 1 #recompensa que se da por cumplir cada iteración
MARGEN_CAIDA = 10 #altura a la que se considera que ha caido el robot
ID_ROOT = 1 #id del link utilizado para coger la velocidad total del objeto
POSICION_INICIAL = [0,0,2]
ORIENTACION_INICIAL=[0,0,0,45]
PENALIZACION = 100

FUERZA_MAXIMA =500              #FUERZA MÁXIMA QUE SE APLICA EN CADA UNION
INCREMENTO_UNION = 0.5          #CUANTO SE SUMO RESTA CADA UNION EN CADA ITERACION
NUMERO_SERVOS = 33

#clase del entorno de simulacion
class entorno():
    DIMENSION_OBSERVACION = 105
    DIMENSION_ACCION= 3
    def __init__(self):
        #self.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
        self.entorno = p.connect(p.GUI)
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
        print(p.getNumJoints(self.robot))
        return
    def reset(self):
        p.resetSimulation()
        p.setGravity(0,0,-9.8)
        p.setRealTimeSimulation(1)
        self.plano = p.loadURDF("plane.urdf")   
        #se carga el robot de nuevo
        self.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
        self.iteracion = 0
        estado = self.estado()
        return estado
    def step(self,accion,servo):
        self.iteracion = self.iteracion +1
        self.accion(accion,servo)
        #p.stepSimulation()
        #hay que crear el reward
        #vemos el estado del entorno despues de eejcutar la accion
        estado_actual= self.estado()
        estado_actual[50] = servo
      

        score = self.reward(estado_actual)
        if estado_actual[49] ==1:
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
        if estado[49] == 1:#se ha caido el robot, el indice hay que cambiarlo
            score = -200
        else:
            score = self.iteracion*RECOMPENSA_ITERACION - sum(estado[0:self.num_uniones])*PENALIZACION -sum(estado[self.num_uniones:2*self.num_uniones])*PENALIZACION #resta el torque y las velocidades al reward
        
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
        if WorldPosition[2] < MARGEN_CAIDA:
            caido = 1
            
        else: 
            caido = 0
        #ver si los dos pies estás paralelos (opcional)
        servo = 0
        info_uniones = np.hstack((posicion,velocidad,torque,WorldOrientation,caido,servo))
        info_uniones = np.around(info_uniones,1)
    
        return info_uniones
 
 


if __name__ == '__main__':
    env = entorno()
    env.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
  
    fichero = "grafica_rendimiento.png"
    num_games = 500
    load_checkpoint = False
    best_score = -21
    agent = Agent(gamma=0.99, epsilon=1.0, alpha=0.0001,
                  input_dims=(env.DIMENSION_OBSERVACION,), n_actions=env.DIMENSION_ACCION, mem_size=25000,
                  eps_min=0.02, batch_size=32, replace=1000, eps_dec=1e-5)
                  

    if load_checkpoint:
        agent.load_models()

    scores, eps_history = [], []
    n_steps = 0
    env.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
    for i in range(num_games):
        done = False
        observation = env.reset()
        score = 0
        while not done:
            for servo in range(NUMERO_SERVOS):      #vamos a hacer que se itere por cada servo de forma independiente
                action = agent.choose_action(observation)
                reward, observation_, done = env.step(action,servo)
                print(observation)
                n_steps += 1
                score += reward
                print("se ha llegado punto 1")
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

    x = [i+1 for i in range(num_games)]
    plot_learning_curve(x, scores, eps_history, fichero)
