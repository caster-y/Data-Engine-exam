# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:13:25 2020

@author: yanming4
"""
#efficient_apriori找到商品和用户之间的关系
import pandas as pd
import time
data=pd.read_csv('./订单表.csv',encoding='gbk')
data.drop(data[data['产品名称'] =='none'].index)
from efficient_apriori import apriori
start = time.time()
data1=data.sort_values(by='客户ID',axis=0,ascending=True)
orders_series = data1.set_index('客户ID')['产品名称']
transactions = []
temp_index = 0
for i, v in orders_series.items():
    if i != temp_index:
        temp_set=set()
        temp_index=i
        temp_set.add(v)
        transactions.append(temp_set)
    else:
        temp_set.add(v)
print(transactions)
itemsets,rules = apriori(transactions,min_support=0.02,min_confidence=0.5)
print('频繁项集：', itemsets)
print('关联规则：', rules)
end=time.time()
print('用时：',end-start)

#使用mlxtend.frequent_patterns工具包

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
hot_encoded_df=data.groupby(['客户ID','产品名称'])['产品名称'].count().unstack().reset_index().fillna(0).set_index('客户ID')
hot_encoded_df = hot_encoded_df.applymap(encode_units)
frequent_itemsets = apriori(hot_encoded_df, min_support=0.02, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)
print(frequent_itemsets)
print(rules)



        