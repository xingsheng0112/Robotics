#!/usr/bin/env python
# license removed for brevity

import rospy
import xlrd
import numpy as np



data = xlrd.open_workbook('/home/andrew/catkin_ws/src/hw5/HW5-1.xls')
table = data.sheet_by_index(0)

a = np.zeros([50,3])
b = np.zeros([50,1])
row=50
col=2
for i in range(row):
	for j in range(col):
		a[i][j]=table.cell(i+1,j).value
	b[i]=table.cell(i+1,2).value
	a[i][2]=1
		
A = np.mat(a)
Y = np.mat(b)

x = (A.T*A).I*A.T*Y
print(x)
