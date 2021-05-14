#!/usr/bin/env python
# license removed for brevity

import rospy
import xlrd
import xlwt
from xlutils.copy import copy
import numpy as np



data = xlrd.open_workbook('/home/andrew/catkin_ws/src/hw5/HW5-2.xls')
table = data.sheet_by_index(0)

wb = copy(data)
ws = wb.get_sheet(0)

Qini = np.mat([[1],[0],[0],[0]])
a = np.zeros([100,3])
row=100
col=3

for i in range(row):
	for j in range(col):
		a[i][j]=table.cell(i+1,j).value

A = np.mat(a)

for k in range(row):
	q = Qini
	Jg = np.mat([[-2*q[2,0],2*q[3,0],-2*q[0,0],2*q[1,0]],
	   	     [2*q[1,0],2*q[0,0],2*q[3,0],2*q[2,0]],
	    	     [0,-4*q[1,0],-4*q[2,0],0]])
	f = np.mat([[2*(q[1,0]*q[3,0]-q[0,0]*q[2,0])-A[k,0]],
		    [2*(q[0,0]*q[1,0]+q[2,0]*q[3,0])-A[k,1]],
		    [2*(0.5-q[1,0]*q[1,0]-q[2,0]*q[2,0])-A[k,2]]])	
	q = q - Jg.T*f
	while (Jg.T*f).all() != 0:
		Jg = np.mat([[-2*q[2,0],2*q[3,0],-2*q[0,0],2*q[1,0]],
	   	  	    [2*q[1,0],2*q[0,0],2*q[3,0],2*q[2,0]],
	    		    [0,-4*q[1,0],-4*q[2,0],0]])
		f = np.mat([[2*(q[1,0]*q[3,0]-q[0,0]*q[2,0])-A[k,0]],
			    [2*(q[0,0]*q[1,0]+q[2,0]*q[3,0])-A[k,1]],
			    [2*(0.5-q[1,0]*q[1,0]-q[2,0]*q[2,0])-A[k,2]]])	
		q = q - Jg.T*f
	ws.write(k+1,3,q[0,0])
	ws.write(k+1,4,q[1,0])
	ws.write(k+1,5,q[2,0])
	ws.write(k+1,6,q[3,0])
	wb.save('/home/ncrl/catkin_ws/src/Homework5/HW5-2.xls')
	print(q)
	



