import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)
import prettytensor as pt 
import numpy as np

def distribution_model(num_features, out_features=45):
	import tensorflow as tf
	def weight_variable(shape):
		initial = tf.truncated_normal(shape, stddev=0.1)
		return tf.Variable(initial)

	def bias_variable(shape):
		initial = tf.constant(0.1, shape=shape)
		return tf.Variable(initial)

	x = tf.placeholder(tf.float32, shape=[None, num_features])
	y_ = tf.placeholder(tf.float32, shape=[None, out_features])

	W_fc1 = weight_variable([num_features, 300])
	b_fc1 = bias_variable([300])

	h_fc1 = tf.nn.relu(tf.matmul(x, W_fc1) + b_fc1)

	keep_prob = tf.placeholder(tf.float32)
	h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

	W_fc2 = weight_variable([300, out_features*2])
	b_fc2 = bias_variable([out_features*2])

	h_fc2 = tf.nn.relu(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

	W_fc3 = weight_variable([out_features*2, out_features])
	b_fc3 = bias_variable([out_features])
	out = tf.matmul(h_fc2, W_fc2) + b_fc2

	pred = tf.nn.softmax(out)

	loss = tf.nn.l2_loss(y_ - pred)

	train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)

	with sess.as_default():
		sess.run(tf.initialize_all_variables())
		for i in range(5000):
			train_step.run(feed_dict{x: batch[0], y_:batch[1], keep_prob: 0.5})
