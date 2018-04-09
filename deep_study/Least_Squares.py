import numpy as np

x = [2, 4, 6, 8]
y = [81, 93, 91, 97]

mx = np.mean(x) #x의 평균을 구해서 mx에 집어넣음
my = np.mean(y) #y의 평균을 구해서 my에 집어넣음
print("x의 평균값:",mx)
print("y의 평균값:",my)

divisor = sum([(mx-i)**2 for i in x]) #for i in x는 x의 각 원소를 한번씩 i에 대입하라는 뜻이다. / **2sms 제곱을 구하라는 의미이다.

#기울기 공식의 분자
def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return d
dividend = top(x, mx, y, my)

print("분모:",divisor)
print("분자:",dividend)
# 분모와 분자를 계산하여 기울기 a를 구함
a = dividend / divisor

# y절편을 구하는 공식을 이용해 b를 구해본다.
b = my - (mx*a)

print("기울기 a =", a)
print("y 절편 b =", b)

