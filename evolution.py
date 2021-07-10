from player import Player
import numpy as np
from config import CONFIG
import random


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):
        rand= random.uniform(0, 1)
        if(rand<0.25):
            child.nn.layer1_weights+= np.random.normal(size=child.nn.layer1_weights.shape)
            child.nn.layer2_weights+= np.random.normal(size=child.nn.layer2_weights.shape)
            child.nn.biases1 += np.random.normal(size=child.nn.biases1.shape)
            child.nn.biases2 += np.random.normal(size=child.nn.biases2.shape)
        return child


    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:
            result=[]
            layer1shape=prev_players[0].nn.layer1_weights.shape
            layer2shape=prev_players[0].nn.layer2_weights.shape
            bias1shape=prev_players[0].nn.biases1.shape
            bias2shape=prev_players[0].nn.biases2.shape
            for _ in range(num_players):
                child = Player(self.mode)
                parents=random.sample(prev_players,2)
                child.nn.layer1_weights= np.block([[parents[0].nn.layer1_weights[:layer1shape[0]//2]],[parents[1].nn.layer1_weights[layer1shape[0]//2:layer1shape[0]]]])
                child.nn.layer2_weights= np.block([[parents[0].nn.layer2_weights[:layer2shape[0]//2]],[parents[1].nn.layer2_weights[layer2shape[0]//2:layer2shape[0]]]])
                child.nn.biases1 = np.block([[parents[0].nn.biases1[:bias1shape[0]//2]],[parents[1].nn.biases1[bias1shape[0]//2:bias1shape[0]]]])
                child.nn.biases2 = np.block([[parents[0].nn.biases2[:bias2shape[0]//2]],[parents[1].nn.biases2[bias2shape[0]//2:bias2shape[0]]]])
                self.mutate(child)
                result.append(child)
            return result

    def next_population_selection(self, players, num_players,gen_num):

        # TODO (additional): plotting

        #using Q-tournoment algorithm for selection and Mu+landa
        result = []
        Q = gen_num
        for _ in range(num_players):
            random.sample(players,Q)
            result.append(max(random.sample(players,Q), key=lambda item: item.fitness))

        return result
