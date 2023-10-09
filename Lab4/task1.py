class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, node_name):
        if node_name not in self.neighbors:
            self.neighbors.append(node_name)

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_name):
        if node_name not in self.nodes:
            self.nodes[node_name] = Node(node_name)

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            self.nodes[node1].add_neighbor(node2)
            self.nodes[node2].add_neighbor(node1)

    def get_connected_nodes(self, node_name):
        if node_name in self.nodes:
            return self.nodes[node_name].neighbors
        else:
            return []

    def get_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            if node2 in self.nodes[node1].neighbors:
                return (node1, node2)
            elif node1 in self.nodes[node2].neighbors:
                return (node2, node1)
        return None

    def are_connected(self, node1, node2):
        return self.get_edge(node1, node2) is not None

    def is_valid_path(self, path):
        if len(path) < 2:
            return True
        for i in range(len(path) - 1):
            if not self.are_connected(path[i], path[i+1]):
                return False
        return True

    def print_graph(self):
        for node_name in self.nodes:
            node = self.nodes[node_name]
            neighbors = ", ".join(node.neighbors)
            print(f"{node_name}: [{neighbors}]")

    def delete_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            if node2 in self.nodes[node1].neighbors:
                self.nodes[node1].neighbors.remove(node2)
            if node1 in self.nodes[node2].neighbors:
                self.nodes[node2].neighbors.remove(node1)

def breadth_first_search(graph, start, goal):
    visited = set()
    queue = []
    queue.append([start])

    while queue:
        path = queue.pop(0)  
        node = path[-1]

        if node == goal:
            return path  

        if node not in visited:
            for neighbor in graph.get_connected_nodes(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)

    return []

def depth_first_search(graph, start, goal):
    visited = set()
    stack = []
    stack.append([start])

    while stack:
        path = stack.pop()  
        node = path[-1]

        if node == goal:
            return path  

        if node not in visited:
            for neighbor in graph.get_connected_nodes(node):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
            visited.add(node)
    return []

if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_node("A")
    my_graph.add_node("B")
    my_graph.add_node("C")
    my_graph.add_node("D")
    my_graph.add_node("E")
    my_graph.add_node("F")
    my_graph.add_node("G")
    my_graph.add_node("H")

    my_graph.add_edge("A", "B")
    my_graph.add_edge("B", "C")
    my_graph.add_edge("C", "D")
    my_graph.add_edge("D", "A")
    my_graph.add_edge("A", "C")
    my_graph.add_edge("B", "D")
    my_graph.add_edge("G", "A")
    my_graph.add_edge("G", "H")
    my_graph.add_edge("D", "G")


    print("Connected Nodes to A:", my_graph.get_connected_nodes("A"))
    print("Edge between A and H:", my_graph.get_edge("A", "H"))
    print("Are A and C connected?", my_graph.are_connected("A", "C"))
    path = ["A", "B", "C", "D" , "E"]
    print(f"Is {path} a valid path?", my_graph.is_valid_path(path))
    my_graph.print_graph()
    print("--------------")

    my_graph.delete_edge("A", "B")
    my_graph.print_graph()
    print("--------------")
    print(f"Breath First Search {breadth_first_search(my_graph, 'A', 'F')}")
    print(f"Breath First Search {depth_first_search(my_graph, 'A', 'F')}")
    
