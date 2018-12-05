#!/usr/bin/env python
total=0
N = input()
price=[]
price = sorted([int(raw_input()) for i in xrange(N)], reverse=True)
for i in range(N):
	if (i+1)%3!=0:
		total= total+price[i]
print total
