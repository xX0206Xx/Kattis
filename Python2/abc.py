#!/usr/bin/env python
digits=sorted(list(map(int,raw_input().split())))
for char in raw_input():
	print digits[ord(char)-65],
print
