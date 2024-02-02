from local.problems.problem import Problem, Action, State


class NQueensState(State):
    def __init__(self, board: list[int]):
        super().__init__(board)
        self.N = len(board)
        if not self.is_valid():
            print(self.data)
            raise ValueError("Invalid board")

    def is_goal(self) -> bool:
        for col in range(self.N):
            if self.data[col] == -1 or self.conflicted(self.data[col], col):
                return False
        return True

    def is_valid(self) -> bool:
        for col in self.data:
            if col < 0 or col > self.N - 1:
                return False
        return True

    def conflicted(self, row1: int, col1: int) -> bool:
        for col2 in range(col1 + 1, self.N):
            row2 = self.data[col2]
            if self.check_conflict(row1, col1, row2, col2):
                return True
        return False

    def check_conflict(self, row1: int, col1: int, row2: int, col2: int) -> bool:
        return (
            row1 == row2
            or row1 - col1 == row2 - col2  # same row
            or row1 + col1 == row2 + col2  # same \ diagonal
        )  # same / diagonal

    def __eq__(self, other) -> bool:
        return isinstance(other, NQueensState) and self.data == other.data

    def __hash__(self) -> int:
        tup = tuple(self.data)
        return hash(tup)


class NQueensAction:
    def __init__(self, col: int, row: int):
        self.col = col
        self.row = row

    def is_enabled(self, state: NQueensState) -> bool:
        return state.data[self.col] != self.row

    def execute(self, state: NQueensState) -> NQueensState:
        new_data = [
            (self.row if col == self.col else q) for col, q in enumerate(state.data)
        ]
        return NQueensState(new_data)


class NQueensProblem(Problem):
    def __init__(self, initial: NQueensState):
        super().__init__([], initial)

    def actions(self, state: NQueensState) -> list[Action]:
        actions = [
            NQueensAction(col, row)
            for col in range(self.initial.N)
            for row in range(self.initial.N)
            if state.data[col] != row
        ]
        return actions

    def factory(self):
        return True

    def __repr__(self):
        return "NQueens"

    def factory(self):
        from generators.n_queens_generator import NQueensGenerator
        return NQueensGenerator(self.initial.N)
