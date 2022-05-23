import sys
from collections import deque

class Stack:
    # 스택 데이터 초기화
    def __init__(self):
        self.data = []
    
    # 내장함수 len을 정의    
    def __len__(self):
        return len(self.data)
    
    # append 연산을 정의
    def append(self, num):
        self.data.append(num)
    
    # pop 연산을 정의
    def pop(self):
        return self.data.pop()
    
    # top 연산을 정의, 제일 끝 값을 꺼내준다.
    def top(self):
        return self.data[-1]
    
cases = int(sys.stdin.readline().strip())
stack = Stack()

result = '' # 결과를 저장할 변수
for i in range(cases):
    # 한 줄씩 입력을 받는다
    command = sys.stdin.readline().strip()
    
    # 문자을 파싱을 했을때 0번째,1번재 값이 pu이면 push 이므로 command와 num으로 분리
    if command[0:2] == 'pu':
        command, num = command.split()
    

    if command == 'push':
        stack.append(int(num))
        
    elif command == 'pop':
        if stack:
            result += (str(stack.pop()) + '\n')
        else:
            result += '-1 \n'
            
    elif command == 'size':
        result += (str(len(stack)) + '\n')
        
    elif command == 'empty':
        if stack:
            result += '0 \n'
        else:
            result += '1 \n'
            
    elif command == 'top':
        if stack:
            result += (str(stack.top()) + '\n')
        else: 
            result += '-1 \n'
            
print(result)
