#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

# 字符串去空
def str_Trim():
    s = " ,123, "
    print(s)
    s = s.strip()
    print(s)
    s = s.strip().rstrip(',')
    print(s)
    s = s.strip().lstrip(',')
    print(s)

# 字符串复制和连接
def str_copyAndCat():
    s1 = '12356954856'
    s2 = s1[-3:]
    print(s2)
    s = ';'
    sList = ['he.zhang1','li.mengchun','chang.wang','chen.yundong']
    print(s.join(sList))

# 判断字符串中是否包含另一个字符串
def str_cmpStr():
    s1 = '123'
    s2 = '12'
    print(s1.find(s2) > -1 )

# 获取字符串长度
def str_getLength():
    s = '12635'
    print(len(s))

# 翻转字符串
def str_reverseStr():
    s = 'Admingj'
    print(s[::-1])

# 分割字符串
def str_splitStr():
    s = 'he.zhang1;125;likd'
    print(s.split(';'))

# 截取字符串
def str_subStr():
    str = '0123456789'
    print(str[0:3])  # 截取第一位到第三位的字符
    print(str[:])  # 截取字符串的全部字符
    print(str[6:])  # 截取第七个字符到结尾
    print(str[:-3])  # 截取从头开始到倒数第三个字符之前
    print(str[2])  # 截取第三个字符
    print(str[-1])  # 截取倒数第一个字符
    print(str[::-1])  # 创造一个与原字符串顺序相反的字符串
    print(str[-3:-1])  # 截取倒数第三位与倒数第一位之前的字符
    print(str[-3:])  # 截取倒数第三位到结尾
    print(str[:-5:-3])  # 逆向截取，倒数第一位与倒数第五位之间的字符，步长为3

# 字符串的判断函数
def str_Judge():
    S = '123'
    print(S.isalnum()) # 是否全是字母和数字，并至少有一个字符
    print(S.isalpha())  # 是否全是字母，并至少有一个字符
    print(S.isdigit()) # 是否全是数字，并至少有一个字符
    print(S.isspace())  # 是否全是空白字符，并至少有一个字符
    print(S.islower())  # S中的字母是否全是小写
    print(S.isupper())  # S中的字母是否便是大写
    print(S.istitle())  # S是否是首字母大写的

# 数字左填充0
def Number_LFill():
    n = '123'
    print(n.zfill(5));
    n = 123
    s = '%05d' % n
    print(s)

# 数字保留两位小数
def Number_Fixed():
    n = 123.126
    print('%.2f' % n)
    print(round(n,2))
    print(format(n,'.2f'))