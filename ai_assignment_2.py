import heapq
import random

# ------------------------------
# PART 1 : DIJKSTRA - INDIAN CITIES
# ------------------------------

graph = {
    "Delhi": {"Jaipur": 281, "Lucknow": 555},
    "Jaipur": {"Delhi": 281, "Ahmedabad": 657},
    "Ahmedabad": {"Jaipur": 657, "Mumbai": 524},
    "Mumbai": {"Ahmedabad": 524, "Pune": 150},
    "Pune": {"Mumbai": 150, "Hyderabad": 560},
    "Hyderabad": {"Pune": 560, "Bangalore": 570},
    "Bangalore": {"Hyderabad": 570, "Chennai": 346},
    "Chennai": {"Bangalore": 346},
    "Lucknow": {"Delhi": 555}
}

def dijkstra(graph, start, goal):

    pq = [(0, start)]
    visited = set()
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    parent = {}

    while pq:

        cost, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            break

        for neighbor, weight in graph[node].items():

            new_cost = cost + weight

            if new_cost < dist[neighbor]:

                dist[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(pq, (new_cost, neighbor))

    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    return path, dist[goal]


# ------------------------------
# PART 2 : UGV WITH STATIC OBSTACLES
# ------------------------------

SIZE = 20

def generate_grid(density):

    grid = [[0]*SIZE for _ in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            if random.random() < density:
                grid[i][j] = 1

    grid[0][0] = 0
    grid[SIZE-1][SIZE-1] = 0

    return grid


def neighbors(node, grid):

    x, y = node
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    result = []

    for dx, dy in moves:

        nx, ny = x+dx, y+dy

        if 0 <= nx < SIZE and 0 <= ny < SIZE and grid[nx][ny] == 0:
            result.append((nx,ny))

    return result


def dijkstra_grid(start, goal, grid):

    pq = [(0,start)]
    visited=set()
    parent={}
    dist={start:0}

    while pq:

        cost,node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            break

        for nb in neighbors(node,grid):

            new_cost = cost + 1

            if nb not in dist or new_cost < dist[nb]:

                dist[nb] = new_cost
                parent[nb] = node
                heapq.heappush(pq,(new_cost,nb))

    path=[]
    node=goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    return path


# ------------------------------
# PART 3 : DYNAMIC OBSTACLES
# ------------------------------

def add_dynamic_obstacles(grid):

    for _ in range(10):
        x = random.randint(0,SIZE-1)
        y = random.randint(0,SIZE-1)
        grid[x][y] = 1

    return grid


# ------------------------------
# MAIN PROGRAM
# ------------------------------

print("\n--- DIJKSTRA : INDIAN CITIES ---")

start = input("Enter Start City: ")
goal = input("Enter Goal City: ")

path, cost = dijkstra(graph,start,goal)

print("Shortest Path:",path)
print("Distance:",cost,"km")


print("\n--- UGV STATIC OBSTACLES ---")

density = float(input("Enter obstacle density (0.1 low / 0.2 medium / 0.3 high): "))

grid = generate_grid(density)

path = dijkstra_grid((0,0),(SIZE-1,SIZE-1),grid)

print("Path found:",path)
print("Path length:",len(path))


print("\n--- UGV DYNAMIC OBSTACLES ---")

grid = add_dynamic_obstacles(grid)

path = dijkstra_grid((0,0),(SIZE-1,SIZE-1),grid)

print("New path after dynamic obstacles:",path)
print("New path length:",len(path))
