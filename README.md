# DataMing
发现软件项目中标签的关联规则
>（项目参考Python数据挖掘-Megan Squire书籍）
+ 从Freecode上下载数据，并解析出项目数据，将其组织为数据库表，并提供了基本的数据可视化处理。此项目可以找出哪些项目标签在FLOSS项目中经常同时出现。
+ 数据集存储在mysql数据库，共30多万条数据，从数据标签中使用Apriori算法找出频繁项集，并生成后续的关联规则  
###### 满足支持阈值条件的二元组 （这里的支持度阈值取的是5%）
![image](https://github.com/Endless-Android/DataMing/blob/master/picture/doubleTon.jpg)
###### 满足支持阈值条件的三元组 （这里的支持度阈值取的是5%）
![image](https://github.com/Endless-Android/DataMing/blob/master/picture/tripleTon.jpg)
###### 打印每条规则的支持度，置信度以及附加值得分（附加值得分 = 整条规则的置信度减去右侧项支持度）
![image](https://github.com/Endless-Android/DataMing/blob/master/picture/AssociationRules.jpg)
