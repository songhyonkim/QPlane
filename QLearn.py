import numpy as np
import random

class QLearn():

    def __init__(self, n_stat, n_acts, gamm, lr, eps, dec, min):
        self.n_states = n_stat
        self.n_actions = n_acts
        self.gamma = gamm
        self.learningRate = lr
        self.epsilon = eps
        self.decay = dec
        self.epsMin = min
        self.qTable = np.zeros( [self.n_states, self.n_actions] )

    # get action for current state
    def selectAction(self, state, episode, n_epochs):
        explorationTreshold = random.uniform(0, 1)
        explore = False
        # Check if explore or explore with current epsilon vs random number between 0 and 1
        if explorationTreshold > self.epsilon:
            action = np.argmax(self.qTable[state,:])  # explore, which means predicted action
        else:
            action = int(random.uniform(0, self.n_actions))  # Explore, which means random action
            explore = True
        # decay epsilon
        if(self.epsilon > self.epsMin):  # decay the value
            self.epsilon = self.epsilon * (1 - self.decay)
        elif(self.epsilon < self.epsMin):  # if decayed too far set to min
            self.epsilon = self.epsMin

        return action, explore

    # update q table
    def learn(self, state, action, reward, new_state):
        self.qTable[state, action] = (1 - self.learningRate) * self.qTable[state, action] + self.learningRate * (reward + self.gamma * np.max(self.qTable[new_state, :]))  # Bellman
