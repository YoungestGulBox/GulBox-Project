import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

X = tf.compat.v1.placeholder(tf.float32, shape = [None])
Y = tf.compat.v1.placeholder(tf.float32, shape = [None])

w = tf.Variable(tf.random_normal([1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis = X*w +b

cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.compat.v1.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, w_val, b_val, _ = \
    sess.run([cost, w, b, train], feed_dict={X: [1, 2, 3, 4, 5], Y: [2.1, 3.1, 4.1, 5.1, 6.1]})
    if step % 20 == 0:
        print("Step =  " + str(step), \
             "Cost =  " + str(cost_val),\
             "Weight =  " + str(w_val),\
             "Bias =  " + str(b_val))

print(sess.run(hypothesis, feed_dict={X: [5]}))