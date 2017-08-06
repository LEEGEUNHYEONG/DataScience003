#   tensorboard 설치 해야 함
import tensorflow as tf

#   데이터 플로우 그래프 구축하기
a = tf.constant(20, name="a")
b = tf.constant(30, name="b")
mul_op = a * b

#   세션 생성하기
sess = tf.Session()

#   TensorBoard 사용
#   SummaryWriter 없음, tf.train.SummaryWriter -> tf.summary.FileWriter
tw = tf.summary.FileWriter ("log_dir", graph=sess.graph)

result = sess.run(mul_op)

#   세션 실행
print(result)