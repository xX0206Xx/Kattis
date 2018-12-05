#!/usr/bin/env python
import math
inp = raw_input()
A = float(inp.split(' ')[0])
N = float(inp.split(' ')[1])
if A>(N**2/(4*math.pi)):
	print 'Need more materials!'
else:
	print 'Diablo is happy!'
