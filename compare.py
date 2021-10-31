import pandas as pd
import numpy as np


urllist=[]
timelist=[]
data = pd.read_csv(r'/root/tingyun/exportElem.csv')

url_list=data['元素URL'].unique()
    
tests=data['时间'].unique()
for test in tests:
  test_data=data[data['时间']==test]
  for url in url list





