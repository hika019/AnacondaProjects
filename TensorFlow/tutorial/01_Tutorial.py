#https://qiita.com/taigamikami/items/1bda03d20928bf98f36e
import tensorflow as tf
sess = tf.Session()



node1 = tf.constant(3.0, dtype=tf.float32) #定数3.0
node2 = tf.constant(4.0)
print(node1, node2) #a,bの出力


#print(sess.run([node1, node2]))


# node1+node2の出力
node3 = tf.add(node1, node2) #node1 + node2
print('node3', node3)
print("sess.run(node3):", sess.run(node3))



'''
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a + b

print(sess.run(adder_node, {a:3, b:4.5})) #a=3 b=4.5の合計
print(sess.run(adder_node, {a:[1,3], b:[2,4]})) #a=[1,3] b=[2,4]の合計

add_and_triple = adder_node * 3.0
print(sess.run(add_and_triple, {a: 3, b: 4.5}))
'''

'''
W = tf.Variable([.3], dtype=tf.float32) #0.3
b = tf.Variable([-.3], dtype=tf.float32) #-0.3
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
linear_model = W * x + b -y
init = tf.global_variables_initializer()

sess.run(init)

print(sess.run(linear_model, {x: [1, 2, 3, 4], y: [2, 5, -4, 10]}))
'''