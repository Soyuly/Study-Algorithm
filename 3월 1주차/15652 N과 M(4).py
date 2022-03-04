def dfs(num, start):
    if num == m:
        print(' '.join(map(str, graph)))
        return

    for i in range(start, n+1):
        graph.append(i)
        dfs(num + 1, i)
        graph.pop()

import sys

n, m = map(int, sys.stdin.readline().split())

graph = []

dfs(0,1)
