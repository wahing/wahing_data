'''
Created on Feb 12, 2020

@author: zero
'''
import pandas as pd
pd.set_option('expand_frame_repr', False) #当列太多时不换行
pd.set_option('display.max_row',1000) #最多显示多少行
#pd.set_option('precision',6) #浮点数的精度
df = pd.read_csv(filepath_or_buffer='./bitmex_data.csv'#,skiprow=1 忽略第一行
                #,sep=';'分隔符,usecols=['open_time','open','close','high','low','volume']
                )
#print(df)
#print(df.dtypes)
#print(df.shape) #有几行几列
#print(df.columns)
# print(df.index)
# for index in df.index:
#     print(index)
#     
# print(df.head(3)) #显示前几行 默认5
# print(df.tail(3)) #显示后几行 默认5
# print(df.sample(n=3)) #随机抽取3行
# print(df.sample(frac=0.3)) #按固定比例来选
#print(df.describe()) #非常方便的函数，对每一列数据有直观感受；只会对数字类型的列有效 

###pandas对数据的访问和操作###
#如何选取指定的列和行
#print(df['open'])
#同时获取两列 需要两个[]
# print(df[['open_time','close']])
print(df[['open_time']])
exit()
#增加列
df['mark'] = "北京时间"
nums = [i for i in range(0,940,1)]
# df['number'] = nums
# print(df)
# df['open_time'] = df['open_time'] + pd.Timedelta(hours=8)
# print(df)

#iloc 通过position来读取数据 loc
# print(df.iloc[0])
# print(df.iloc[0]['open'])
print(df.iloc[1:3]) #选取在此范围内的多列，读取的数据是dataframe类型
print(df.iloc[:,1:3])#选取指定的多列，
