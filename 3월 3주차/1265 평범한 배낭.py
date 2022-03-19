def dfs(start, weight, cost):
    global result
    if weight > k:
        return
    
    for i in range(start, n):
        if not visited[items[i][0]] and weight <= k:
            cost += items[i][1]
            visited[items[i][0]] = True
            weight += items[i][0]

            if weight <= k:
                result = max(result,cost)
                # print('weight',weight, 'cost',cost, 'result',result)
                dfs(i, weight, cost)
            

            

            visited[items[i][0]] = False
            weight -=  items[i][0]
            cost -= items[i][1]
    


import sys

n, k = map(int, sys.stdin.readline().split())
result = 0
items = []
visited = {}
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    items.append((w,v))
    visited[w] = False

start = 0
weight = 0
dfs(0,0,0)
print(result)

