#https://qiita.com/taigamikami/items/7d915615d1478e19f133
'''
input 28*28*1
covoltion 2x2
max pooling 2x2
covoltion2 2x2
max pooling2 2x2
結合
Dropuot
読み出し
'''
#MNISTのダウンロード&読み込み?
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot = True)

import tensorflow as tf

#入力x,正解y_の作成
x = tf.placeholder(tf.float32, shape=[None, 784]) 
y_ = tf.placeholder(tf.float32, shape=[None, 10])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

#重みの初期値
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

#バイアス(０だと進まない)    
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


#よくわからん↓
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')

#プーリング層
    '''
    ksize=[1,2,2,1] 2x2のブロックを適応
    strides=[1,2,2,1] 2pxずつずらす
    padding='SAM' 左右に0を付けたデータに変換
                    (出力が入力と同じサイズになるように0で埋める)
    '''
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

#第一畳み込み
W_conv1 = weight_variable([5,5,1,32]) #[パッチサイズ,入力チャンネル数,出力チャンネル数]
b_conv1 = bias_variable([32]) #バイアスの設定　上記と同じにする

x_image = tf.reshape(x, [-1, 28, 28, 1]) #[?,x,y,色]

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1) #covoltion
h_pool1 = max_pool_2x2(h_conv1) #pooling
'''
ここまでで、x_image、重みテンソルと畳み込み、バイアスを加え、ReLU関数,プールを適用する。
このmax_pool_2x2方法では、画像サイズを14x14に縮小する。
'''

#第二畳み込み
W_conv2 = weight_variable([5,5,32,64]) #5*5パッチが32種類の64個
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)
#7x7で出力

#結合層
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

#Dropout 過学習防止
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

#読み出し
W_fc2 = weight_variable([1024,10]) #1024行x10列(0~9の確立)
b_fc2 = bias_variable([10])

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))



#モデルのトレーニングと評価
'''
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))reduce_mean()は平均値を取る
tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv)は正解ラベル(y_)と推定値(y_conv)を比べる
tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)で学習の仕方を設定今回はAdamOptimizer
'''

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  for i in range(15000):
       # # バッチ数分だけ、mnistからランダムに選択し、データを返すメソッド
    batch = mnist.train.next_batch(50)
    #学習部分
    if i % 100 == 0:
      train_accuracy = accuracy.eval(feed_dict={
          x: batch[0], y_: batch[1], keep_prob: 1.0})
      print('step %d, training accuracy %g' % (i, train_accuracy))
    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

  print('test accuracy %g' % accuracy.eval(feed_dict={
      x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))