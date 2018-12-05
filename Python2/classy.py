#!/usr/bin/env python
import operator
N = input()
for i in range(N):
	ppl = {}
	numPpl = input()
	maxlen = 0
	for j in range(numPpl):
		inp = raw_input()
		classes = inp.split(' ')[1]
		ppl[inp.split(':')[0]]= classes.split('-')
		if len(ppl[inp.split(':')[0]]) > maxlen: maxlen =  len(ppl[inp.split(':')[0]])
	for key, value in ppl.iteritems():
		for k in range(maxlen-len(value)):
			value.insert(0,'middle')
		ppl[key]=value[::-1]
	fruit = sorted(ppl.items(), key=operator.itemgetter(0))
	sorted_d = sorted(fruit, key=operator.itemgetter(1), reverse=True)
	final = [x[0] for x in sorted_d]
	print('\n'.join(map(str, final)))
	print '==============================' 