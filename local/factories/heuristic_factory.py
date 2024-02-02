class HeuristicFactory:
  
    from local.heuristics.n_queens_heuristics import count_conflicted_queens, inverse_count_conflicted_queens	
    from local.algorithms.genetics.heuristic_n_queens_genetic import fitness_func_n_queens
    from local.algorithms.genetics.heuristic_knap_sack import fitness_func_knap_sack

    heuristics_n_queens_local = {
        "CountConflictedQueens": count_conflicted_queens,
        "InverseCountConflictedQueens": inverse_count_conflicted_queens,
    
    }

    heuristics_genetic = {
        "CountConflictedQueens": fitness_func_n_queens,
        "SumWeighted": fitness_func_knap_sack,    
    }
   

    @classmethod
    def create(cls,problem_name:str,algorithm_name:str, heuristic:str ) -> callable:
        from local.constants import LOCAL_ALGORITHMS, GENETIC_ALGORITHMS
        if algorithm_name in LOCAL_ALGORITHMS:
            return cls.heuristics_n_queens_local[heuristic]
        elif algorithm_name in GENETIC_ALGORITHMS:
            return cls.heuristics_genetic[heuristic]
        else:
            raise ValueError("Non valid heuristic.")

    @classmethod
    def heuristic_names(cls) -> list[str]:
        return ["CountConflictedQueens"]