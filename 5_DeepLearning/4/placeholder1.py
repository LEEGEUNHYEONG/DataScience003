import tensorflow as tf

#   placeholder 정의하기
a = tf.placeholder(tf.int32, [3])

#   배열을 모든 값을 2배 연산 정의
b = tf.constant(2)
x2_op = a * b

#   세션 시작
sess = tf.Session()

#   placeholder에 값 넣고 실행
r1 = sess.run(x2_op, feed_dict={a:[1, 2, 3]})
print(r1)
r2 = sess.run(x2_op, feed_dict={a:[10, 20, 10]})
print(r2)