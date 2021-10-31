import pandas as pd
import numpy as np


list=[]
data = pd.read_csv(r'/root/tingyun/exportElem.csv')

# add all url in list
for each in data.元素URL:
  if each not in list:
    list.append(each)



def counter(url):
 data = pd.read_csv(r'exportElem.csv')
 data['summary']= data.DNS时间 + data.建立连接时间+data.发出请求时间+data.首包时间+data.剩余包时间+data.SSL握手时间+data.关闭连接时间+data.阻塞时间
 i=0
 for index,row in data.iterrows():
   if url in row.元素URL:
     i=i+1  
 result=url+','+str(i)
 print(result)

def counterror(url):
  data = pd.read_csv(r'exportElem.csv')
  data['summary']= data.DNS时间 + data.建立连接时间+data.发出请求时间+data.首包时间+data.剩余包时间+data.SSL握手时间+data.关闭连接时间+data.阻塞时间
  i=0
  for index,row in data.iterrows():
   if url in row.元素URL :
     if row.summary > 15000:
       i=i+1
       print (row.时间)
   result=url+','+str(i)
  print('%s error number is %s' %(url,i))

def countslow(url):
  data = pd.read_csv(r'exportElem.csv')
  data['summary']= data.DNS时间 + data.建立连接时间+data.发出请求时间+data.首包时间+data.剩余包时间+data.SSL握手时间+data.关闭连接时间+data.阻塞时间
  i=0
  for index,row in data.iterrows():  
   if url in row.元素URL:
     if row.summary > 2000 and row.summary < 15000:
       i=i+1
       print (row.时间)
   result=url+','+str(i)
  print('%s slow number is %s' %(url,i))

def counter504(url):
 data = pd.read_csv(r'exportElem.csv')
 data['summary']= data.DNS时间 + data.建立连接时间+data.发出请求时间+data.首包时间+data.剩余包时间+data.SSL握手时间+data.关闭连接时间+data.阻塞时间
 i=0
 for index,row in data.iterrows():
   if url in row.元素URL:
    if row.HTTP状态码 == 0 :
     i=i+1
     print (row.时间)
   result=url+','+str(i)
 print('%s return 0 number is %s' %(url,i))

for each in list:
    counter(str(each))
    counterror(str(each))
    countslow(str(each))
    counter504(str(each))