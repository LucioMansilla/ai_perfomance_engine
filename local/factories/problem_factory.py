from local.constants import NQUEENS, KNAPSACK
from local.problems.n_queens import NQueensProblem, NQueensState
from local.problems.knapsack import KnapsackState, KnapSackProblem
from local.problems.problem import Problem

class ProblemFactory:
    

    @classmethod
    def create(cls, params: dict) -> tuple[Problem, callable]:
        problem_name = params['problem_name']
        
        if problem_name == NQUEENS:
            initial_state_data = params['initial']
            problem =  NQueensProblem(NQueensState(initial_state_data))    
            return problem 
        
        elif problem_name == KNAPSACK:
            state = params['initial']
            weights = params['weights']
            capacity = params['capacity']
            values = params['values']
            return KnapSackProblem(KnapsackState(state, weights, capacity, values))          
        else:
            raise Exception("Problem not found")