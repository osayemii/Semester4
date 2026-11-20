import tensorflow as tf

# Define the recurrent weights
Wh = tf.Variable(tf.random.normal([32, 32]))

# Define the input weights
Wx = tf.Variable(tf.random.normal([10, 32]))

# Define the bias
b = tf.Variable(tf.zeros([32]))

# Initial hidden state
h_previous = tf.zeros([1, 32])

# First input
x1 = tf.random.normal([1, 10])

# Calculate first hidden state
h1 = tf.tanh(
tf.matmul(x1, Wx) +
tf.matmul(h_previous, Wh) + b
)

# Second input
x2 = tf.random.normal([1, 10])

# Calculate second hidden state
# Notice that h1 is passed into the next time step.
h2 = tf.tanh(
tf.matmul(x2, Wx) +
tf.matmul(h1, Wh) + b
)

# Third input
x3 = tf.random.normal([1, 10])

# Calculate third hidden state
# Notice that h2 is passed into the next time step.
h3 = tf.tanh(
tf.matmul(x3, Wx) +
tf.matmul(h2, Wh) + b
)

print("First hidden state:", h1.numpy())
print("Second hidden state:", h2.numpy())
print("Third hidden state:", h3.numpy())