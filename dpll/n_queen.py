from aima.logic import *
from aima.utils import *

def generate_formula(n):
    clauses = []

    # One queen in each row
    for i in range(1, n+1):
        row_clauses = [f"Q{i}{j}" for j in range(1, n+1)]
        print(row_clauses)
        clauses.append("(" + " | ".join(row_clauses) + ")")
        for j in range(1, n+1):
            for k in range(j+1, n+1):
                clauses.append(f"~(Q{i}{j} & Q{i}{k})")

    # One queen in each column
    for j in range(1, n+1):
        for i in range(1, n+1):
            for k in range(i+1, n+1):
                clauses.append(f"~(Q{i}{j} & Q{k}{j})")

    # Diagonal constraints
    for i in range(1, n+1):
        for j in range(1, n+1):
            # Up-right diagonal
            for k in range(1, min(i, n-j+1)):
                clauses.append(f"~(Q{i}{j} & Q{i-k}{j+k})")
            # Down-right diagonal
            for k in range(1, min(n-i+1, n-j+1)):
                clauses.append(f"~(Q{i}{j} & Q{i+k}{j+k})")
            # Up-left diagonal
            for k in range(1, min(i, j)):
                clauses.append(f"~(Q{i}{j} & Q{i-k}{j-k})")
            # Down-left diagonal
            for k in range(1, min(n-i+1, j)):
                clauses.append(f"~(Q{i}{j} & Q{i+k}{j-k})")

    return " & ".join(clauses)


