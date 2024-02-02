from local.algorithms.hill_climbing import HillClimbingSearch, HillClimbingSearchWithSidewaysMoves, HillClimbingSearchWithRandomRestarts
from local.algorithms.simulated_annealing import SimulatedAnnealing
from local.algorithms.genetics.genetic_algorithm import NQueensGeneticSearch, KnapSackGeneticSearch

NQUEENS = "NQueens"
KNAPSACK = "Knapsack"

LOCAL_ALGORITHMS = {
    
    "HillClimbingSearch":HillClimbingSearch,
    "HillClimbingSearchWithSidewaysMoves": HillClimbingSearchWithSidewaysMoves,
    "HillClimbingSearchWithRandomRestarts": HillClimbingSearchWithRandomRestarts,
    "SimulatedAnnealingSearch": SimulatedAnnealing
}

HILL_CLIMBING = "HillClimbingSearch"
HILL_CLIMBING_SIDEWAYS = "HillClimbingSearchWithSidewaysMoves"
HILL_CLIMBING_RANDOM_RESTART = "HillClimbingSearchWithRandomRestarts"
SIMULATED_ANNEALING = "SimulatedAnnealingSearch"




GENETIC_ALGORITHMS = {
    "NQueensGeneticSearch" : NQueensGeneticSearch,
    "KnapSackGeneticSearch" : KnapSackGeneticSearch
}


## -- PARAMS -- ##

QUEENS_PARAMS = {
    'problem_name': 'NQueens',
    'initial': [1, 0, 0, 0, 0, 0, 0, 0]
}

KNAPSACK_PARAMS = {
    'problem_name': 'Knapsack',
    'initial': [0, 0, 0, 0], 
    'weights': [2,5,10,5],  
    'capacity': 16,  
    'values': [20,30,50,10]  
}

HILL_CLIMBING_PARAMS = {
    'algorithm_name': 'HillClimbingSearch',
}

HILL_CLIMBING_SIDEWAYS_PARAMS = {
    'algorithm_name': 'HillClimbingSearchWithSidewaysMoves',
    'sideways_moves': 200
}

HILL_CLIMBING_RANDOM_RESTART_PARAMS = {
    'algorithm_name': 'HillClimbingSearchWithRandomRestarts',
    'restarts': 15
}

SIMULATED_ANNEALING_PARAMS = {
    'algorithm_name': 'SimulatedAnnealingSearch',
    'temperature': 20,  
    'cooling_rate': 0.001,  
}

import numpy as np
GENETIC_ALGORITHM_PARAMS_NQUEENS = {
    'algorithm_name': 'NQueensGeneticSearch',
    'num_generations': 100,
    'pop_size': 300,
    'num_parents_mating': 2,
    'gene_type': np.int32,
    'parent_selection_type': "rank",
    'sol_per_pop': 300,
    'crossover_probability': 0.9,
    'crossover_type': "single_point",
    'mutation_type': "random",
    'keep_elitism': 1,
    'gene_space': 8
}

GENETIC_ALGORITHM_PARAMS_KNAPSACK = {
    'algorithm_name': 'KnapSackGeneticSearch',
    'num_generations': 100,
    'pop_size': 300,
    'num_parents_mating': 2,
    'gene_type': np.int32,
    'parent_selection_type': "rank",
    'sol_per_pop': 300,
    'crossover_probability': 0.9,
    'crossover_type': "single_point",
    'mutation_type': "random",
    'keep_elitism': 1,
    'gene_space': 2
}






