import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, cost):
        if start in self.graph:
            self.graph[start].append((end, cost))
        else:
            self.graph[start] = [(end, cost)]

    def uniform_cost_search(self, start, goal):
        priority_queue = [(0, start, [])]
        visited = set()

        while priority_queue:
            cost, node, path = heapq.heappop(priority_queue)
            if node in visited:
                continue

            visited.add(node)

            if node == goal:
                return cost, path + [node]

            for neighbor, edge_cost in self.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [node]))


        return float('inf'), []

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge('A', 'B', 2)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('A', 'D', 1)
    graph.add_edge('B', 'D', 2)
    graph.add_edge('C', 'D', 5)
    graph.add_edge('D', 'E', 3)

    start_node = 'A'
    goal_node = 'E'
    cost, path = graph.uniform_cost_search(start_node, goal_node)

    if cost != float('inf'):
        print(f"Minimum cost from {start_node} to {goal_node}: {cost}")
        print("Path:", " -> ".join(path))
    else:
        print(f"No path found from {start_node} to {goal_node}")
