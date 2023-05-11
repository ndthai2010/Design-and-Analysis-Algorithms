import itertools

# Bài toán người bán hàng


def travelling_salesman(graph):
    # Get all possible permutations of nodes
    nodes = list(graph.keys())
    permutations = itertools.permutations(nodes)

    # Set initial values
    shortest_path = None
    shortest_distance = float('inf')

    # Try each permutation and update the shortest path and distance
    for path in permutations:
        total_distance = 0
        for i in range(len(path) - 1):
            current = path[i]
            next_node = path[i+1]
            total_distance += graph[current][next_node]
        # Add distance from last node back to starting node
        total_distance += graph[path[-1]][path[0]]

        # Update shortest path and distance if necessary
        if total_distance < shortest_distance:
            shortest_path = path
            shortest_distance = total_distance

    return shortest_path, shortest_distance


# Create a graph
graph = {
    'A': {'B': 2, 'C': 3, 'D': 5},
    'B': {'A': 2, 'C': 4, 'D': 4},
    'C': {'A': 3, 'B': 4, 'D': 1},
    'D': {'A': 5, 'B': 4, 'C': 1}
}

# Find the shortest path and distance using the travelling_salesman function
shortest_path, shortest_distance = travelling_salesman(graph)

# Print the results
print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)
