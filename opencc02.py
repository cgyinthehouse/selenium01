from opencc import OpenCC

import urllib.request as httplib  # 3.x
try:
    url="https://www.w3school.com.cn/sql/index.asp"  # http ,   https
    # url="https://tw.news.yahoo.com/"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        # contents=reponse.read().decode(reponse.headers.get_content_charset())
        contents=reponse.read()
        # contents2=reponse.read().decode("utf-8")   # bytes 轉成str
        # contents=reponse.read().decode("big-5")
        print(contents)
except:
    print("error")

text1=contents.decode("gbk")
openCC = OpenCC('s2t')
line =openCC.set_conversion('s2twp')
line = openCC.convert(text1)
print("s2twp:"+line)
line=line.replace('<html lang="zh-cn">','<html lang="utf-8">').replace('charset="gbk"','charset="utf-8"')
fr = open('workfile.html', 'w',encoding="utf-8")
fr.write(line)
fr.close()
