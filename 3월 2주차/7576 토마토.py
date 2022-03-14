def bfs(x,y):
    cnt = 0
    
    queue = deque()
    queue.append((x,y))
    tomato[x][y] = 1

    while queue:
        tcnt = 0
        numx, numy = queue.popleft()

        for i in range(4):
            tx = numx + dx[i]
            ty = numy + dy[i]

            if 0 <= tx < n and 0 <= ty < m:
                if tomato[tx][ty] == 0:
                    queue.append((tx,ty))
                    tomato[tx][ty] = 1
                    tcnt +=1
        cnt = cnt + 1 
        for i in tomato:
            print(i)
        print(queue)
        print(tcnt, cnt)
        print()


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())

tomato = [[0] for _ in range(n)]

for i in range(n):
    tomato[i] = list(map(int, sys.stdin.readline().split()))

bfs(3,5)


