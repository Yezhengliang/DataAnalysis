#!usr/bin/env python  
# -*- coding:utf-8 _*-
# @author:Torres Ye
# @file: dataAnalysis.py
# @version:
# @time: 2018/11/18
# @email:yzlview@163.com
import pandas as pd
obj = pd.Series([1,-5,2,3],index=['a','b','c','d'])
print(obj['a'])