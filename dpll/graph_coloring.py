from dpll.aima.logic import *
from dpll.aima.utils import *


def generate_correct_formula(graph, k):
    formula = []

    # Each vertex has at least one color
    for vertex in graph:
        vertex_with_color = [f"X{vertex}{color}" for color in range(1, k+1)]
        formula.append("(" + " | ".join(vertex_with_color) + ")")

    # Each vertex has no more than one color
    for vertex in graph:
        vertices = []
        for color in range(1, k+1):
            vertex_with_exactly_one_color = [f"X{vertex}{color}"]
            for not_color in range (1, k+1):
                if color != not_color:
                    vertex_with_exactly_one_color.append(f"~X{vertex}{not_color}")
            vertices.append("(" + " & ".join(vertex_with_exactly_one_color) + ")")
        formula.append("(" + " | ".join(vertices) + ")")

    # Adjacent vertices are not colored with the same color.
    for vertex1 in graph:
        for vertex2 in graph[vertex1]:
            for color in range(1, k+1):
                formula.append(f"(~X{vertex1}{color} | ~X{vertex2}{color})")

    return " & ".join(formula)


def generate_formula(graph, k):
    formula = []
    #Now that you have a graph, generate all the possible colorings
    # Representation: Xij means vertex i has color j
    for vertex in graph:
        vertex_with_color = [f"X{vertex}{color}" for color in range(1, k+1)]
        formula.append("(" + " | ".join(vertex_with_color) + ")")

    # Adjacency constraints
    # Representation: Xi_j OR Xm_j, for each pair of adjacent vertices i and m and for each color j
    for vertex1 in graph:
        for vertex2 in graph[vertex1]:
            for color in range(1, k+1):
                formula.append(f"(~X{vertex1}{color} | ~X{vertex2}{color})")

    return " & ".join(formula)

def read_graph(file_name):
    graph = {}

    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        
        if '->' in line:
            from_node, to_node = line.split('->')
            #from_node = int(string_from_node.strip())
            #to_node = int(string_to_node.strip())
            
            if from_node not in graph:
                graph[from_node] = []
            
            if to_node not in graph:
                graph[to_node] = []
            
            graph[from_node].append(to_node)

    return graph

def write_colored_graph_to_dot(graph, res, filename):
    with open(filename, 'w') as file:
        file.write("digraph G {\n")
        
        # Primero, escribe todos los vértices con sus colores
        for vertex in graph:
            color = ""
            for k in res:
                if res[k] == True and str(vertex) in k:
                    # En este caso, se asume que "k" es de la forma "Xi" donde "i" es el color
                    color = k.replace(f"X{vertex}", "")
                    break
            file.write(f"{vertex} [color={color}]\n")
        
        # Luego, escribe todas las aristas
        for vertex1 in graph:
            for vertex2 in graph[vertex1]:
                file.write(f"{vertex1} -> {vertex2}\n")
        
        file.write("}\n")

def convert_number_to_color(number):
    colors = ["red", "blue", "green", "yellow", "purple", "brown", "orange", "pink"]
    return colors[int(number) - 1]
def write_colored_graph_to_dot(graph, assignments, filename):
    with open(filename, 'w') as file:
        file.write("digraph G {\n")
        
        # Convert assignments list to a dictionary
        assignments_dict = {}
        for assignment in assignments:
            node = assignment[1:-1]  # Get the node number (strip 'X' and color)
            color_number = assignment[-1:]  # Get the last character as color number
            color = convert_number_to_color(color_number)
            assignments_dict[node] = color
        
        # Write all the vertices with their colors
        for vertex in graph:
            color = assignments_dict.get(str(vertex), "")  # Use empty color if not found
            file.write(f"{vertex} [color={color}]\n")
        
        # Write all the edges
        for vertex1 in graph:
            for vertex2 in graph[vertex1]:
                file.write(f"{vertex1} -> {vertex2}\n")
        
        file.write("}\n")

if __name__ == "__main__":
    graph = read_graph("dpll/romania_map.dot")
    print("Nodos:", list(graph.keys()))
    print("Aristas:", [(from_node, to_node) for from_node in graph for to_node in graph[from_node]])
    formula = generate_correct_formula(graph, 3)
    print(formula)
    res = dpll_satisfiable(expr(formula))
    lista = []
    if not res:
        print("No pude colorearlo")
    else:
        for key in res:
            if res[key] == True:
                print(key)
                lista.append(key.__str__())
                print("Stringeado")

    print(lista)

    
    write_colored_graph_to_dot(graph, lista, "dpll/colored_graph.dot") 
