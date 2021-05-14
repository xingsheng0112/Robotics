#!/usr/bin/env python
# license removed for brevity

import rospy
import xlrd
import xlwt
from xlutils.copy import copy
import numpy as np
import math


data = xlrd.open_workbook('/home/bbq/robotics/src/hw5/HW5-2.xls')
table = data.sheet_by_index(0)

wb = copy(data)
ws = wb.get_sheet(0)

Qini = np.mat([[1],[0],[0],[0]])
a = np.zeros([100,3])
row=100
col=3
deltaT=0.001
for i in range(row):
	for j in range(col):
		a[i][j]=table.cell(i+1,j).value
s
A = np.mat(a)

for k in range(row):
	q = Qini
	norm = math.sqrt(A[k,0]*A[k,0] + A[k,1]*A[k,0] + A[k,2]*A[k,2])
	A[k,0] = A[k,0]/norm
	A[k,1] = A[k,1]/norm
	A[k,2] = A[k,2]/norm

	Jg = np.mat([[-2*q[2,0]*(-9.8),2*q[3,0]*(-9.8),-2*q[0,0]*(-9.8),2*q[1,0]*(-9.8)],
	   	     [2*q[1,0]*(-9.8),2*q[0,0]*(-9.8),2*q[3,0]*(-9.8),2*q[2,0]*(-9.8)],
	    	     [0,-4*q[1,0]*(-9.8),-4*q[2,0]*(-9.8),0]])
	f = np.mat([[2*(q[1,0]*q[3,0]-q[0,0]*q[2,0])*(-9.8)-A[k,0]],
		    [2*(q[0,0]*q[1,0]+q[2,0]*q[3,0])*(-9.8)-A[k,1]],
		    [2*(0.5-q[1,0]*q[1,0]-q[2,0]*q[2,0])*(-9.8)-A[k,2]]])
	G = Jg.T*f
	norm = math.sqrt(G[0,0]*G[0,0] + G[1,0]*G[1,0] + G[2,0]*G[2,0] + G[3,0]*G[3,0])
	G = G/norm
	q = q - deltaT*G
	norm = math.sqrt(q[0,0]*q[0,0] + q[1,0]*q[1,0] + q[2,0]*q[2,0] + q[3,0]*q[3,0])
	q = q/norm
	for s in range(10000):
		Jg = np.mat([[-2*q[2,0]*(-9.8),2*q[3,0]*(-9.8),-2*q[0,0]*(-9.8),2*q[1,0]*(-9.8)],
	   	  	    [2*q[1,0]*(-9.8),2*q[0,0]*(-9.8),2*q[3,0]*(-9.8),2*q[2,0]*(-9.8)],
	    		    [0,-4*q[1,0]*(-9.8),-4*q[2,0]*(-9.8),0]])
		f = np.mat([[2*(q[1,0]*q[3,0]-q[0,0]*q[2,0])*(-9.8)-A[k,0]],
			    [2*(q[0,0]*q[1,0]+q[2,0]*q[3,0])*(-9.8)-A[k,1]],
			    [2*(0.5-q[1,0]*q[1,0]-q[2,0]*q[2,0])*(-9.8)-A[k,2]]])	
		G = Jg.T*f
		norm = math.sqrt(G[0,0]*G[0,0] + G[1,0]*G[1,0] + G[2,0]*G[2,0] + G[3,0]*G[3,0])
		G = G/norm
		q = q - deltaT*G
		norm = math.sqrt(q[0,0]*q[0,0] + q[1,0]*q[1,0] + q[2,0]*q[2,0] + q[3,0]*q[3,0])
		q = q/norm
	ws.write(k+1,3,q[0,0])
	ws.write(k+1,4,q[1,0])
	ws.write(k+1,5,q[2,0])
	ws.write(k+1,6,q[3,0])
	wb.save('/home/bbq/robotics/src/hw5/HW5-2.xls')
	print(q)
	



