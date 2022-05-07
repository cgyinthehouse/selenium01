from opencc import OpenCC
text1="我去过清华大学和交通大学，打印机、光盘、内存。"
text2="我去過清華大學和交通大學，印表機、光碟、記憶體。"

text1="""
SQL 是用于访问和处理数据库的标准的计算机语言。

在本教程中，您将学到如何使用 SQL 访问和处理数据系统中的数据，这类数据库包括：Oracle, Sybase, SQL Server, DB2, Access 等等。

开始学习 SQL ！

注：本教程中出现的姓名、地址等信息仅供教学，与实际情况无关。
"""

openCC = OpenCC('s2t')                # 建立opencc型別物件，並設定轉換模式
line = openCC.convert(text1)
print("      "+text1)
print("s2t  :"+line)
line =openCC.set_conversion('s2twp')  # 設定轉換模式
line = openCC.convert(text1)          # 轉換
print("s2twp:"+line)

line =openCC.set_conversion('t2s')
line = openCC.convert(text2)
print("      "+text2)
print("t2s  :"+line)
line =openCC.set_conversion('tw2sp')
line = openCC.convert(text2)
print("tw2sp:"+line)