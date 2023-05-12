import sys


def print_matrix(a):
    for line in a:
        print('  '.join(map(str, line)))


def traveling_salesman(i, city, pass_through, mincost, current_cost, path, num_visited, total_vertices, result=None):
    if result is None:
        result = []

    for idx in range(len(city)):
        if city[i][idx] != 0:
            if not pass_through[i][idx] and idx not in path:
                current = current_cost + city[i][idx]
                if current < mincost:
                    num_visited += 1
                    path.append(idx)
                    pass_through[i][idx] = True
                    pass_through[idx][i] = True

                    if num_visited == total_vertices:
                        if city[idx][0] != 0:
                            path.append(0)
                            mincost = current + city[idx][0]
                            result.append(path.copy())
                            path.pop()
                        else:
                            num_visited -= 1
                    else:
                        mincost = traveling_salesman(
                            idx, city, pass_through, mincost, current, path, num_visited, total_vertices, result)

                    path.pop()
                    pass_through[i][idx] = False
                    pass_through[idx][i] = False
                    num_visited -= 1
    return mincost


def salesman(city, maxcost=sys.maxsize):
    pass_through = [[False] * len(city) for _ in range(len(city))]
    result = []
    total_vertices = len(city)
    mincost = traveling_salesman(0, city, pass_through, maxcost, 0, [
                                 0], 1, total_vertices, result)
    return result, mincost


city = [[0, 3, 0, 0, 0, 0, 0, 3],
        [3, 0, 5, 0, 0, 0, 6, 3],
        [0, 5, 0, 7, 40, 1, 3, 0],
        [0, 0, 7, 0, 5, 1, 4, 0],
        [0, 0, 40, 5, 0, 9, 1, 0],
        [0, 0, 1, 1, 9, 0, 2, 0],
        [0, 6, 3, 4, 1, 2, 0, 8],
        [3, 3, 0, 0, 0, 0, 8, 0]
        ]
result, mincost = salesman(city)
print("Chi phí thấp nhất: " + str(mincost))
print("Đường đi ngắn nhất: " + str(result[-1]))
