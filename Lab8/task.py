import numpy as np

# Define the MDP components
grid_size = 4
n_states = grid_size * grid_size
n_actions = 4  # UP, DOWN, LEFT, RIGHT
P_slip = 0.4  # Probability of slipping

# Define the grid, rewards, and transitions
grid = [['S', 'F', 'F', 'F'],
        ['F', 'H', 'F', 'H'],
        ['F', 'F', 'F', 'H'],
        ['H', 'F', 'F', 'G']]
rewards = {'S': 0, 'F': -0.1, 'H': -1, 'G': 1}

# Initialize the value function
V = np.zeros(n_states)

# Define the transition function
def transition_probability(s, a, s_prime):
    if s_prime == s:
        return 1 - P_slip + P_slip / n_actions
    else:
        return P_slip / n_actions

# Value Iteration
gamma = 0.9  # Discount factor
tolerance = 1e-6  # Convergence tolerance
while True:
    delta = 0
    for s in range(n_states):
        if s == n_states - 1:
            continue  # Skip the goal state

        v = V[s]
        V[s] = max(sum(transition_probability(s, a, s_prime) *
                      (rewards[grid[s // grid_size][s % grid_size]] + gamma * V[s_prime])
                      for a in range(n_actions)
                      for s_prime in range(n_states)), V[s])
        delta = max(delta, abs(v - V[s]))

    if delta < tolerance:
        break

# Extract the optimal policy
policy = []
for s in range(n_states):
    if s == n_states - 1:
        policy.append('G')  # Goal state
        continue

    best_action = None
    best_value = float('-inf')
    for a in range(n_actions):
        action_value = sum(transition_probability(s, a, s_prime) *
                           (rewards[grid[s // grid_size][s % grid_size]] + gamma * V[s_prime])
                           for s_prime in range(n_states))
        if action_value > best_value:
            best_value = action_value
            best_action = a
    policy.append(['UP', 'DOWN', 'LEFT', 'RIGHT'][best_action])

# Print the policy
for i in range(grid_size):
    for j in range(grid_size):
        state = i * grid_size + j
        print(policy[state], end='\t')
    print()
