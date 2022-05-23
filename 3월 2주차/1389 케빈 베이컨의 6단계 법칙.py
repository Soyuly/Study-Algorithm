def dfs(num,target):
    # 자기자신은 방문 한 것이므로 방문여부 체크해줌
    visited[num] = True

    # 전역변수 선언
    global count
    global minCnt

    # 만약 타겟을 발견했으면 minCnt와 개수를 체크해서 최소값을 넣고 return
    if num == target:
        minCnt = min(minCnt,count)
        return
    
    for i in graph[num]:
        if not visited[i]:
            count += 1
            dfs(i,target)

            # dfs 복귀를 하면 방문여부를 다시 False로 해주고 count를 1빼줌
            visited[i] = False
            count -= 1
            
        
# 재귀함수 깊이 설정
import sys
sys.setrecursionlimit(10000)

# n은 인원수 m은 관계
n, m = map(int, sys.stdin.readline().split())


# 인접리스트 설정
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in graph:
    i.sort()

# 각 노드별 결과를 담을 변수
result = []

# dfs(1,1) 부터 dfs(5,5) 까지 다 돌림
for i in range(1,n+1):
    temp = 0
    for j in range(1, n+1):
        # 자기 자신은 제외이므로 continue
        if i == j:
            continue

        # count는 0으로 초기화
        # count는 타겟까지 가는 개수를 측정
        count = 0

        # minCnt를 최대값으로 초기화
        # minCnt는 여러번 타겟에 가서 그중에 최소값을 구해주는 변수
        minCnt = 1000000000
        visited = [False] * (n+1) # 방문 여부 확인

        dfs(i,j)
        # 각 target별 최소값을 temp에 더해줌.
        temp += minCnt
    result.append(temp)
    
# 최소값 출력
print(result.index(min(result)) + 1)
