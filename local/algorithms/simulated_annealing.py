import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from local.structures.node import Node
from typing import Callable
from local.problems.problem import Problem
from local.algorithms.search_algorithm import SearchAlgorithm
import math

class SimulatedAnnealing(SearchAlgorithm):
    def __init__(
        self,
        heuristic: Callable[[Node], float],
        k: int = 20,
        lam: float = 0.005,
        limit: int = 80000,
    ):
        self.heuristic = heuristic
        self.k = k
        self.lam = lam
        self.limit = limit
        self.valuations = []

    def search(self, problem: Problem) -> Node:
        current = Node(problem.initial)
        for t in range(sys.maxsize):
            print(t)
            T = self.schedule(t)
            if T <= 1e-05:
                exit(1)
                return current
            neighbors = current.expand(problem)
            if not neighbors:
                return current
            
            next_choice = random.choice(neighbors)
            delta_e = self.heuristic(current) - self.heuristic(next_choice)
            if delta_e > 0 or self.probability(np.exp(delta_e / T)):
                current = next_choice

        print(current.state.data)
        print(self.heuristic(current))
        # plt.x its 0,100,200,300..
        """
        plt.xlabel('Iterations')
        plt.ylabel('Valuation')
        plt.plot(valuations)
        plt.show()
        """
        return current

    def probability(self, p: float) -> bool:
        return p > random.uniform(0.0, 1.0)

    def exp_schedule(
        self, k: int = 100, lam: float = 0.07, limit: int = 500
    ) -> Callable[[int], float]:
        return lambda t: (k * np.exp(-lam * t) if t < limit else 0)

    def schedule(self, t: int) -> float:
        return self.exp_schedule(self.k, self.lam, self.limit)(t)
