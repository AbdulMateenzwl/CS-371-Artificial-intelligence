class Node:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.f_score = 0

    def __lt__(self, other):
        return self.f_score < other.f_score

class Puzzle:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state
        self.size = len(initial_state)
        self.final_positions = self.get_final_positions()
        
    def get_final_positions(self):
        final_positions = {}
        for i in range(self.size):
            for j in range(self.size):
                final_positions[self.final_state[i][j]] = (i, j)
        return final_positions
    
    def calculate_distance(self, state):
        distance = 0
        for i in range(self.size):
            for j in range(self.size):
                value = state[i][j]
                if value != 0:
                    final_i, final_j = self.final_positions[value]
                    distance += abs(i - final_i) + abs(j - final_j)
        return distance
    
    def calculate_f_score(self, node):
        return node.depth + self.calculate_distance(node.state)
    
    def is_final_state(self, state):
        return state == self.final_state
    
    def get_possible_moves(self, node):
        moves = []
        empty_i, empty_j = None, None
        for i in range(self.size):
            for j in range(self.size):
                if node.state[i][j] == 0:
                    empty_i, empty_j = i, j
                    break
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dir_i, dir_j in directions:
            new_i, new_j = empty_i + dir_i, empty_j + dir_j
            if 0 <= new_i < self.size and 0 <= new_j < self.size:
                new_state = [list(row) for row in node.state]
                new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
                move = "UDLR"[directions.index((dir_i, dir_j))]
                moves.append((new_state, move))
        return moves

def a_star_search(initial_state, final_state):
    puzzle = Puzzle(initial_state, final_state)
    
    open_set = [Node(initial_state)]
    closed_set = set()
    
    while open_set:
        open_set.sort(key=lambda x: x.f_score)
        current_node = open_set.pop(0)
        
        if puzzle.is_final_state(current_node.state):
            path = []
            while current_node:
                path.append((current_node.state, current_node.move))
                current_node = current_node.parent
            return list(reversed(path))
        
        closed_set.add(tuple(tuple(row) for row in current_node.state))
        
        for new_state, move in puzzle.get_possible_moves(current_node):
            if tuple(tuple(row) for row in new_state) not in closed_set:
                new_node = Node(new_state, current_node, move, current_node.depth + 1)
                new_node.f_score = puzzle.calculate_f_score(new_node)
                open_set.append(new_node)
    
    return None

if __name__ == "__main__":
    initial_state = [[1, 2, 3],
                    [0, 4, 6], 
                    [7, 5, 8]]
    final_state = [[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 0]]
    path = a_star_search(initial_state, final_state)
    for state, move in path:
        for row in state:
            print(row)
        print("Move:", move)
        print()
