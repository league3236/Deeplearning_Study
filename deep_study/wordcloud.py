import json
import re

from konlpy.tag import Twitter
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

import pytagcloud
import webbrowser

#[CODE 1]
def showGraph(wordInfo):
    
    font_location = "c:/Windows/fonts/malgun.ttf" #글꼴Path
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.xlabel('주요 단어')
    plt.ylabel('빈도수')
    plt.grid(True)
    
    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True) #최대 빈도수값 저장
    Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True) #최대빈도수 단어 저장

    plt.bar(range(len(wordInfo)), Sorted_Dict_Values, align='center') #막대 그래프를 그리는 함수
    plt.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation='70')

    plt.show()

#[CODE 2]
def saveWordCloud(wordInfo, filename):
    
    taglist = pytagcloud.make_tags(dict(wordInfo).items(), maxsize=80)
    pytagcloud.create_tag_image(taglist, filename, size=(640, 480), fontname='korean', rectangular=False)#워드 클라우드를 생성
    webbrowser.open(filename)   
    
    
def main():
    
    openFileName = 'jtbcnews_facebook_2018-03-01_2018-03-31.json'
    cloudImagePath = openFileName + '.jpg'
    
    rfile = open(openFileName, 'r', encoding='utf-8').read()
    
    jsonData = json.loads(rfile)
    message = ''

    #[CODE 3]
    for item in jsonData: #message 부분 합치기
        if 'message' in item.keys():
            message = message + re.sub(r'[^\w]', ' ', item['message']) + ' '#공란 제거
    
    #[CODE 4]
    nlp = Twitter()
    nouns = nlp.nouns(message)
    count = Counter(nouns)

    #[CODE 5]
    wordInfo = dict()
    for tags, counts in count.most_common(50): #상위 50개의 리스트
        if (len(str(tags)) > 1):
            wordInfo[tags] = counts
            print ("%s : %d" % (tags, counts))
            
    showGraph(wordInfo)
    saveWordCloud(wordInfo, cloudImagePath)
    
if __name__ == "__main__":

    main()
