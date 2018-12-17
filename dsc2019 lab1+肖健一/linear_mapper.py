#! /usr/bin/python
import numpy as np
import sys
mul=[]
for line in sys.stdin:
	line=line.strip().split(',')
	length=len(line)
	line=[float(_) for _ in line]
	y=line[-1]
	x=line[:length-1]
	xy=[i*y for i in x]
	mul_each=[]
	for i in range(0,length-1):
		xj=[x[i]*k for k in x]
		mul_each.append(xj)
	mul_each.append(xy)
	mul.append(mul_each)
mul=np.array(mul)
summul=mul.sum(axis=0)
summul=summul.tolist()
for j in summul:
	print(','.join(str(_) for _ in j))