from local.constants import LOCAL_ALGORITHMS, GENETIC_ALGORITHMS, HILL_CLIMBING, HILL_CLIMBING_SIDEWAYS, HILL_CLIMBING_RANDOM_RESTART, SIMULATED_ANNEALING
from local.algorithms.search_algorithm import SearchAlgorithm


class AlgorithmFactory:

    @classmethod
    def create(cls, problem_params, algorithm_params: dict, h: callable) -> SearchAlgorithm:
        algorithm = algorithm_params['algorithm_name']
        
        if algorithm == HILL_CLIMBING:
            return LOCAL_ALGORITHMS[algorithm](h)

        elif algorithm == HILL_CLIMBING_SIDEWAYS:
            return LOCAL_ALGORITHMS[algorithm](h, algorithm_params['sideways_moves'])
        
        elif algorithm == HILL_CLIMBING_RANDOM_RESTART:
            return LOCAL_ALGORITHMS[algorithm](h, algorithm_params['restarts'])
        
        elif algorithm == SIMULATED_ANNEALING:
            return LOCAL_ALGORITHMS[algorithm](h, algorithm_params['temperature'], algorithm_params['cooling_rate'])
        
        elif algorithm in GENETIC_ALGORITHMS.keys():
            return GENETIC_ALGORITHMS[algorithm](h, algorithm_params, problem_params)
        
        else:
            raise Exception("Algorithm Not Found")
