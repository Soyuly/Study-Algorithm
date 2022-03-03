# 너비우선탐색 구현
from collections import deque

def bfs():
    cnt = 0
    queue = deque()
    queue.append(1)
    visited[1] = True
    while queue:
        v = queue.popleft()
        for i in computer[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1
    return cnt

n = int(input())  # 정점의 개수
m = int(input())  # 간선의 수

computer = [[] for i in range(n+1)]  # 그래프 배열 초기화
print(computer)
visited = [False] * (n+1)  # 방문 횟수를 찾는 visited 배열

for i in range(m):
    v1, v2 = map(int, input().split())
    computer[v1].append(v2)
    computer[v2].append(v1)

for i in range(n+1):
    computer[i].sort()

print(bfs())
