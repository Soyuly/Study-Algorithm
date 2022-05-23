# 푸는 방식 똑같음, 단지 6방향과 3차원 배열을 사용할 뿐 완전 똑같음.
def bfs():
    queue = deque()
    flag = False

    for i in range(h):
        for j in range(m):
            for k in range(n):
                if tomato[i][j][k] == 1:
                    queue.append((i,j,k,0))
                
                if tomato[i][j][k] == 0:
                    flag = True
    
    if not flag:
        return 0

    while queue:
        height, x, y, count = queue.popleft()
        z = [0,0,0]
        for i, j, k in [(-1,0,0),(1,0,0),(0,0,-1),(0,0,1),(0,-1,0),(0,1,0)]:
            z[0] = height + i
            z[1] = x + j
            z[2] = y + k
            
            if 0 <= z[0] < h and 0 <= z[1] < m and 0 <= z[2] < n:
           
                if tomato[z[0]][z[1]][z[2]] == 0:
                    queue.append((z[0],z[1],z[2], count + 1))
                    tomato[z[0]][z[1]][z[2]] = 1

    for i in range(h):
        for j in range(m):
            for k in range(n):
                if tomato[i][j][k] == 0:
                    return -1
    return count

import sys
from collections import deque
n, m, h = map(int, sys.stdin.readline().split())

tomato = []

for i in range(h):
    temp = []
    for j in range(m):
        temp.append(list(map(int, sys.stdin.readline().split())))
    tomato.append(temp)


print(bfs())