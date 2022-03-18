import sys
from collections import deque
def postfix():
    result = ''
    stack = deque()

    for i in notation:
        if i == '(' or i ==')':
            continue

        
        print(stack)
        if i == '*' or i == '/' or i == '+' or i == '-':
            result += stack.popleft() 
            print('result', result)
            stack.append(i) 
        else:
            stack.append(i)
    
    return result


notation = list(sys.stdin.readline().strip())

print(postfix())