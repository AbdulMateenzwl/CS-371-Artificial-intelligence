class Node:
    def __init__(self, value):
        self.value=value
        self.next = None


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices=num_vertices
        self.adj_list=[None]*num_vertices

    def add_edge(self, src, dest):
        new_node=Node(src)
        new_node.next=self.adj_list[dest]
        self.adj_list[dest]=new_node
        
        new_node=Node(dest)
        new_node.next=self.adj_list[src]
        self.adj_list[src]=new_node

    def print_graph(self):
        for i in range(num_vertices):
            print(f"Vertix {i} : ", end = " ")
            temp=self.adj_list[i]
            while temp:
                print(f"-> {temp.value}", end = " ")
                temp=temp.next
            print("\n")
    def get_connected_nodes(self,node):
        connected_nodes=[]
        temp = self.adj_list[node]
        while temp:
            connected_nodes.append(temp.value)
            temp=temp.next
        return connected_nodes
    def are_connected(self,node1,node2):
        temp = self.adj_list[node1]
        while temp:
            if node2==temp.value:
                return True
            temp=temp.next
        return False
    def is_valid_path(self,path):
        for i in range(len(path)-1):
            if not self.are_connected(path[i],path[i+1]):
                return False
        return True
    def get_edge(self,node1,node2):
        if self.are_connected(node1,node2):
                return [node1,node2] 
        return []
def breadth_first_search(graph, start, goal):
    visited = set()
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph.get_connected_nodes(node)
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            visited.add(node)
    return "No path exists"



num_vertices = 5  
graph = Graph(num_vertices)

if __name__ == "__main__":

    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(2, 4)

    print(breadth_first_search(graph,0,3))
