from sys import maxsize
from itertools import permutations

V = 4

def tsp(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_cost = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_cost = 0
        k = s
        path = [s]
        for j in i:
            current_cost += graph[k][j]
            k = j
            path.append(j)
        current_cost += graph[k][s]
        path.append(s)
        min_cost = min(min_cost, current_cost)
        print("Path:", path)
        print("Cost:", current_cost)
    return min_cost

graph = [
    [0, 2451, 713, 1018],
    [2451, 0, 1745, 1524],
    [713, 1745, 0, 355],
    [1018, 1524, 355, 0]
]

s = 0
print("Minimum cost:", tsp(graph, s))

