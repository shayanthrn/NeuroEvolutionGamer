from player import Player
import numpy as np
from config import CONFIG
import random
import copy


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child,Standard_deviation,prob):
        rand= random.uniform(0, 1)
        if(rand<prob):
            child.nn.layer1_weights+= Standard_deviation*np.random.normal(size=child.nn.layer1_weights.shape)
            child.nn.layer2_weights+= Standard_deviation*np.random.normal(size=child.nn.layer2_weights.shape)
            child.nn.biases1 += Standard_deviation*np.random.normal(size=child.nn.biases1.shape)
            child.nn.biases2 += Standard_deviation*np.random.normal(size=child.nn.biases2.shape)


    def generate_new_population(self, num_players, prev_players=None):
        crossove_p = 1
        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:
            result=[]
            layer1shape=prev_players[0].nn.layer1_weights.shape
            layer2shape=prev_players[0].nn.layer2_weights.shape
            bias1shape=prev_players[0].nn.biases1.shape
            bias2shape=prev_players[0].nn.biases2.shape
            for _ in range(num_players-50):
                child = Player(self.mode)
                parents = [max(random.sample(prev_players,30), key=lambda item: item.fitness),random.sample(prev_players,1)[0]]
                child.nn.layer1_weights= np.block([[parents[0].nn.layer1_weights[:layer1shape[0]//2]],[parents[1].nn.layer1_weights[layer1shape[0]//2:layer1shape[0]]]])
                child.nn.layer2_weights= np.block([[parents[0].nn.layer2_weights[:layer2shape[0]//2]],[parents[1].nn.layer2_weights[layer2shape[0]//2:layer2shape[0]]]])
                child.nn.biases1 = np.block([[parents[0].nn.biases1[:bias1shape[0]//2]],[parents[1].nn.biases1[bias1shape[0]//2:bias1shape[0]]]])
                child.nn.biases2 = np.block([[parents[0].nn.biases2[:bias2shape[0]//2]],[parents[1].nn.biases2[bias2shape[0]//2:bias2shape[0]]]])
                self.mutate(child, 0.2, 0.9)
                result.append(child)
            for _ in range(50):
                child = Player(self.mode)
                self.mutate(child, 1, 0.2)
                result.append(child)
            random.shuffle(result)
            return result

    def next_population_selection(self, players, num_players,gen_num):
        fitness_sum = 0
        fitness_min = players[0].fitness
        fitness_max = players[0].fitness
        #Learning curve
        for player in players:
            fitness_sum += player.fitness
            if(player.fitness<fitness_min):
                fitness_min = player.fitness
            if(player.fitness> fitness_max):
                fitness_max = player.fitness
        fitness_avg = fitness_sum/len(players)
        file = open('learning_curve.txt','a')
        file.writelines(str(fitness_avg)+" "+str(fitness_max)+" "+str(fitness_min)+"\n")
        file.close()
        
        #using Q-tournoment algorithm for selection and Mu+landa
        result = []
        Q = gen_num
        # Q = 3
        i = 0
        # while(i<num_players):
        #     choice = max(random.sample(players,Q), key=lambda item: item.fitness)
        #     if(choice in result):
        #         pass
        #     else:
        #         result.append(choice)
        #         i+=1
            # result.append(max(random.sample(players,Q), key=lambda item: item.fitness))
            # i+=1
        for _ in range(num_players):
            choice = max(random.sample(players,Q), key=lambda item: item.fitness)
            if(choice in result):
                result.append(copy.deepcopy(choice))
            else:
                result.append(choice)
        return result
