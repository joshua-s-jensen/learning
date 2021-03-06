import tensorflow as tf

with tf.name_scope('computation'):
    with tf.name_scope('p1'):
        a = tf.constant(5)
        b = tf.constant(4)
        c = tf.multiply(a, b)
    with tf.name_scope('p2'):
        d = tf.constant(3)
        e = tf.constant(2)
        f = tf.multiply(d, e)

with tf.name_scope('result'):
    g = tf.add(c, f)


with tf.Session() as sess:
    writer = tf.summary.FileWriter('output', sess.graph)
    print(sess.run(g))
    writer.close()