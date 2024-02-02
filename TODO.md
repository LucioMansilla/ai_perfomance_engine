- Urgent
  - [x] Brenda nos explique la libreria.
  - [x] Armar nueva estructura.
  - [x] Repo nuevo.
  - [x] Definir Playground.
  - [x] Armar el requirements.txt
  - [x] Implementar generador de estados para el nqueens.
        1. El generador debe poder ser llamado desde problem.factory() <- retorna el generador instanciado con el N correspondiente.
        2. El generador a su vez debe tener un método .create() <- retorna un nuevo estado.
  - [ ] Armar un archivo y levantar desde el archivo. //discutir el formato
  - [ ] Mover tests viejos.
      - [x] test_nqueens.py
      - [x] test_knapsack.py
      - [ ] test_hill_climbing.py
      - [ ] test_simulated_annealing.py
      - [x] test_nqueens_generator.py
      - [ ] test_knapsack_generator.py

      - [x] utils_tests.py //cheat.py
  - [ ] armar en el playground tp_test().
      - [X] mejor valuación de un nodo <-
      - [ ] to_csv del solution. 
      - [X] Alloy.
          - [X] Ver si se puede hacer en visualstudio code.
          - [X] Repasar teoría.
      - [X] incorporar los algoritmos genéticos.
      - [X] incorporar knapsack.
        - [ ] MODULARIZARLO
      - [x] Resolver knapsack con genéticos.


  - [x] NQueensGenerator:
      - [x] init(N: int)
      - [x] new_state() -> NQueensState
      - [x] new_config() -> List[int]
      - [x] from_file(path, amount) -> List[NQueensState]
  - [ ] Encontrar mejores k, lam y limit para el simulated annealing.

- [x] Nuevo Repo/
  - [ ] [local]()/
    - [x] algorithms folder falta definir local_node
      - [x] hill_climbing.py
      - [x] simulated_annealing.py
      - [x] search_algorithm.py
      - [x] Ver si las heuristicas van a recibir state o node.

    - [x] heuristics folder
       - [x] nqueensheuristic.py
       - [x] knapsackheuristic.py
 
    - [x] problems folder
      - [x] problem.py.
      - [x] nqueens.py.
      - [x] knapsack.py.
      - [x] definir factory (NQueensStateFactory).


    - [x] structures folder
      - [x] implementar local node. leer el TP que dato se solicita y hacer que el nodo lo lleve , o el problema o el algoritmo.
    - [ ] execute.py 
    - [ ] parser.py

    - [x] solution.py
      - [ ] to_csv method
      - [x] Leer TP para ver que datos se solicitan e implementarlos.

    - [x] solver.py
    - [x] Definir solver.. 
    - [x] playground

    - [x] constants.py

    - [TESTS]()/:
      - [x] tests folder
      - [x] test sucesores en nqueens:
      - [x] test nqueensgen
    
  - [X] [DPLL]()/
        -[ ] Implementar correctamente NQueens (El algoritmo actual no escala lo suficiente).
        -[x] Corregir Coloreo de grafo (Detallito que marco el profe)

  - [x] [Alloy]()/

  - [ ] minisat
  - [x] grafos con colorcitos
  - [ ] armar un folder de experimentos/lab donde se muestren los diferentes valores  ( playground).
  - [ ] hillclimbing con restarts aleatorios no va.
  
