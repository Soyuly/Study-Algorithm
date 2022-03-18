# 이문제를 많이 틀렸는데, heqpq에 넣을때 (정점, 코스트) 이렇게 넣었는데,
# 코스트, 정점 이렇게 넣어줘야 우선순위면에서 시간복잡도가 유리

import sys
import heapq

INF = int(1e9)

vertex, edge = map(int,sys.stdin.readline().split())
first = int(sys.stdin.readline().strip())

graph = [[] for _ in range(vertex + 1)]

for _ in range(edge):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end,cost))

def dajikstra(start):
    distance = [INF] * (vertex + 1)
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        print(q)
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    
    return distance

result = dajikstra(first)
s = ''
for i in range(1, vertex + 1):
    if result[i] >= INF:
        s += 'INF' + '\n'
    else:
       s += str(result[i]) + '\n'

print(s)