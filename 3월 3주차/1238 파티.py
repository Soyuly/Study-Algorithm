import heapq
import sys
# 거리의 최대값을 위한 INF
INF = int(1e9)

# 사람 수, 도로 수, 마을명
n, m, x = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

# 그래프에 (도착지점,비용)  추가해줌.
for i in range(m):
    start, end, cost = map(int,sys.stdin.readline().split())
    graph[start].append((end,cost))

# 다익스트라 알고리즘
def dijkstra(start, target):
    # 거리를 무한대로 초기화
    distance = [INF] * (n+1)

    # 힙을 위한 리스트
    queue = []

    # (비용, 도착지점)을 힙에 넣어줌.
    # 이때 시작점이므로 비용 0을 넣어줌
    heapq.heappush(queue, (0,start))
    distance[start] = 0

    while queue:
        # 비용과 현재위치를 꺼냄
        dist, now = heapq.heappop(queue)

        # 중복 방문을 피하기 위한 변수
        if distance[now] < dist:
            continue
        
        # 정점과 연결 되어 있는 모든 노드를 탐색한다.
        for i in graph[now]:
            # 앞서 꺼냈던 비용과 해당 노드까지의 비용을 계산한다.
            cost = dist + i[1]

            # 비용의 최소값을 구하고, 최소이면 해당 정점을 넣는다.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))
    return distance[target]


result = 0
for i in range(1,n + 1):
    
    if i == x:
        continue
    result = max(dijkstra(i,x) + dijkstra(x,i), result)


print(result)


