# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:58:39 2022

@author: fitsum
"""


from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0,0],[1,1],[2,2]],[0,1,2])
