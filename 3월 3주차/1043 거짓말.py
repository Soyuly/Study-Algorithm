def dfs(n):
    global flag # 만남여부

    # n이 0이면 지민이의 진실을 알고 있으므로 flag를 True로 바꾸고
    # 리턴
    if n == 0:
        flag = True
        return

    # 방문여부 확인
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            dfs(i)

# 입력 받기
import sys
n, m = map(int,sys.stdin.readline().split())

# 친구수 저장
friend = list(map(int, sys.stdin.readline().split()))

party = [] # 파티정보 저장
graph = [[] for _ in range(n+1)] # 친구 정보를 알 수 있는 그래프 생성
count = 0 # 지민이가 거짓말 할 수 있는 파티의 개수

# 파티 정보를 입력한다.
for i in range(m):
    party.append(list(map(int, sys.stdin.readline().split())))

# 만약 친구수가 1명이라도 있으면, 그 여러명에 대해 0번 노드와 연결 시켜준다.
# 이때 0번 노드는 지민(본인)이다.
if friend[0] != 0:
    for i in range(1,len(friend)):
        graph[friend[i]].append(0)
        graph[0].append(friend[i])

# 만약에 파티 한 사람만 있으면, 진실을 알고 있는 사람과 만나지 않으므로 걱정없다
# 만약에 2명이상이면 진실을 알고 있는 친구가 포함될 수 있기 때문에
# 해당 그래프의 친구 노드에 연관 되어 있는 사람을 추가해준다.
# 이때 자기 자신이 들어갈수도 있지만, visited 처리를 해줘서 상관없다.
for i in range(len(party)):
    if party[i][0] >= 2:
        for j in range(1,len(party[i])):
            graph[party[i][j]] += party[i][1:]

# dfs 탐색을 위한 정렬
for i in graph:
    i.sort()

# 파티의 개수만큼 지민이가 갈 수 있는 파티를 확인한다.
for i in range(len(party)):
    flag = False # 파티 참석여부를 False

    # dfs를 위해 visited 리스트 초기화
    visited = [ False ] * (n + 1)

    # 만약에 파티 참여친구가 1명이면, 그 1명에 대해서만 dfs 돌린다.
    # 그리고 flag = False는 진실을 아는 친구가 없으므로 카운트 1증가
    if party[i][0] == 1:
        dfs(party[i][1])
        if not flag :
            count += 1
    else:
        # 파티참여 친구가 2명이상이면, 그 사람 모두 진실을 알고 있는지 검사한다.
        # 만약에 이 중 1명이라도 알면, 반복문을 빠져나간다.
        for j in range(1,len(party[i])):
            visited = [ False ] * (n + 1)
            dfs(party[i][j])

            # 만약에 진실을 아는 친구가 있으면 반복문을 빠져나감.
            if flag:
                break
        # 없으면 1증가
        if not flag:
            count += 1

print(count)