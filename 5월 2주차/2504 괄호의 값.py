import sys
from collections import deque

# 스택 사용을 위해 덱을 사용
stack = deque()

# 구하려는 String
prob = sys.stdin.readline().strip()

# String 하나씩 for문으로 꺼내옴
for i in prob:
    
    # 만약 괄호가 (이나 [이면 스택에 추가한다
    if i == '(' or i == '[':
        stack.append(i)
        
    # 만약 괄호가 ]인다면 그 다음 [가 나올때까지 계속 빼낸다.
    # 만약 []안에 다른 숫자가 있다면 3을 곱해준다
    elif i == ']':
        try:
            num = [] # 숫자 계산을 위한 리스트
            index = 0 # 인덱스
            while True:
                temp = stack.pop()
                
                # 만약 [를 만났을때, 안에 숫자가 없다면 3을 추가하고
                # 있다면 3을 곱한 값을 추가한다
                if temp == '[':
                    if len(num) == 0:
                        stack.append(3)
                    elif len(num) == 1:
                            stack.append(3 * num[0])
                    break
                
                # 만약 빼낸 숫자가가 [외 다른 값(숫자)이면 num 리스트에 추가
                # 이때 리스트의 숫자가 2개가 된다면, 그것을 합치고 num을 하나로 만들어줌
                else:
                    num.append(temp)
                    index += 1
                    if len(num) == 2:
                        num = [sum(num)]
        except:
            # 예외처리, 오류 뜨면 잘못된 경우이므로 0을 출력하고 종료
            print(0)
            exit()
            
    #)도 마찬가지
    elif i == ')':
        try:
            num = []
            index = 0
            while True:
                temp = stack.pop()
                if temp == '(':
                    if len(num) == 0:
                        if temp == '(':
                            stack.append(2)
                    elif len(num) == 1:
                            stack.append(2 * num[0])
                    break
                else:
                    num.append(temp)
                    index += 1
                    if len(num) == 2:
                        num = [sum(num)]
        except:
            print(0)
            exit()

# 반례가 [[인 경우나 ))인 경우
try:
    print(sum(stack))
except:
    print(0)
            
