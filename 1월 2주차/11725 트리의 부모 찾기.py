from collections import deque
import sys

sys.setrecursionlimit(10000000)

# 알고리즘
# 직접 트리를 그려서 DFS 수행과정을 체크해보면, DFS 재귀함수를 호출 할 당시
# 노드의 값이 부모임을 알 수 있음.


def dfs(n):
    # 해당 노드를 방문처리
    visited[n] = True

    # dfs를 실행
    for j in graph[n]:
        if not visited[j]:
            result[j] = n
            dfs(j)


# 개수를 입력 받음
count = int(input())

# 빈 그래프를 생성
graph = [[] for _ in range(count + 1)]

# 결과값을 출력하기 위한 리스트
result = [0] * (count + 1)

# 방문여부 확인
visited = [False] * (count + 1)

# 값을 입력받고, 인접행렬을 만든다
for i in range(count - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# DFS()를 수행하기 위해 인접행렬을 정렬한다.
for i in range(count+1):
    graph[i].sort()

# 루트 노드 1부터 DFS를 실행한다.
dfs(1)


for i in result:
    if i != 0:
        print(i)
