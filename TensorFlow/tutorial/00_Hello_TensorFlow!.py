import tensorflow as tf
sess = tf.Session()


hello = tf.constant("Hello, TensorFlow!")
print(sess.run(hello))

'''
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b

print(sess.run(c))
'''