# 기존의 N과 M에서 조금 꼬아서 낸 문제
# 다른 사람들은, for문이 시작지점을 start로 두어서
# 재귀함수를 실행시킬대마다 start + 1을 해서 무조건 자기보다 크게
# 하였지만, 나는 만약에 그래프를 정렬했을때 똑같다면 오름차순으로 되어 있는 것이므로
# 나타내고, 아닐경우에는 오름차순이 아니므로 출력하지 않는다.

def dfs(num):
    if num == M:
        if sorted(graph) == graph:
            print(' '.join(map(str, graph)))
        return

    for i in range(1, N+1):
        if not visited[i]:
      
                visited[i] = True
                graph.append(i)
                dfs(num + 1)
                visited[i] = False
                graph.pop()

import sys

N, M = map(int, sys.stdin.readline().split())

graph = []
visited = [False] * (N + 1)

dfs(0)