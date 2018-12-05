#!/usr/bin/env python
soln = []
i = 1
while 1:
    inp = raw_input()
    if inp == 'END':
        break
    else:
        inp = inp.split('*')[1:-1]
    if inp == []:
        soln.append(str(i)+' EVEN')
        i = i+1
    else:
        num = len(inp[0])
        isEven = True
        for x in inp:
            if len(x) != num:
                isEven = False
                soln.append(str(i)+' NOT EVEN')
                i = i + 1
                break
        if isEven:
            soln.append(str(i)+' EVEN')
            i=i+1
print '\n'.join(soln)
