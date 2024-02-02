import pytest
from local.problems.n_queens import NQueensState, NQueensProblem

# -- Test NQueensState --#

is_goal_config = [
    (NQueensState([0, 3, 0, 2, 4, 5]), False),
    (NQueensState([1, 0, 3, 2, 4, 1]), False),
    (NQueensState([4, 6, 1, 5, 2, 0, 3, 7]), True),
    (NQueensState([6, 2, 0, 5, 7, 4, 1, 3]), True),
    (NQueensState([5, 3, 0, 2, 7, 4, 1, 3]), False),
    (NQueensState( [5,2,6,1,7,4,0,3]), True),
    (NQueensState([5,9,2,0,7,4,1,8,6,3]), True),
]

@pytest.mark.parametrize("current_state, expected_result", is_goal_config)
def test_is_goal(current_state, expected_result):
    assert current_state.is_goal() == expected_result

unvalid_config = [
    (([0, 0, 0, 10, 1, 2])),
    (([1, 0, -1, 0, 2, 3])),
    (([4, 6, 1, 5, 2, 0, 3, 9])),
    (([6, 2, 0, 5, 7, 4, 1, -5])),
    (([5, 3, 0, 2, -1, 4, 1, 3])),
]

@pytest.mark.parametrize("current_state", unvalid_config)
def test_is_valid(current_state):
    try:
        NQueensState(current_state)
    except:
        assert True
    assert True

get_n_quees_number_config = [
    (NQueensState([0, 0, 0, 1]), 4),
    (NQueensState([0, 1, 0, 2, 4, 1]), 6),
    (NQueensState([4, 6, 1, 5, 2, 0, 3, 7]), 8),
    (NQueensState([6, 2, 0, 5, 7, 4, 1, 3]), 8),
]

@pytest.mark.parametrize("current_state, expected_result", get_n_quees_number_config)
def test_get_n_quees_number(current_state, expected_result):
    assert current_state.N == expected_result

n_queens_config = [
    (NQueensState([0, 0, 0, 1]), 12),
    (NQueensState([0, 1, 0, 2]), 12),
    (NQueensState([3, 2, 5, 0, 0, 1]), 30),
    (NQueensState([0, 1, 0, 2, 4, 1]),30),
    (NQueensState([4, 6, 1, 5, 2, 0, 3, 7]), 56),
    (NQueensState([0, 2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13, 15]), 240)
    ]

@pytest.mark.parametrize("current_state, expected_result", n_queens_config)
def test_actions_for_n_queens(current_state, expected_result):

    n_queens_problem = NQueensProblem(current_state)
    actions_available = n_queens_problem.actions(current_state)
    successor = []

    for action in actions_available:
        if action.is_enabled(current_state):
            successor.append(action.execute(current_state))

    assert len(successor) == len(set(successor))
    assert len(successor) == expected_result 

    for successor in successor:
        assert successor.is_valid()
