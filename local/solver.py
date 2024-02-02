import time
from local.factories.algorithm_factory import AlgorithmFactory
from local.factories.heuristic_factory import HeuristicFactory
from local.factories.problem_factory import ProblemFactory

class Solver:
    def __init__(self,problem_params :dict, algorithm_params:dict,heuristic :str):
        self.problem = ProblemFactory.create(problem_params)
        self.heuristic = HeuristicFactory.create(problem_params['problem_name'], algorithm_params['algorithm_name'],heuristic)
        self.algorithm = AlgorithmFactory.create(problem_params, algorithm_params,self.heuristic)
        self.problem_params = problem_params

    def solve(self):
        t = time.time()
        solution = self.algorithm.search(self.problem)
        h = time.time()
        solution.run_time = h-t
        solution.problem_params = self.problem_params
        solution.algorithm = self.algorithm.__class__.__name__
        return solution
    