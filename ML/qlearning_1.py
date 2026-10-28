import numpy as np

num_states = 5       # Rows
num_actions = 3      # Columns

alpha = 0.1          # Learning rates
gamma = 0.9          # Discount factor

Q_table_init = np.random.rand(num_states, num_actions)

reward_matrix = np.array([
    [-1, 0, -3],
    [2, -1, 5],
    [0, 1, -2],
    [3, 2, 1],
    [-2, -3, 4]
])

def q_learning(Q, state, action, reward, next_state):
    best_next_action = np.argmax(Q[next_state])
    
    Q[state, action] += alpha * (
        reward
        + gamma * Q[next_state, best_next_action]
        - Q[state, action]
    )
    
    return Q


current_state = 1
chosen_action = 2

reward = reward_matrix[current_state][chosen_action]
next_state = 2

Q_table_updated = q_learning(Q_table_init, current_state, chosen_action, reward, next_state)

print("Updated Q-table")
print(Q_table_updated)

print("Learning policy:")
print(np.argmax(Q_table_updated, axis=1))