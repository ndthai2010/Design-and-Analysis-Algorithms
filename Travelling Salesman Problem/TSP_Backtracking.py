def minCostWay(graph):
    n = len(graph)
    min_cost = float('inf')
    way = []

    def try_way(i, current_cost, visited):
        nonlocal min_cost, way
        if i > n:
            if graph[visited[-1]][visited[0]] > 0:
                total_cost = current_cost + graph[visited[-1]][visited[0]]
                if total_cost < min_cost:
                    way = visited + [visited[0]]
                    min_cost = total_cost
        else:
            for v in range(n):
                if graph[visited[-1]][v] > 0 and v not in visited:
                    new_cost = current_cost + graph[visited[-1]][v]
                    if new_cost < min_cost:
                        visited.append(v)
                        try_way(i+1, new_cost, visited)
                        visited.pop()

    for start in range(n):
        try_way(2, graph[start][0], [start])

    way = [x + 1 for x in way]
    return way, min_cost


graph = [[0,  3,  0,  0,  0,  0,  0,  3,],
         [3,  0,  5,  0,  0,  0,  6,  3,],
         [0,  5,  0,  7, 40,  1,  3,  0,],
         [0,  0,  7,  0,  5,  1,  4,  0,],
         [0,  0, 40,  5,  0,  9,  1,  0,],
         [0,  0,  1,  1,  9,  0,  2,  0,],
         [0,  6,  3,  4,  1,  2,  0,  8,],
         [3,  3,  0,  0,  0,  0,  8,  0,]]

way, min_cost = minCostWay(graph)
print("Đường đi:", way)
print("Chi phí nhỏ nhất:", min_cost)
