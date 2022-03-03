def dfs(n, count):
    if count == 2:
        return
    print(n, end=' ')
    print("count", count)
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            count += 1
            dfs(i, count)



N, M = map(int, input().split())
visited = [False] * (N + 1)
graph = [[]]

for i in range(N):
    graph.append([i for i in range(1, N+1)])

dfs(1,0)