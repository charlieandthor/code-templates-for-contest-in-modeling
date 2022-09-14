# code-templates-for-contest-in-modeling
模型简述及代码

## 1.反距离加权法（Inverse Distance Weighted）插值  
[stations-pre.csv](https://github.com/charlieandthor/code-templates-for-contest-in-modeling/blob/main/stations-pre.csv)  
[IDW.py](https://github.com/charlieandthor/code-templates-for-contest-in-modeling/blob/main/IDW.py)  
首先把经纬度转换成空间直角坐标来计算两点之间的直线距离  
https://blog.csdn.net/ss19890125/article/details/46335467  
然后根据IDW的公式算出权重和插值点的值   
https://zhuanlan.zhihu.com/p/508842098  

## 2.异常值检测--孤立森林 Isolation Forest  
https://blog.csdn.net/u013250861/article/details/124329133  
https://www.jianshu.com/p/dbb98e9d8aa4  
[outlier_IF.py](https://github.com/charlieandthor/code-templates-for-contest-in-modeling/blob/main/outlier_IF.py)

## 3.异常值检测--3 sigma
[catering_sale.csv](https://github.com/charlieandthor/code-templates-for-contest-in-modeling/blob/main/catering_sale.csv)  
[outlier_3sigma.py](https://github.com/charlieandthor/code-templates-for-contest-in-modeling/blob/main/outlier_3sigma.py)

## 4.异常值检测--简单的描述性统计分析方法
[outlier_simp.py](https://github.com/charlieandthor/code-templates-for-contest-in-modeling/blob/main/outlier_simp.py)

## 5.批量读入文件  
Python: 
```
# 批量读入每一条线文件
line = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19]\
for i in line:\
    station = pd.read_csv('att2_1_station.csv')\
    if len(str(i)) == 1:\
        dis = pd.read_csv('dis00'+str(i)+'.csv')\
    else:\
        dis = pd.read_csv('dis0'+str(i)+'.csv')\
```
MATLAB:  
https://lishizheng.blog.csdn.net/article/details/116760408  
Python实现批量修改文件名、文件夹名:  
https://blog.csdn.net/liguo_yao/article/details/80934420  
