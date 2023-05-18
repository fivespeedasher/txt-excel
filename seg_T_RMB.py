"""
将如下格式转换成表格:
    2月8日
    1 广湛九标二分部 10 2000
"""

import pandas as pd
import re
from datetime import datetime

pattern = re.compile(r' +')
xlm_name = datetime.now().strftime('%Y_%m_%d')+'.xlsx'   #新表格文件为日期
colum = ["日期", "标段", "吨位", "价格", "备注"]

date = str(xlm_name)
trade = dict({"日期":[], "标段":[], "吨位":[], "价格":[], "备注":[]})

with open("标段_T_RMB.txt", 'r', encoding='utf-8') as f:
    for line in f.readlines():
        # line = line.strip().split(' ')
        line = line.strip()
        line = re.split(' +', line)
        if(len(line) == 1): 
            date = line[0]
        elif(len(line) == 4 or len(line) == 5):
            trade['日期'].append(date)
            trade['标段'].append(line[1])
            trade['吨位'].append(line[2])
            trade['价格'].append(line[3])
            if(len(line) == 5):
                trade['备注'].append(line[4])
            else:
                trade['备注'].append(' ')

            
        elif(len(line) == 0): pass
        else:  # 出现了行元素数目不对的情况
            print(len(line))
            print(date)
            assert(1 == 0)

    df = pd.DataFrame(trade, index=range(1, len(trade['价格']) + 1), columns=colum)
    df.to_excel('./output/'+xlm_name)
        
