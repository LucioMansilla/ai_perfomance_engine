from local.algorithms.search_algorithm import SearchAlgorithm
from local.problems.problem import Problem
from typing import Callable
import csv
from local.structures.node import Node


class Solution():
    def __init__(
        self,
        problem: Problem,
        heuristic: Callable[[Node], float],
        node: Node
    ):
        self.algorithm = None
        self.problem_name = problem
        self.params = []
        self.heuristic = heuristic
        self.best_valuation = heuristic(node)
        self.generated_nodes = node.generated_nodes
        self.visited_nodes = node.depth
        self.final_state = node.state.data
        self.final_node = node
        self.runtime = 0
        self.memory = 0


    def write_to_csv(self, file_name:str):
        headers = ["Problem Name", "Algorithm", "Params", "Heuristic", "Best Valuation", "Generated Nodes", "Visted Nodes", "Execution Time", "Memory Usage"]
        with open(f"{file_name}", "a", encoding="UTF8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                if f.tell() == 0:
                    writer.writeheader()
                writer.writerow(
                    {
                        "Problem Name": str(self.problem_name),
                        "Algorithm": str(self.algorithm),
                        "Params": str(self.params),
                        "Heuristic": str(self.heuristic),
                        "Best Valuation": str(self.best_valuation),
                        "Generated Nodes": str(self.generated_nodes),
                        "visited Nodes": str(self.visited_nodes),
                        "Execution Time": str(self.runtime),
                        "Memory Usage": str(self.memory),
                    }
                )

    def update(self, solution):
        self.best_valuation = max(self.best_valuation, solution.best_valuation)
        self.generated_nodes += solution.generated_nodes
        self.visited_nodes += solution.visited_nodes
        self.final_state = solution.final_state
        self.final_node = solution.final_node

    def __hash__(self):
        return hash(self.final_state)

    def __repr__(self):
        return f"""\n
        -------------------------------------------------------------------------------------------------
        Algorithm: {self.algorithm} 
        Problem: {self.problem_name} 
        Params: {self.params}
        Heuristic: {self.heuristic}
        ------------------------------------
        Better Valuation: {self.best_valuation}
        Generated Nodes: {self.generated_nodes}
        Execution Time: {self.runtime}     
        Memory Usage: {self.memory}
        -------------------------------------------------------------------------------------------------
        Initial State: {self.problem_name.initial_state}
        Final State: {self.final_state}
        """

