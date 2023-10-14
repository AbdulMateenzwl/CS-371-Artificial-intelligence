import heapq

class Node:
    def __init__(self, name, neighbors, heuristic):
        self.name = name
        self.neighbors = neighbors
        self.heuristic = heuristic

    def __lt__(self, other):
        return False

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, neighbors, heuristic):
        self.nodes[name] = Node(name, neighbors, heuristic)

def astar_search(graph, start, goal):
    priority_queue = [(graph.nodes[start].heuristic, 0, start, [], 0)]
    visited = set()

    while priority_queue:
        _, g_cost, node, path, total_distance = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path + [node], total_distance

        for neighbor, edge_cost in graph.nodes[node].neighbors.items():
            if neighbor not in visited:
                new_path = path + [node]
                g_cost_to_neighbor = g_cost + edge_cost
                f_cost = g_cost_to_neighbor + graph.nodes[neighbor].heuristic
                total_distance_to_neighbor = total_distance + edge_cost
                heapq.heappush(priority_queue, (f_cost, g_cost_to_neighbor, neighbor, new_path, total_distance_to_neighbor))

    return [], float('inf')

# Create the graph
my_graph = Graph()
my_graph.add_node("A", {"F": 3, "B": 6}, 10)
my_graph.add_node("F", {"G": 1, "H": 7}, 6)
my_graph.add_node("G", {"I": 3}, 5)
my_graph.add_node("H", {"I": 2}, 3)
my_graph.add_node("I", {"J": 3,"E":5}, 1)
my_graph.add_node("J", {"E":5}, 0)
my_graph.add_node("E", {"D":8,"C":5}, 3)
my_graph.add_node("C", {"B":3,"D":1}, 7)
my_graph.add_node("B", {}, 8)

# Test the A* search
start_node = 'A'
goal_node = 'J'
path, total_distance = astar_search(my_graph, start_node, goal_node)

if path:
    print("Path from", start_node, "to", goal_node + ":", " -> ".join(path))
    print("Total Distance:", total_distance)
else:
    print("No path found from", start_node, "to", goal_node)
