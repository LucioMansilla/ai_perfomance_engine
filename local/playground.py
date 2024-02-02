from local.algorithms.hill_climbing import (
    HillClimbingSearch,
    HillClimbingSearchWithSidewaysMoves,
    HillClimbingSearchWithRandomRestarts,
)
from local.algorithms.simulated_annealing import SimulatedAnnealing
from local.problems.n_queens import NQueensProblem, NQueensState
from local.problems.knapsack import KnapsackState, KnapSackProblem, KnapsackState
from local.heuristics.n_queens_heuristics import (
    count_conflicted_queens,
    inverse_count_conflicted_queens,
)
from local.heuristics.knapsack import sum_weighted
from generators.n_queens_generator import NQueensGenerator
from local.structures.node import null_node



def test_1_knapsack_hill_climbing():
    state = [0, 0, 0, 0]
    weights = [2, 5, 10, 5]
    values = [20, 30, 50, 10]
    capacity = 16

    algorithm = HillClimbingSearch(sum_weighted)
    problem = KnapSackProblem((KnapsackState(state, weights, capacity, values)))
    sol = algorithm.search(problem)
    print("Maximum value of the knapsack: ", sol.state.sack_value)
    print("Total weight of the knapsack: ", sol.state.sack_weight)


def test_2_knapsack_hill_climbing():
    state = [0, 0, 0]
    weights = [4, 5, 1]
    values = [1, 2, 3]
    capacity = 4

    algorithm = HillClimbingSearch(sum_weighted)
    problem = KnapSackProblem((KnapsackState(state, weights, capacity, values)))
    sol = algorithm.search(problem)
    print("Maximum value of the knapsack: ", sol.state.sack_value)
    print("Total weight of the knapsack: ", sol.state.sack_weight)


def test_3_knapsack_hill_climbing():
    state = [0, 0, 0]
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    algorithm = HillClimbingSearch(sum_weighted)
    problem = KnapSackProblem((KnapsackState(state, weights, capacity, values)))
    sol = algorithm.search(problem)
    print("Maximum value of the knapsack: ", sol.state.sack_value)
    print("Total weight of the knapsack: ", sol.state.sack_weight)


def test_n_queens_climbing():
    n_queens_generator = NQueensGenerator(8)

    n_queens_states = n_queens_generator.create_state(100)
    count_goals = 0
    for current_state in n_queens_states:
        problem = NQueensProblem(current_state)
        algorithm = HillClimbingSearch(inverse_count_conflicted_queens)
        solution = algorithm.search(problem)
        if solution != null_node and solution.state.is_goal():
            count_goals += 1
    print("Total number of goals: ", count_goals)


def test_n_queens_restarts_climbing():
    n_queens_generator = NQueensGenerator(16)
    n_queens_states = n_queens_generator.create_state(100)
    count_goals = 0
    for current_state in n_queens_states:
        problem = NQueensProblem(current_state)
        algorithm = HillClimbingSearchWithRandomRestarts(inverse_count_conflicted_queens)
        solution = algorithm.search(problem)
        if solution != null_node and solution.state.is_goal():
            count_goals += 1
            print(count_goals)
    print("Total number of goals: ", count_goals)


def test_n_queens_hill_climbing_with_sideways_moves():
    n_queens_generator = NQueensGenerator(8)
    n_queens_states = n_queens_generator.create_state(100)
    count_goals = 0
    for current_state in n_queens_states:
        problem = NQueensProblem(current_state)
        algorithm = HillClimbingSearchWithSidewaysMoves(inverse_count_conflicted_queens)
        solution = algorithm.search(problem)
        if solution != null_node and solution.state.is_goal():
            count_goals += 1
    print("Total number of goals: ", count_goals)


def test_n_queens_simulated_annealing():
    n_queens_generator = NQueensGenerator(8)
    n_queens_states = n_queens_generator.create_state(10)
    count_goals = 0
    flag = 0
    
    for current_state in n_queens_states:
        problem = NQueensProblem(current_state)
        algorithm = SimulatedAnnealing(count_conflicted_queens,k=2,lam=0.003,limit=6000)
        solution = algorithm.search(problem)
        print("Voy por: ", flag+1)
        flag += 1
        if solution.state.is_goal():
            count_goals += 1
    print("Total number of goals: ", count_goals)

#algorithm = SimulatedAnnealing(count_conflicted_queens,k=1,lam=0.0009,limit=20000)
#k = 2, lam = 0.003



    #solutions.extend(genetic.search(best_params('NQueens')))



def test_ploteo_simulated_annealing():
    import matplotlib
    matplotlib.use('TkAgg')
    from matplotlib import pyplot as plt
    #use TKAgg backend for plt
    import time
    params = [(1, 0.001), (10, 0.5), (10, 0.1), (10, 0.005), (10, 0.001)]
    params_2 = [(5, 0.01), (20, 0.5), (20, 0.1), (20, 0.005), (20, 0.001)]
    fig, ax = plt.subplots()
    fig2, ax2 = plt.subplots()
    queen_state = NQueensGenerator(8).create_state(1)
    
    for k, lam in params:
        problem = NQueensProblem((queen_state))
        algorithm = SimulatedAnnealing(count_conflicted_queens, k=k, lam=lam)
        start_time = time.time()
        solution = algorithm.search(problem)
        if solution and solution.state.is_goal():
            print("Solution found for k=", k, " and lam=", lam)    
        end_time = time.time()
        elapsed_time = end_time - start_time
        ax.plot(
            algorithm.valuations,
            label=f"k={k}, lam={lam}, time={round(elapsed_time,4)}",
        )

    for k, lam in params_2:
        problem = NQueensProblem((queen_state))
        algorithm = SimulatedAnnealing(count_conflicted_queens, k=k, lam=lam)
        start_time = time.time()
        solution = algorithm.search(problem)
        end_time = time.time()
        if solution and solution.state.is_goal():
            print("Solution found for k=", k, " and lam=", lam)    
        elapsed_time = end_time - start_time
        ax2.plot(
            algorithm.valuations,
            label=f"k={k}, lam={lam}, time={round(elapsed_time,4)}",
        )
    
 

    ax.legend()
    ax.set_xlabel("Iteraciones")
    ax.set_ylabel("Valor de la función de evaluación")

    ax2.legend()
    ax2.set_xlabel("Iteraciones")
    ax2.set_ylabel("Valor de la función de evaluación")


    import numpy as np

    ax.set_xticks(np.arange(0, 8000, 500))
    ax.set_yticks(np.arange(0, 50, 1))
    ax2.set_xticks(np.arange(0, 8000, 500))
    ax2.set_yticks(np.arange(0, 50, 1))
    plt.show()


if __name__ == "__main__":
    test_ploteo_simulated_annealing()
