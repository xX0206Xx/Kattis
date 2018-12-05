#!/usr/bin/env python
probs = {}
right = []
score = 0
while(1):
	now = raw_input().split()
	if now == ['-1']:
		break
	if str(now[1]) not in probs:
		probs[str(now[1])]=[[int(now[0]),now[2]]]
	else:
		probs[str(now[1])].append([int(now[0]),now[2]])
	if now[2]=='right':
		right.append(now[1])

for char in right:
	for i in range(len(probs[char])):
		if probs[char][i][1]=='wrong':
			score = score + 20
		if probs[char][i][1]=='right':
			score = score + probs[char][i][0]
			break

print len(right), score