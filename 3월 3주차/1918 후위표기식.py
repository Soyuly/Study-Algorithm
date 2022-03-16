import sys
from collections import deque


# 연산자의 우선순위를 반환해주는 함수
# 괄호 < +,- < *,/
def check(n):
    if n == '*' or n == '/':
        return 3

    elif n == '+' or n == '-':
        return 2

    elif n == '(' or n == ')':
        return 1

    else:
        return 0


# 후위 표기법 변환
def postfix():

    # 스택 사용
    result = ''
    stack = deque()
   
   # 문자열들을 탐색
    for i in notation:
        
        # 만약 문자가 연산자일때
        if i == '*' or i == '/' or i == '+' or i == '-':
            # 연산자 우선순위를 봤을때, 스택에 있는 연산자가 새로 들어오는 연산자보다
            # 우선순위가 크거나 같다면 계속 pop을 해준다
            # 예를 들어 [+,*] 가 있을때 -가 들어온다면 +,*을 다 빼줘야 한다.
            while stack and check(stack[-1]) >= check(i):
                    result += stack.pop()

            # 그리고 연산자를 다시 넣어준다
            stack.append(i)

        # 오른쪽 괄호일때 왼쪽 괄호를 만날때까지
        #전부 pop
        elif i == ')':
            temp = stack.pop()
            while temp != '(':
                result += temp
                temp = stack.pop()

        # 왼쪽 괄호일떄
        elif i == '(':
            stack.append(i)

        # 문자일때
        else:
            result += i

    while stack:
        result += stack.pop()
    return result

    

notation = list(sys.stdin.readline().strip())

print(postfix())