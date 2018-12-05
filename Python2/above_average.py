#!/usr/bin/env python
N,rate=input(),[]
for i in range(0,N):
	rate.append(0)
	numbers = list(map(int,raw_input().split()))
	Sum = sum(numbers[1:])
	for k in range (1,numbers[0]+1):
		if numbers[0]*numbers[k]>Sum:
			rate[i]=rate[i]+1
	rate[i]='{:.3%}'.format(float(rate[i])/numbers[0])
print '\n'.join(rate)