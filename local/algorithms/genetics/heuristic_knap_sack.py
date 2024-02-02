def fitness_func_knap_sack(values,capacity,weights):
    def fitness_function(ga_instance, solution, solution_idx):
        return sum_weighted(solution,values,capacity,weights)
    return fitness_function

def sum_weighted(items,values,capacity,weights) -> int:
    accum = 0
   
    for i in range(len(items)):
        if items[i] == 1:
            accum += values[i]
            capacity -= weights[i]
        if capacity < 0:
            return -1
    return accum