#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import requests
import sys
import os
import time
'''# t代表身份证号码的位数，w表示每一位的加权因子
t = []
w = []
for i in range(0,18):
    t1 = i + 1
    t.append(t1)
    w1 = (2 ** (t1-1)) % 11
    w.append(w1)
#队列w要做一个反序
w = w[::-1]  
#print w
# 根据前17位的余数，计算第18位校验位的值
def for_check(n):
    # t = 0
    for i in range(0,12):
        if (n + i) % 11 == 1:
            t = i % 11
    if t == 10:
        t = 'X'
    return t
   
# 根据身份证的前17位，求和取余，返回余数
def for_mod(id):
    sum = 0
    for i in range(0,17):
        sum += int(id[i]) * int(w[i])
        # print(int(id[i]),int(w[i]),sum)
    sum = sum % 11
    #print(sum)
    return sum

# 验证身份证有效性
def check_true(id):
    # print(for_check(for_mod(id[:-1])))
    if id[-1] == 'X':
        if for_check(for_mod(id[:-1])) == 'X':
            return True
        else:
            return False
    else:
        if for_check(for_mod(id[:-1])) == int(id[-1]):
            return True
        else:
           return False

# 获取日期列表，从01到31
day = []
for i in range(0,4):
    for j in range(0,10):
        d = str(i) + str(j)
        day.append(d)
        if d == '31':
            break
    if d == '31':
        break
day = day[1:]
print day

# 获取月份列表，从01到12
month = []
for i in range(0,3):
    for j in range(0,10):
        d = str(i) + str(j)
        month.append(d)
        if d == '12':
            break
    if d == '12':
        break
month = month[1:] 

# 获取年月列表，从0101到1231，剔除不存在的日期
mmdd = []
for i in month:
    for j in day:
        md = i + j
        mmdd.append(md)
mmdd.remove('0230')
mmdd.remove('0231')
mmdd.remove('0431')
mmdd.remove('0631')
mmdd.remove('0931')
mmdd.remove('1131')

#以下代码用于遍历所有日期，打印出通过校验的身份证号码
id1 = '3522012000'
id3 = '0016m'
j = 0
for i in mmdd:
    theid = id1 + i + id3
    if check_true(theid):
        print(theid)
        j += 1

'''
FILE_PATH = 'guozihan.txt'#modify 
def read_file(file_path): 
    url= list() 
    with open(file_path, 'r') as f: 
        txt = f.read() 
        for line in txt.split('\n'):  
                url.extend(line.split()) 
    return url
print read_file(FILE_PATH)
url=read_file(FILE_PATH)

FILE_PATH = 'guozihan_formdata.txt'#modify 
def read_file(file_path): 
    formdata= list() 
    with open(file_path, 'r') as f: 
        txt = f.read() 
        for line in txt.split('\n'):  
                formdata.extend(line.split()) 
    return formdata
print read_file(FILE_PATH)
