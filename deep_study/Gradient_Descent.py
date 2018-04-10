import tensorflow as tf

data = [[2,0,81],[4,4,93],[6,2,91],[8,3,97]]
x1 = [x_row1[0] for x_row1 in data]
x2 = [x_row2[1] for x_row2 in data]    #새로 추가되는 값
y_data = [y_row[2] for y_row in data]

learning_rate = 0.1

a1= tf.Variable(tf.random_uniform([],0,10,dtype = tf.float64, seed = 0))    #0~10사이의 기울기를 넣었음 / tf.float94 = 실수형 / 실행시 같은값이 나올수 있게 seed의 값을 선택.
a2= tf.Variable(tf.random_uniform([],0,10,dtype = tf.float64, seed = 0))    #새로 추가되는 값
b = tf.Variable(tf.random_uniform([1],0,100, dtype = tf.float64, seed = 0)) #y절편은 0~100사이에서 임의의 값을 얻게끔 함.

# 일차 방정식 ax+b의 식을 구현

y = a1*x1+a2*x2 + b

# 텐서 플로우를 이용해 편균 제곱근의 오차를  구현
rmse = tf.sqrt(tf.reduce_mean(tf.square(y-y_data)))

#경사 하강법 실행 차례
#텐서플로의 GradientDescentOptimizer() 함수에 저장되어 있음
gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

#텐서플로우를 실행시키고, 결과값을 출력
with tf.Session() as sess:
    #변수 초기화
    sess.run(tf.global_variables_initializer())
    #2001번 실행(0번째를 포함하므로)
    for step in range(2001):
        sess.run(gradient_decent)
        #100번마다 결과 출력
        if step % 100 == 0:
            print("Epoch: %.f, RMSE = %.04f, 기울기 a1 = %.4f, 기울기 a1 = %.4f, y 절편 b = %.4f" % (step,sess.run(rmse),sess.run(a1),sess.run(a2),sess.run(b)))
