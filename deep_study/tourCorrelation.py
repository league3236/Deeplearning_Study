import json
import math
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

import pandas as pd

#[CODE 1]
def correlation(x, y): #상관관계 분석을 위한 함수
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0
    
    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)
    
    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / math.sqrt( ((n*x_sum_pow) - pow(x_sum, 2)) * ((n*y_sum_pow) - pow(y_sum, 2)) )
    except:
        r = 0.0
    
    return r

#[CODE 2]    
def setScatterGraph(tour_table, fv_table, tourpoint):
    
    #[CODE 8]
    tour = tour_table[tour_table['resNm'] == tourpoint]
    merge_table = pd.merge(tour, fv_table, left_index=True, right_index=True)

    fig = plt.figure()
    
    fig.suptitle(tourpoint + '상관관계 분석')
    
    plt.subplot(1, 3, 1)
    plt.xlabel('중국인 입국수')
    plt.ylabel('외국인 입장객수')
    r1 = correlation(list(merge_table['china']), list(merge_table['ForNum']))
    plt.title('r = {:.5f}'.format(r1))
    plt.scatter(list(merge_table['china']), list(merge_table['ForNum']), edgecolor='none', alpha=0.75, s=6, c='black')

    plt.subplot(1, 3, 2)
    plt.xlabel('일본인 입국수')
    plt.ylabel('외국인 입장객수')
    r2 = correlation(list(merge_table['japan']), list(merge_table['ForNum']))
    plt.title('r = {:.5f}'.format(r2))
    plt.scatter(list(merge_table['japan']), list(merge_table['ForNum']), edgecolor='none', alpha=0.75, s=6, c='black')

    plt.subplot(1, 3, 3)
    plt.xlabel('미국인 입국수')
    plt.ylabel('외국인 입장객수')
    r3 = correlation(list(merge_table['usa']), list(merge_table['ForNum']))
    plt.title('r = {:.5f}'.format(r3))
    plt.scatter(list(merge_table['usa']), list(merge_table['ForNum']), edgecolor='none', alpha=0.75, s=6, c='black')

    plt.tight_layout()

    #fig = matplotlib.pyplot.gcf()
    #fig.set_size_inches(10, 7)
    #fig.savefig(tourpoint+'.png', dpi=300)
 
    plt.show()
    return [tourpoint, r1, r2, r3]
        
def main():
    #[CODE 3]
    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)
    #해당 열의 인덱스 값을 가지고 ‘drop()’ 함수를 사용하여 데이터를 삭제한 후 ‘sort()’를 이용하여 ‘china’ 열을 내림차순으로 정렬

    #[CODE 4]
    tpFileName = '서울특별시_관광지입장정보_2011_2016.json'
    jsonTP = json.loads(open(tpFileName, 'r', encoding='utf-8').read())
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm', 'resNm', 'ForNum'))
    tour_table = tour_table.set_index('yyyymm') #json 값을 원래는 데이터만 추출.
    
    #[CODE 5]
    resNm = tour_table.resNm.unique()
    
    #[CODE 6]
    fv_CFileName = '중국(112)_해외방문객정보_2011_2016.json'
    jsonFV = json.loads(open(fv_CFileName, 'r', encoding='utf-8').read())
    china_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
    china_table = china_table.rename(columns={'visit_cnt': 'china'})
    china_table = china_table.set_index('yyyymm')

    fv_JFileName = '일본(130)_해외방문객정보_2011_2016.json'
    jsonFV = json.loads(open(fv_JFileName, 'r', encoding='utf-8').read())
    japan_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
    japan_table = japan_table.rename(columns={'visit_cnt': 'japan'})
    japan_table = japan_table.set_index('yyyymm')

    fv_UFileName = '미국(275)_해외방문객정보_2011_2016.json' 
    jsonFV = json.loads(open(fv_UFileName, 'r', encoding='utf-8').read())
    usa_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns={"visit_cnt": "usa"})
    usa_table = usa_table.set_index('yyyymm')
    #중국인, 일본인 입국수와 미국인 입국수를 처리

    #[CODE 7]
    fv_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    fv_table = pd.merge(fv_table, usa_table, left_index=True, right_index=True)
    #resNM’에서 추출하는 관광지 이름과, ‘tour_table’, ‘fv_table’을 인자로 하여 ‘setScatterGraph()’ 함수를 호출
    r_list = []
    for tourpoint in resNm:
        #[CODE 9]
        r_list.append(setScatterGraph(tour_table, fv_table, tourpoint)) # 함수를 수행하면서 반환한 리스트 값을 추가하여, 각 관광지마다 상관계수 값을 가지고 온다.
    
    #[CODE 10]
    r_table = pd.DataFrame(r_list, columns=('tourpoint', 'china', 'japan', 'usa'))
    r_table = r_table.set_index('tourpoint')
    r_table = r_table.drop('서울시립미술관 본관')
    r_table = r_table.drop('서대문자연사박물관')
    r_table.plot(kind='bar', rot=70)
    plt.show()
           
if __name__ == "__main__":

    main()


