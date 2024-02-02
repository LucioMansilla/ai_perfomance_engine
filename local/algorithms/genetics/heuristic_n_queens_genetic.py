
def fitness_func_n_queens(ga_instance, solution, solution_idx):
    aptitud = count_conflicted_queens(solution)   
    #print("aptitud: ", aptitud)
    if aptitud == 0:
        return float('inf')
    return -aptitud

def count_conflicted_queens(state) -> int:
    num_conflicts = 0

    for r1, c1 in enumerate(state):
        for r2, c2 in enumerate(state):
            if (r1, c1) != (r2, c2):
                num_conflicts += check_conflict(r1, c1, r2, c2)

    return num_conflicts


def check_conflict(row1: int, col1: int, row2: int, col2: int) -> bool:
    return (
        row1 == row2
        or col1 == col2
        or row1 - col1 == row2 - col2 
        or row1 + col1 == row2 + col2  
    ) 