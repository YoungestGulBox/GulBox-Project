import os

from tensorflow.python.ops.gen_array_ops import shape
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np

xy = np.loadtxt('data-01-test-score.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

# print(x_data.shape, x_data, len(x_data))
# print(y_data.shape, y_data)

X = tf.compat.v1.placeholder(tf.float32, shape=[None, 3])
Y = tf.compat.v1.placeholder(tf.float32, shape=[None, 1])

w = tf.Variable(tf.random_normal([3, 1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis = tf.matmul(X, w) + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.compat.v1.Session()
sess.run(tf.global_variables_initializer())

for step in range(8001):
    cost_val, hy_val, _ = \
    sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    if step % 50 == 0:
        print(step, "Cost: ", cost_val, "\nPrediction: \n", hy_val)

print("Your score will be ", sess.run(hypothesis, feed_dict={X: [[100, 70, 101]]}))
print("Other score will be ", sess.run(hypothesis, feed_dict={X: [[60, 70, 110], [90, 100, 80]]}))