import sys

def dfs(path, distance, shortest_distance): # Dùng nhánh cận
    global shortest_path
    if len(path) == len(cities) and distance + distances[path[-1]][path[0]] < shortest_distance:
        shortest_path = path[:]
        shortest_distance = distance + distances[path[-1]][path[0]]
    else:
        for city in cities:
            if city not in path:
                new_distance = distance + distances[path[-1]][city]
                if new_distance < shortest_distance:
                    path.append(city)
                    shortest_distance = dfs(path, new_distance, shortest_distance)
                    path.pop()
    return shortest_distance

cities = ["A", "B", "C", "D", "E"]
distances = {
    "A": {"B": 2, "C": 4, "D": 3, "E": 7},
    "B": {"A": 2, "C": 5, "D": 2, "E": 6},
    "C": {"A": 4, "B": 5, "D": 1, "E": 3},
    "D": {"A": 3, "B": 2, "C": 1, "E": 3},
    "E": {"A": 7, "B": 6, "C": 3, "D": 3}
}

# Khởi tạo biến shortest_path và shortest_distance
shortest_path = []
shortest_distance = sys.maxsize

# Tìm kiếm đường đi ngắn nhất
for city in cities:
    shortest_distance = dfs([city], 0, shortest_distance)

# Tìm vị trí của điểm xuất phát trong chuỗi shortest_path
start_index = shortest_path.index(cities[0])

# Lấy đường đi ngắn nhất bắt đầu từ điểm xuất phát và quay trở về điểm xuất phát
shortest_path = shortest_path[start_index:] + shortest_path[:start_index] + [cities[0]]

# In ra đường đi và giá trị khoảng cách ngắn nhất
print("Đường đi ngắn nhất:", shortest_path)
print("Chi phí nhỏ nhất:", shortest_distance)
