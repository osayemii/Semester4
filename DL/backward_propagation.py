# Backpropagation
import numpy as np

def backpropagation(inputs, weights, biases, targets, learning_rates):
    
    # Forward pass
    weighted_sum = np.dot(inputs, weights) + biases
    output = 1/ (1 + np.exp(-weighted_sum))
    
    # Compute error
    error = targets - output
    
    # Compute gradient
    gradient = error * output * (1 - output)
    
    # Update weights and biases
    weights += learning_rates * np.dot(inputs.T, gradient)
    biases += learning_rates * np.sum(gradient)
    
    weights
    biases
    
    return error


# Example inputs and targets
inputs = np.array([[0.5, 0.3, 0.2]])
weights  = np.array([[0.4], [0.7], [0.2]])
biases = 0.1
targets = np.array([0.8])

# Perform backpropagation
learning_rates = 0.1
error = backpropagation(inputs, weights, biases, targets, learning_rates)
print("Backpropagation Error:", error)