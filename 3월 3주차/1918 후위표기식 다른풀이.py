from unittest import result


def postfix():
    result = ''
    stack = deque()

    for i in notation:
        if i.isalpha():
            result += i

        if i == '(':
            stack.append(i)

        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack [-1] == '/'):
                result += stack.pop()
            stack.append(i)

        elif i == "+" or i == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        
        elif i == ')':
            while stack and stack[-1] == '(':
                result += stack.pop()

    while stack:
        result += stack.pop()
    return result

import sys
from collections import deque
notation = list(sys.stdin.readline().strip())

print(postfix())