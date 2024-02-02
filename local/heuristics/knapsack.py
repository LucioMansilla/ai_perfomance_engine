def sum_weighted(state) -> int:
    items = state.data
    weights = state.weights
    accum = 0
    values = state.values
    capacity = state.capacity
    for i in range(len(items)):
        if items[i] == 1:
            accum += values[i]
            capacity -= weights[i]
        if capacity < 0:
            return -1
    return accum
