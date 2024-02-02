import random
import csv
from local.problems.n_queens import NQueensState


class NQueensGenerator:
    def __init__(self, N: int):
        self.N = N

    def create_state(self, amount :int =1) -> list[NQueensState] | NQueensState:
        states = []
        for i in range(amount):
            if amount == 1:
                return NQueensState(self.create_config())
            states.append(NQueensState(self.create_config()))
        return states

    def create_config(self) -> list:
        return list(random.randint(0, self.N - 1) for _ in range(self.N))

    @classmethod
    def create_from_csv(cls, file_path :str) -> list[list[int]]:
        states = []
        with open(f"{file_path}", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                state = row["Problem Name"], eval(row["Initial State"])
                states.append(state[1])
        return states
