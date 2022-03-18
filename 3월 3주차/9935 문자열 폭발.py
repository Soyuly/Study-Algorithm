def check():
    stk = []

    for i in word:
        stk.append(i)
        if stk[-len(boom):] == boom:
            for _ in range(len(boom)):
                stk.pop()
    return stk

import sys
word = sys.stdin.readline().strip()
boom = list(sys.stdin.readline().strip())

result = check()

if not result:
    print('FRULA')
else:
    print(''.join(result))