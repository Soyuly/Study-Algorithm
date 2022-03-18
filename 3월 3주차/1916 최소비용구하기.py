import sys
import heapq

INF = 1e9

city = int(sys.stdin.readline().strip())
bus = int(sys.stdin.readline().strip())

graph = [[] for _ in range(city + 1)]

for _ in range(bus):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end,cost))

now, target = map(int, sys.stdin.readline().split())

def dajikstra(start,target):
    distance = [INF] * (city + 1)
    q = []

    distance[start] = 1
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance[target]

print(dajikstra(now,target))