import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.neighbors = {}

    def add_neighbor(self, neighbor, edge_cost):
        self.neighbors[neighbor] = edge_cost

    def get_neighbors(self):
        return self.neighbors

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, heuristic):
        self.nodes[name] = Node(name, heuristic)

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

if __name__ == '__main__':

    # Create the graph
    my_graph = Graph()
    my_graph.add_node("A", 10)
    my_graph.add_node("F", 6)
    my_graph.add_node("G", 5)
    my_graph.add_node("H", 3)
    my_graph.add_node("I", 1)
    my_graph.add_node("J", 0)
    my_graph.add_node("E", 3)
    my_graph.add_node("C", 7)
    my_graph.add_node("B", 8)

    # Add neighbors
    my_graph.nodes["A"].add_neighbor("F", 3)
    my_graph.nodes["A"].add_neighbor("B", 6)
    my_graph.nodes["F"].add_neighbor("G", 1)
    my_graph.nodes["F"].add_neighbor("H", 7)
    my_graph.nodes["G"].add_neighbor("I", 3)
    my_graph.nodes["H"].add_neighbor("I", 2)
    my_graph.nodes["I"].add_neighbor("J", 3)
    my_graph.nodes["I"].add_neighbor("E", 5)
    my_graph.nodes["J"].add_neighbor("E", 5)
    my_graph.nodes["E"].add_neighbor("D", 8)
    my_graph.nodes["E"].add_neighbor("C", 5)
    my_graph.nodes["C"].add_neighbor("B", 3)
    my_graph.nodes["C"].add_neighbor("D", 1)

# Test the A* search
    start_node = 'A'
    goal_node = 'J'
    path, total_distance = astar_search(my_graph, start_node, goal_node)

    if path:
        print("Path from", start_node, "to", goal_node + ":", " -> ".join(path))
        print("Total Distance:", total_distance)
    else:
        print("No path found from", start_node, "to", goal_node)
