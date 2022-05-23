import sys
import heapq

INF = int(1e9)
n, m, r = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]
for i in range(r):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
    return distance
    
items = 0

for i in range(1, n+1):
    temp = 0
    result = dijkstra(i)
    for j in range(1, n+1):
        if result[j] <= m:
            temp += item[j-1]
        
    items = max(items,temp)

print(items)

