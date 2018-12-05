#!/usr/bin/env python
from __future__ import print_function
N = raw_input()
M = raw_input()
if len(N)<len(M):
	N='0'*(len(M)-len(N))+N
length=len(N)
for i in range(len(M)-1):
	if N[-1]=='0':
		N=N[0:-1]
	else:
		break
print (N[0:(length-len(M))+1],end='')
if (length-len(M)+1)!=len(N):
	print ('.'+N[(length-len(M)+1):],end='\n')