class Utils():
    def __init__(self):
        pass

    def is_valid_nqueens(self, state:list[int]):
        length = len(state)
        for i in range(length):
            if not (0 <= state[i] and state[i] < length):
                return False  
        return True


utils = Utils()