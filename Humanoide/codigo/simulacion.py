
import pybullet as p
import numpy as np
import keras.backend.tensorflow_backend as backend
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Activation, Flatten
from keras.optimizers import Adam
from keras.callbacks import TensorBoard
import tensorflow as tf
from collections import deque
import time
import random
import os

DISCOUNT = 0.99
REPLAY_MEMORY_SIZE = 50_000  # How many last steps to keep for model training
MIN_REPLAY_MEMORY_SIZE = 1_000  # Minimum number of steps in a memory to start training
MINIBATCH_SIZE = 64  # How many steps (samples) to use for training
UPDATE_TARGET_EVERY = 5  # Terminal states (end of episodes)
MODEL_NAME = 'prueba1'
MIN_REWARD = -200  # For model save
MEMORY_FRACTION = 0.20

# Environment settings
NUMERO_EPISODIOS = 20_000

# Exploration settings
epsilon = 1  # not a constant, going to be decayed
EPSILON_DECAY = 0.99975
MIN_EPSILON = 0.001

#  Stats settings
AGGREGATE_STATS_EVERY = 50  # episodes
SHOW_PREVIEW = False

RECOMPENSA_ITERACION = 1 #recompensa que se da por cumplir cada iteración
MARGEN_CAIDA = 2 #altura a la que se considera que ha caido el robot
ID_ROOT = 4 #id del link utilizado para coger la velocidad total del objeto
POSICION_INICIAL = [0,0,8]
ORIENTACION_INICIAL=[45,0,0,45]
PENALIZACION = 1

FUERZA_MAXIMA =500              #FUERZA MÁXIMA QUE SE APLICA EN CADA UNION
INCREMENTO_UNION = 0.5          #CUANTO SE SUMO RESTA CADA UNION EN CADA ITERACION

#clase del entorno de simulacion
class entorno():
    DIMENSION_OBSERVACION = 49
    DIMENSION_ACCION= 3
    def __init__(self):
        self.entorno = p.connect(p.GUI)     
        #pongo gravedad
    
        p.setGravity(0,0,-9.8)
        p.setRealTimeSimulation(1)
        #cargo el plano
        self.plano = p.loadURDF("plane.urdf")
        #cargo el fichero del robot
        self.cargarRobot(POSICION_INICIAL,ORIENTACION_INICIAL)
        
        #se nombra una variable de iteración para ver cuantos segundos lleva el robot de pie, y así premiarlo
        self.iteracion = 0
        return
    def cargarRobot(self,posicion_inicial,orientacion_inicial):
        self.robot = p.loadURDF("humanoide.urdf",posicion_inicial,orientacion_inicial)
        return
    def reset(self):
        p.resetSimulation()
        p.setGravity(0,0,-10)
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
        p.stepSimulation()
        #hay que crear el reward
        #vemos el estado del entorno despues de eejcutar la accion
        estado_actual,posicion_actual= self.estado()

        score = self.reward(estado_actual)
        flag  = False  #booleano utilizado para establecer si se ha llegado al final del proceso o no

        return score,estado_actual,flag
    def accion(self,accion, servo):
        indice = servo-1
        if accion == [1,0,0]:
           posicion = estado[indice] + INCREMENTO_UNION         #mira la posicion el momento y la aumenta
        elif accion == [0,1,0]:
            posicion = estado[indice]-INCREMENTO_UNION          #mira la posicion el momento y la diminuye
        elif accion == [0,0,1]:
            posicion = estado[indice]
        p.setJointMotorControl2(self.robot, jointIndex = servo,controlMode = p.POSITION_CONTROL,targePosition = posicion,force =FUERZA_MAXIMA)
        p.stepSimulation()
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
            
            #recibo los datos de cadauni, posicion y velocidad
            velocidad[i], posicion[i],fuerzas, torque[i] = p.getJointState(self.robot,i)
            
        #para conseguir la velocidad del centro de masa, considero como centro de masa el "link" del pecho
        WorldPosition,WorldOrientation,localInertialFramePosition,localInertialFrameOrientation,LinkFramePosition,LinkFrameOrientation,velocidad_general,aceleracion = p.getLinkState(self.robot,2,ID_ROOT)
        if WorldPosition[2] < MARGEN_CAIDA:
            caido = 1
            
        else: 
            caido = 0
        #ver si los dos pies estás paralelos (opcional)
        
        info_uniones = np.hstack((posicion,velocidad,torque,WorldOrientation,caido))
        info_uniones = np.round(info_uniones,2)
        return info_uniones, WorldOrientation
 
 
entorno = entorno()

# For stats
ep_rewards = [-200]

# For more repetitive results
random.seed(1)
np.random.seed(1)
tf.set_random_seed(1)


# Own Tensorboard class
class ModifiedTensorBoard(TensorBoard):

    # Overriding init to set initial step and writer (we want one log file for all .fit() calls)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.step = 1
        self.writer = tf.summary.FileWriter(self.log_dir)

    # Overriding this method to stop creating default log writer
    def set_model(self, model):
        pass

    # Overrided, saves logs with our step number
    # (otherwise every .fit() will start writing from 0th step)
    def on_epoch_end(self, epoch, logs=None):
        self.update_stats(**logs)

    # Overrided
    # We train for one batch only, no need to save anything at epoch end
    def on_batch_end(self, batch, logs=None):
        pass

    # Overrided, so won't close writer
    def on_train_end(self, _):
        pass

    # Custom method for saving own metrics
    # Creates writer, writes custom metrics and closes writer
    def update_stats(self, **stats):
        self._write_logs(stats, self.step)


# Agent class
class DQNAgent:
    def __init__(self):

        # Main model
        self.model = self.create_model()

        # Target network
        self.target_model = self.create_model()
        self.target_model.set_weights(self.model.get_weights())

        # An array with last n steps for training
        self.replay_memory = deque(maxlen=REPLAY_MEMORY_SIZE)

        # Custom tensorboard object
        self.tensorboard = ModifiedTensorBoard(log_dir="logs/{}-{}".format(MODEL_NAME, int(time.time())))

        # Used to count when to update target network with main network's weights
        self.target_update_counter = 0

    def create_model(self):
        model = Sequential()

        model.add(Conv2D(256, (3, 3), input_shape=entorno.DIMENSION_OBSERVACION))  # OBSERVATION_SPACE_VALUES = (10, 10, 3) a 10x10 RGB image.
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))

        model.add(Conv2D(256, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))

        model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
        model.add(Dense(64))

        model.add(Dense(entorno.DIMENSION_ACCION, activation='linear'))  # ACTION_SPACE_SIZE = how many choices (9)
        model.compile(loss="mse", optimizer=Adam(lr=0.001), metrics=['accuracy'])
        return model

    # Adds step's data to a memory replay array
    # (observation space, action, reward, new observation space, done)
    def update_replay_memory(self, transition):
        self.replay_memory.append(transition)

    # Trains main network every step during episode
    def train(self, terminal_state, step):

        # Start training only if certain number of samples is already saved
        if len(self.replay_memory) < MIN_REPLAY_MEMORY_SIZE:
            return

        # Get a minibatch of random samples from memory replay table
        minibatch = random.sample(self.replay_memory, MINIBATCH_SIZE)

        # Get current states from minibatch, then query NN model for Q values
        current_states = np.array([transition[0] for transition in minibatch])/255
        current_qs_list = self.model.predict(current_states)

        # Get future states from minibatch, then query NN model for Q values
        # When using target network, query it, otherwise main network should be queried
        new_current_states = np.array([transition[3] for transition in minibatch])/255
        future_qs_list = self.target_model.predict(new_current_states)

        X = []
        y = []

        # Now we need to enumerate our batches
        for index, (current_state, action, reward, new_current_state, done) in enumerate(minibatch):

            # If not a terminal state, get new q from future states, otherwise set it to 0
            # almost like with Q Learning, but we use just part of equation here
            if not done:
                max_future_q = np.max(future_qs_list[index])
                new_q = reward + DISCOUNT * max_future_q
            else:
                new_q = reward

            # Update Q value for given state
            current_qs = current_qs_list[index]
            current_qs[action] = new_q

            # And append to our training data
            X.append(current_state)
            y.append(current_qs)

        # Fit on all samples as one batch, log only on terminal state
        self.model.fit(np.array(X)/255, np.array(y), batch_size=MINIBATCH_SIZE, verbose=0, shuffle=False, callbacks=[self.tensorboard] if terminal_state else None)

        # Update target network counter every episode
        if terminal_state:
            self.target_update_counter += 1

        # If counter reaches set value, update target network with weights of main network
        if self.target_update_counter > UPDATE_TARGET_EVERY:
            self.target_model.set_weights(self.model.get_weights())
            self.target_update_counter = 0

    # Queries main network for Q values given current observation space (environment state)
    def get_qs(self, state):
        return self.model.predict(np.array(state).reshape(-1, *state.shape)/255)[0]
# For stats
ep_rewards = [-200]

# For more repetitive results
random.seed(1)
np.random.seed(1)
tf.set_random_seed(1)

# Memory fraction, used mostly when trai8ning multiple agents
#gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=MEMORY_FRACTION)
#backend.set_session(tf.Session(config=tf.ConfigProto(gpu_options=gpu_options)))

# Create models folder
if not os.path.isdir('models'):
    os.makedirs('models')


if __name__ == '__main__':
    #creo el entorno

    agent = DQNAgent()
    while True:
        entorno.step()
    # Iterate over episodes
    for episode in range(NUMERO_EPISODIOS):

        # Update tensorboard step every episode
        agent.tensorboard.step = episode

        # Restarting episode - reset episode reward and step number
        episode_reward = 0
        step = 1

        # Reset environment and get initial state
        current_state = entorno.reset()

        # Reset flag and start iterating until episode ends
        done = False
        while not done:

            # This part stays mostly the same, the change is to query a model for Q values
            if np.random.random() > epsilon:
                # Get action from Q table
                action = np.argmax(agent.get_qs(current_state))
            else:
                # Get random action
                action = np.random.randint(0, entorno.ACTION_SPACE_SIZE)

            new_state, reward, done = entorno.step(action)

            # Transform new continous state to new discrete state and count reward
            episode_reward += reward

            # Every step we update replay memory and train main network
            agent.update_replay_memory((current_state, action, reward, new_state, done))
            agent.train(done, step)

            current_state = new_state
            step += 1

        # Append episode reward to a list and log stats (every given number of episodes)
        ep_rewards.append(episode_reward)
        if not episode % AGGREGATE_STATS_EVERY or episode == 1:
            average_reward = sum(ep_rewards[-AGGREGATE_STATS_EVERY:])/len(ep_rewards[-AGGREGATE_STATS_EVERY:])
            min_reward = min(ep_rewards[-AGGREGATE_STATS_EVERY:])
            max_reward = max(ep_rewards[-AGGREGATE_STATS_EVERY:])
            agent.tensorboard.update_stats(reward_avg=average_reward, reward_min=min_reward, reward_max=max_reward, epsilon=epsilon)

            # Save model, but only when min reward is greater or equal a set value
            if min_reward >= MIN_REWARD:
                agent.model.save(f'models/{MODEL_NAME}__{max_reward:_>7.2f}max_{average_reward:_>7.2f}avg_{min_reward:_>7.2f}min__{int(time.time())}.model')

        # Decay epsilon
        if epsilon > MIN_EPSILON:
            epsilon *= EPSILON_DECAY
            epsilon = max(MIN_EPSILON, epsilon)
            