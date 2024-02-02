from local.problems.problem import State


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(
        self,
        state: State = None,
        parent: object = None,
    ) -> object:
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

   
         
    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        possible_actions = []
        result = []
        for action in problem.actions(self.state):
            possible_actions.append(action)
        for action in possible_actions:
            result.append(self.child_node(problem, action))

        self.generated_nodes = len(result)
        return result

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(
            next_state,
            self,
        )
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


class NullNode(Node):
    def __init__(self):
        super().__init__(None, None)

    def __eq__(self, other):
        return isinstance(other, NullNode)


null_node = NullNode()
