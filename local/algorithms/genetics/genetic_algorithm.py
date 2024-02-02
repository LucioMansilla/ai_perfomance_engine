import numpy as np
from typing import Callable
from local.algorithms.search_algorithm import SearchAlgorithm
from local.problems.problem import Problem
import pygad

class GeneticSearch(SearchAlgorithm):
    def __init__(self, heuristic, algorithm_params, problem_params):
        self.fitness_func = heuristic
        self.ga_instance = pygad.GA(num_generations= algorithm_params['num_generations'],
                           num_parents_mating= algorithm_params['num_parents_mating'],
                           sol_per_pop= algorithm_params['sol_per_pop'],   
                           num_genes=len(problem_params['initial']),
                           gene_type= algorithm_params['gene_type'],
                           fitness_func= heuristic,
                           gene_space=list(range(0, algorithm_params['gene_space'])),                      
                           #mutation_probability= self.mutation_probability,
                           crossover_type= algorithm_params['crossover_type'],
                           #crossover_probability= self.crossover_probability,
                           parent_selection_type= algorithm_params['parent_selection_type'],
                           keep_elitism= algorithm_params['keep_elitism']
                           )  
        print("GeneticSearchsss", self.ga_instance.initial_population)
    
    def search(self, problem: Problem):
        raise NotImplementedError
    
        
class NQueensGeneticSearch(GeneticSearch):
    def __init__(self, heuristic, algorithm_params, problem_params):
        super().__init__(heuristic, algorithm_params, problem_params)

    def search(self, problem: Problem):
        print("GeneticSearchhhhh", self.ga_instance.num_genes)
        self.ga_instance.mutation_percent_genes= 1 * 100 / self.ga_instance.num_genes
        self.ga_instance.mutation_by_replacement=True

        # Inicio del algoritmo genético.
        self.ga_instance.run()
                           
        #Devuelve la mejor solución y el valor de fitness
        solution, solution_fitness, solution_idx = self.ga_instance.best_solution()
        print("Parameters of the best solution : {solution}".format(solution=solution))
        print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

        from local.algorithms.genetics.heuristic_n_queens_genetic import count_conflicted_queens
        print("Count conflicted queens: ", count_conflicted_queens(solution))

        exit(1)

class KnapSackGeneticSearch(GeneticSearch):
    def __init__(self, heuristic, algorithm_params, problem_params):
        super().__init__(heuristic, algorithm_params, problem_params)

    def search(self, problem: Problem):
        values = problem.initial.values
        weights = problem.initial.weights
        capacity = problem.initial.capacity

        self.ga_instance.fitness_func = self.fitness_func(values,capacity,weights)
        self.ga_instance.mutation_type= None

        # Inicio del algoritmo genético.
        self.ga_instance.run()

        #Devuelve la mejor solución y el valor de fitness
        solution, solution_fitness, solution_idx = self.ga_instance.best_solution()
        print("Parameters of the best solution : {solution}".format(solution=solution))
        print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

        exit(1)



