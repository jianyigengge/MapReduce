#! /usr/bin/python
import numpy as np
import sys
mul=[]
for line in sys.stdin:
	l=line.strip().split(',')
	l=[float(_) for _ in l]
	mul.append(l)
mul=np.array(mul)
mullist=mul.tolist()
length=len(mullist)
xtx=mullist[:length-1]
xty=mullist[-1]
xtx=np.mat(xtx)
inv=xtx.I
xty=np.mat(xty).T
beta=inv*xty
beta=beta.T.tolist()
for j in beta:
	print(','.join(str(_) for _ in j))
