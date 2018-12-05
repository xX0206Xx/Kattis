#!/usr/bin/env python
possibilities = ['4']
solution = {}
toprint=[]

for i in range(3):
	ns = []
	for s in possibilities:
		ns.append(s+' * 4')
		ns.append(s+' / 4')
		ns.append(s+' + 4')
		ns.append(s+' - 4')
	possibilities=ns

for s in possibilities:
	a = eval(s)
	solution[a]=s

N = input()
for i in range(N):
	result = input()
	if result in solution:
		toprint.append(solution[result] + ' = ' + str(result))
	else:
		toprint.append('no solution')

print '\n'.join(toprint)
