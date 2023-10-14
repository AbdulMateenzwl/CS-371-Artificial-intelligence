import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 5)],
    'D': [('E', 3)],
    'E': []
}

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [])]  
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return cost, path + [node]

        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                new_path = path + [node]
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, new_path))

    return float('inf'), []

start_node = 'A'
goal_node = 'E'
cost, path = uniform_cost_search(graph, start_node, goal_node)

if cost != float('inf'):
    print(f"Minimum cost from {start_node} to {goal_node}: {cost}")
    print("Path:", " -> ".join(path))
else:
    print(f"No path found from {start_node} to {goal_node}")
