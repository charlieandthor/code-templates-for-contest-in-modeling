# 2.  3 sigma
# https://zhuanlan.zhihu.com/p/36297816
# https://blog.csdn.net/weixin_45109684/article/details/92633113
#基于3sigma的异常值检测
'''
假定数据服从正态分布。在3∂原则下，异常值如超过3倍标准差，那么可以将其视为异常值。
正负3∂的概率是99.7%，那么距离平均值3∂之外的值出现的概率为P(|x-u| 3∂) = 0.003，
属于极个别的小概率事件。一组测定值中与平均值的偏差超过两倍标准差的测定值 。
与平均值的偏差超过三倍标准差的测定值，称为高度异常的异常值。
在处理数据时，应剔除高度异常的异常值。

如果数据不服从正态分布，也可以用远离平均值的多少倍标准差来描述。
（这就使该原理可以适用于不同的业务场景，只是需要根据经验来
确定 k sigma中的k值，这个k值就可以认为是阈值）。
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

n = 3 # n*sigma

data = pd.read_csv('catering_sale.csv', encoding='utf-8', index_col = False) 
data_y = data[u'销量']
data_x = data[u'日期']

ymean = np.mean(data_y)
ystd = np.std(data_y)
threshold1 = ymean - n * ystd
threshold2 = ymean + n * ystd

outlier = [] #将异常值保存
outlier_x = []

for i in range(0, len(data_y)):
    if (data_y[i] < threshold1)|(data_y[i] > threshold2):
        outlier.append(data_y[i])
        outlier_x.append(data_x[i])
    else:
        continue

print('\n异常数据如下：\n')
print(outlier)
print(outlier_x)

plt.plot(data_x, data_y)
plt.plot(outlier_x, outlier, 'ro')
for j in range(len(outlier)):
    plt.annotate(outlier[j], xy=(outlier_x[j], outlier[j]), xytext=(outlier_x[j],outlier[j]))
plt.show()

'''
*********************************运行结果**************************************************

异常数据如下：

[51.0, 6607.4, 22.0, 60.0, 9106.44]
['2015/3/1', '2015/2/21', '2014/11/8', '2014/11/1', '2014/9/27']

'''
