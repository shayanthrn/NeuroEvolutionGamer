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

        # TODO
        # child: an object of class `Player`
        pass


    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            new_players = prev_players
            return new_players

    def next_population_selection(self, players, num_players,gen_num):

        # TODO (additional): plotting

        #using Q-tournoment algorithm for selection
        result = []
        Q = gen_num
        for _ in range(num_players):
            random.sample(players,Q)
            result.append(max(random.sample(players,Q), key=lambda item: item.fitness))

        return result
