
# 큐에 상하좌우 원소들을 넣고 bfs탐색
def bfs():
    queue = deque()
    flag = False
    
    # 덱에 토마토가 있는 위치 전부를 찾아서 넣어준다.
    # 처음에는 1차원적으로 1개만 익어간다고 생각했지만
    # 여러개가 동시에 익을 수 있었음.
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                queue.append((i,j,0))
            
            # 전부 다 익었을때
            if tomato[i][j] == 0:
                flag = True
    
    # 전부 다 익었을때 0 return
    if not flag:
        return 0

    # x,y 좌표와 count를 큐에 넣었음. 여러개가 익을때마다 1초 추가
    while queue:     
        numx, numy, count = queue.popleft()

        # 상하좌우 토마토 전부 큐에 넣는다.
        for i in range(4):
            tx = numx + dx[i]
            ty = numy + dy[i]

            if 0 <= tx < n and 0 <= ty < m:
                if tomato[tx][ty] == 0:
                    queue.append((tx,ty,count + 1))
                    tomato[tx][ty] = 1

    # 안익었는게 있는지 검사, 있으면 -1 리턴
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                return -1

    # 없으면 1 리턴
    return count


# 상하좌우 이동하기 위한 좌표 모음
dx = [-1, 0, 0, 1] 
dy = [0, -1, 1, 0]


import sys
from collections import deque

# 입력
m, n = map(int, sys.stdin.readline().split())

# 리스트 append보다 대입연산이 빠르므로 미리 만들어놨음.
tomato = [[0] for _ in range(n)]

for i in range(n):
    tomato[i] = list(map(int, sys.stdin.readline().split()))

print(bfs())

