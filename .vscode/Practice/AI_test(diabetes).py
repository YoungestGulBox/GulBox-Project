import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np

xy = np.loadtxt('data-03-diabetes.csv', delimiter=',', dtype=np.float32)
x_data = xy[:,:-1]
y_data = xy[:, [-1]]

X = tf.compat.v1.placeholder(tf.float32, shape=[None, 8])
Y = tf.compat.v1.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([8,1]), name='Weight')
b = tf.Variable(tf.random_normal([1]), name='Bias')

hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1-Y)*tf.log(1-hypothesis))

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

sess = tf.compat.v1.Session()
sess.run(tf.global_variables_initializer())

for step in range(8001):
    cost_val, _ = sess.run([cost, train], feed_dict = {X: x_data, Y: y_data})
    if step % 200 == 0:
        print(step, cost_val)


h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X:x_data, Y:y_data})
print("\nHypothesis:\n", h, "\nCorrect(Y):\n", c, "\nAccuracy: ", a)