import redis
# from jieba import analyse
import jieba
import numpy as np
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import PIL.Image as Image
import  matplotlib.pyplot as plt
r = redis.StrictRedis(host='localhost', port=6379, db=2, decode_responses=True)
string = ''
for i in range(1, 501):
    string = string + (str(r.hgetall('comments:{}'.format(i))['comment']))
# print(string)
# """判断一个unicode是否是汉字"""


def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


#  """判断一个unicode是否是英文字母"""
def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False


def format_str(content):
    content_str = ''
    for i in content:
        if is_chinese(i) or is_alphabet(i):
            content_str = content_str + i
    return content_str
result_content = format_str(string)
cut = jieba.cut(result_content)  #text为你需要分词的字符串/句子
result_string = ' '.join(cut)  #将分开的词用空格连接
# k = jieba.analyse.extract_tags(result_content, topK=50, withWeight=True)
# print(k)
font = r'C:\Users\DELL\Downloads\FZFengYKSJ.TTF'
wc = WordCloud(font_path=font,
               background_color='white',
               width=1000,
               height=800,
               stopwords = STOPWORDS.add("电影")
               ).generate(result_string)
wc.to_file('ss.png')
plt.imshow(wc)  #用plt显示图片
plt.axis('off') #不显示坐标轴
plt.show() #显示图片


