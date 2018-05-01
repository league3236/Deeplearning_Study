import json
import re

from konlpy.tag import Twitter
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

import pytagcloud
import webbrowser


# [CODE 1]
def showGraph(wordInfo):
    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.xlabel('주요 단어')
    plt.ylabel('빈도수')
    plt.grid(True)

    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
    Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True)

    plt.bar(range(len(wordInfo)), Sorted_Dict_Values, align='center')
    plt.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation='70')

    plt.show()


# [CODE 2]
def saveWordCloud(wordInfo, filename):
    taglist = pytagcloud.make_tags(dict(wordInfo).items(), maxsize=80)
    pytagcloud.create_tag_image(taglist, filename, size=(640, 480), fontname='korean', rectangular=False)
    webbrowser.open(filename)


def main():
    openFileName = 'KakaoTalk'
    cloudImagePath = openFileName + '.jpg'

    rfile = open('KakaoTalk.txt', 'rt', encoding='UTF8')
    message = rfile.read()

    # [CODE 4]
    nlp = Twitter()
    nouns = nlp.nouns(message)
    count = Counter(nouns)

    # [CODE 5]
    wordInfo = dict()
    for tags, counts in count.most_common(50):
        if (len(str(tags)) > 1):
            wordInfo[tags] = counts
            print("%s : %d" % (tags, counts))

    showGraph(wordInfo)
    saveWordCloud(wordInfo, cloudImagePath)


if __name__ == "__main__":
    main()
