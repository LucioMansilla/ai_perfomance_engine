import pytest

from generators.n_queens_generator import NQueensGenerator
from tests.cheat import utils

file_path = "tests/files/"

def test_n_queens_creation():
    generator = NQueensGenerator(8)
    state = generator.create_config()

    assert utils.is_valid_nqueens(state)

n_queens_file_configs = [
    (NQueensGenerator.create_from_csv(file_path + "n_queens_creation.csv")[0],([3, 5, 1, 1, 3, 1]),),
    (NQueensGenerator.create_from_csv(file_path + "n_queens_creation.csv")[1],([4, 1, 3, 2, 4, 1]),)
]
@pytest.mark.parametrize("file_state, expected_state", n_queens_file_configs)
def test_n_queens_right_creation_from_csv(file_state, expected_state):
    assert file_state == expected_state