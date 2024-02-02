from local.constants import QUEENS_PARAMS, HILL_CLIMBING_PARAMS,HILL_CLIMBING_SIDEWAYS_PARAMS,GENETIC_ALGORITHM_PARAMS_NQUEENS
from local.solver import Solver

def genetic_n_queens():
    # Define el problema y los parámetros del algoritmo
    problem_params = QUEENS_PARAMS
    algorithm_params = GENETIC_ALGORITHM_PARAMS_NQUEENS
    heuristic = 'CountConflictedQueens'  # Reemplaza esto con el nombre de tu heurística

    # Crea una instancia de Solver
    solver = Solver(problem_params, algorithm_params, heuristic)

    # Resuelve el problema
    solution = solver.solve()

    # Imprime la solución
    print(solution)

def genetic_knap_sack():
    from local.constants import KNAPSACK_PARAMS, GENETIC_ALGORITHM_PARAMS_KNAPSACK
    heuristic = 'SumWeighted'  
    solver = Solver(KNAPSACK_PARAMS, GENETIC_ALGORITHM_PARAMS_KNAPSACK, heuristic)
    solution = solver.solve()
    print(solution)

if __name__ == "__main__":
    #genetic_knap_sack()
    genetic_n_queens()
