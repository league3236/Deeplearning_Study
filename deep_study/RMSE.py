import numpy as np

#코딩으로 평균제곱근 오차 구하기

#임의의 a,b 데이터
ab = [3,76]

# 공부한 시간에 따른 성적을 짝 지어 저장
data = [[2,81],[4,93],[6,91],[8,97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

# 일차 방정식 y = ax + b를 구한다.
def predict(x):
    return ab[0]*x + ab[1]

#평균 제곱근 공식을 파이썬 함수로 옮김
def rmse(p,a):
    return np.sqrt(((p-a)**2).mean())

def rmse_val(predict_result,y):
    return rmse(np.array(predict_result), np.array(y))

#예측 값이 들어갈 빈 리스트를 만든다.
predict_result = []

#모든 x 값을 한 번씩 대입하여
for i in range(len(x)):
    #그 결과 predict_result 리스트를 완성한다.
    predict_result.append(predict(x[i]))
    print("공부한 시간=%.f, 실제 점수=%.f, 예측 점수=%.f" % (x[i],y[i],predict(x[i])))

#최종 RMSE
print("rmse 최종값: " + str(rmse_val(predict_result,y)))


