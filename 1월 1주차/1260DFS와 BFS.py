# 깊이우선 탐색
from collections import deque

def dfs(n):
    # python에서는 default가 end = '\n'로 되어 있음. 이는 자동으로 줄바꿈을 한다는 의미
    # 따라서 한줄에 출력하기 위해서는 end =''로 바꿔줘야함.
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

# 너비우선 탐색
def bfs(n):
    # 너비우선탐색은 큐를 통해 이뤄지므로 덱을 사용
    queue = deque()
    queue.append(n)
    visited[n] = True

    while queue:
        # 덱에서 하나 꺼내기
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


# DFS와 BFS
# 파이썬에서는 공백으로 입력 받으려면 Map함수 사용
# split()은 공백단위로 각 숫자를 나눈다.
n, m, start = map(int, input().split())

# 해당 개수만큼 2차원 배열을 만든다.
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    v1, v2 = map(int, input().split())
    # 리스트에 값 추가
    graph[v1].append(v2)
    graph[v2].append(v1)

# print(graph), 생성된 리스트
# [[], [2, 3], [5, 1], [4, 1], [5, 3], [4, 2]]
# [5,1] 경우에 for문을 돌리면 1의 경우는 읽지 않으므로
# 순서대로 for문을 돌리기 위해 정렬을 해야함.
for i in range(n+1):
    graph[i].sort()

dfs(start)
print()
visited = [False] * (n+1)
bfs(start)
