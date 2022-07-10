# 1.简单的描述性统计分析方法
# https://blog.csdn.net/weixin_45109684/article/details/92633113
'''
可以先对变量做一个描述性统计，进而查看哪些数据是不合理的。
最常用的统计量是最大值和最小值，用来判断这个变量的取值是否超出了合理的范围
'''
import pandas as pd
data = pd.read_csv('secondary_data.csv', encoding = 'utf-8')
print(data.describe())
'''只可以对连续型变量进行分析'''
