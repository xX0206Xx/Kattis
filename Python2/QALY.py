#!/usr/bin/env python
N=input()
qaly=0
for i in range(1,N+1):
	things=raw_input().split()
	qaly=qaly+float(things[0])*float(things[1])
print qaly