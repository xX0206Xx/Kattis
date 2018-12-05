#!/usr/bin/env python
import math
N=input()
digit = []
for i in range(0,N):
	digit.append(str(math.factorial(input()))[-1])
print "\n".join(digit)