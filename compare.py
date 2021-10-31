import pandas as pd
import numpy as np


urllist=[]
timelist=[]
data = pd.read_csv(r'/root/tingyun/exportElem.csv',index_col='时间')

# add all url in list
for each in data.元素URL:
  if each not in urllist:
    urllist.append(each)

# add all time in list:

for each in data.时间:
  if each not in timelist:
    timelist.append(each)

#def sort():
    








for each in timelist:
    test=data.query("时间==@each")
    for onetest in test:
        result = pd.DataFrame()
        # get down 3 kb
        curl3 = test[test['元素URL'].str.contains('com/F3KB')]
        curl3 = curl3.sort_values(by='总下载时间')
       # result=result.

result=pd.concat(result)
