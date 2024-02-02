class State:
    def __init__(self, data):
        self.data = data

    def is_goal(self) -> bool:
        """Method that returns a boolean depending if the state is a final state"""
        raise NotImplementedError

    def is_valid(self) -> bool:
        """Method repOK that returns a boolean depending if the state is a valid state."""
        raise NotImplementedError


class Action:
    """ " Return true if the action is enabled in the given state"""

    def __init__(self) -> None:
        self.cost = 1

    def is_enabled(self, state: State) -> bool:
        raise NotImplementedError

    """" Execute the action in the given state"""

    def execute(self, state: State) -> State:
        raise NotImplementedError


class Problem:
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, actions: list[Action], initial: State):
        """The constructor"""
        self.initial = initial
        self.problem_actions = actions

    """Return the initial state for the problem."""

    def initial_state(self) -> State:
        return self.initial

    def actions(self, state: State) -> list[Action]:
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        result = []
        for action in self.problem_actions:
            if action.is_enabled(state):
                result.append(action)
        return result

    def result(self, state: State, action: Action) -> State:
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        return action.execute(state)

    def goal_test(self, state: State) -> bool:
        """Return True if the state is a goal."""
        return state.is_goal()

    def is_valid(self, state: State) -> bool:
        """Method repOK that returns a boolean depending if the state is a valid state."""
        return state.is_valid()

    def factory(self):
        raise NotImplementedError
