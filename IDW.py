import pandas as pd
import numpy as np

# 待求缺失值城市经纬度
# 镇江  
##LON = 119.45
##LAT = 32.2
# 长沙  
##LON = 112.59
##LAT = 28.12
# 中山  
##LON = 113.38
##LAT = 22.52
# 成都  
LON = 104.06
LAT = 30.67
# 儋州 
##LON = 109.576782
##LAT = 19.517486

R = 6371
x = R*np.cos(LAT)*np.cos(LON)
y = R*np.cos(LAT)*np.sin(LON)

data = pd.read_csv('stations-pre.csv', encoding = 'utf-8')
# 距离
xi = R*np.cos(data['LAT'])*np.cos(data['LON'])
yi = R*np.cos(data['LAT'])*np.sin(data['LON'])
distance = ((x-xi)**2+(y-yi)**2)**0.5
# 权重
w = 1/distance/sum(1/distance)
# 只要前三个
ww = sorted(list(w), reverse=True)[:3]
# 高程
z = sum(w*data['ALT'])
z = ww[0]*data['ALT'][list(w).index(ww[0])]+ww[1]*data['ALT'][list(w).index(ww[1])]+ww[2]*data['ALT'][list(w).index(ww[2])]
print(z)
