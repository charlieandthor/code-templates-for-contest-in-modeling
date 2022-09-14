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
for i in line:
    station = pd.read_csv('att2_1_station.csv')
    if len(str(i)) == 1:
        dis = pd.read_csv('dis00'+str(i)+'.csv')
    else:
        dis = pd.read_csv('dis0'+str(i)+'.csv')
```  
MATLAB:  
https://lishizheng.blog.csdn.net/article/details/116760408  
Python实现批量修改文件名、文件夹名:  
https://blog.csdn.net/liguo_yao/article/details/80934420  

## 6.pandas系列  
常用命令  
https://blog.csdn.net/weixin_39670441/article/details/110925731  
取dataframe特定行/列  
```
start = df.iloc[i, 1]
end = df.iloc[i, 2]
```
https://blog.csdn.net/dili8870/article/details/101506598  
DataFrame随机抽样  
https://blog.csdn.net/qq_38923076/article/details/82925238  
DataFrame 数据替换  
https://blog.csdn.net/weixin_44493841/article/details/122213842  
数据筛选  
https://blog.csdn.net/joker_zsl/article/details/119874694  
选择满足特定条件的行  
https://blog.csdn.net/Janine_1991/article/details/115508987  
read_csv 和 to_csv  
https://blog.csdn.net/qq_41895190/article/details/103332440    
```
pd.DataFrame(mp).to_csv('mp.csv', index=None, header=None)
```
数据排序  
https://zhiqianghe.blog.csdn.net/article/details/108013889  
数据合并与重塑 (pd.concat)  
https://blog.csdn.net/Mr_HHH/article/details/79488445  
随机抽样（不要随便抽样）
```
df = df.sample(n=5000)  
```
## 7.ROC曲线  
https://blog.csdn.net/qq_35098624/article/details/106456237  
https://www.jianshu.com/p/2ca96fce7e81  

## 8.绘图
### Python
直方图  
https://www.cnblogs.com/LiErRui/articles/11588399.html 
```
# 绘制直方图
plt.hist(x = dis, # 指定绘图数据
         bins = 20, # 指定直方图中条块的个数
         color = colors[4], # 指定直方图的填充色
         edgecolor = 'k' # 指定直方图的边框色
         )
# 添加x轴和y轴标签
plt.xlabel(u'出行距离（米）')
plt.ylabel(u'乘客数')
# 添加标题
plt.title(u'乘客出行距离分布')
# 显示图形
plt.grid(ls="--",lw=0.5,color=colors[8])
plt.show()
```
柱状图+拟合线  
https://blog.csdn.net/chenran187906/article/details/102639618  
完善及美化：标签，网格，颜色...  
https://blog.csdn.net/weixin_41685388/article/details/109178092  
matplotlib显示中文（包含字体选择）  
https://blog.csdn.net/weixin_42870380/article/details/94883827  
箱线图  
https://blog.csdn.net/weixin_33428129/article/details/114910341  
https://blog.csdn.net/qq_36523839/article/details/80654277  
相关系数矩阵与热力图  
https://blog.csdn.net/cymy001/article/details/79576019  
### MATLAB
拟合函数  
https://blog.csdn.net/Bily_on/article/details/104309211
