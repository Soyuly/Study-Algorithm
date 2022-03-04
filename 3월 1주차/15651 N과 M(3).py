def dfs(num, index):
    if num == m:
        visited[index] = True
        print(' '.join(map(str, graph)))
        return

    for i in range(1, n+1):
        if not visited[i]:
            graph.append(i)
            dfs(num + 1, index)
            graph.pop()
            visited[i] = False


import sys
n, m= map(int, sys.stdin.readline().split())

graph = []
visited = [False] * (n+1)

dfs(0, 0)