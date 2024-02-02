from local.algorithms.search_algorithm import SearchAlgorithm
from local.problems.problem import Problem
from local.structures.node import Node, null_node
from typing import Callable
from local.solution import Solution
import random


class HillClimbingSearch(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float]):
        self.heuristic = heuristic

    def search(self, problem: Problem) -> Solution:
        current = Node(problem.initial)
        
        while True:
            neighbors = current.expand(problem)
            if not neighbors:
                break
            neighbor = max(neighbors, key=lambda node: self.heuristic(node))
            if self.heuristic(neighbor) <= self.heuristic(current):
                break
            
            current = neighbor
       
        solution = Solution(problem=problem, heuristic=self.heuristic, node=current)
        return solution


class HillClimbingSearchWithSidewaysMoves(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float], sideways_moves: int = 200):
        self.heuristic = heuristic
        self.sideways_moves = sideways_moves

    def search(self, problem: Problem) -> Node:
        current = Node(problem.initial_state())
        while True:
            neighbors = current.expand(problem)
            neighbor = max(neighbors, key=lambda node: self.heuristic(node))
            if (
                self.heuristic(neighbor) < self.heuristic(current)
                or self.sideways_moves == 0
                and self.heuristic(neighbor) == self.heuristic(current)
            ):
                break

            if self.heuristic(neighbor) == self.heuristic(current):
                neighbor = random.choice(
                    [
                        n
                        for n in neighbors
                        if self.heuristic(n) == self.heuristic(current)
                    ]
                )
                self.sideways_moves -= 1

            else:
                self.sideways_moves = 100
            current = neighbor

        solution = Solution(problem, self.heuristic, current)
        return solution

class HillClimbingSearchWithRandomRestarts(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float], restarts: int = 18):
        self.heuristic = heuristic
        self.restarts = restarts
        super().__init__()

    def search(self, problem: Problem) -> Node:
        state_factory = problem.factory()
        solution = Solution(self, problem, self.heuristic)
        while self.restarts >= 0:
            problem.initial = state_factory.create_state()
            solution.update(HillClimbingSearch(self.heuristic).search(problem))
            if problem.goal_test(solution.final_node):
                return solution
            self.restarts -= 1
        return solution
