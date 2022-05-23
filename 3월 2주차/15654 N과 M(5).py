def dfs(num):
    if num == m:
        print(' '.join(map(str,result)))
        return

    for i in range(n):
        if not visited[i]:
            # 만약 방문 하지 않았으면 방문 체크를 해주고, result에 값 추가
            visited[i] = True
            result.append(data[i])
            dfs(num + 1)

            # 재귀함수로 부터 복귀하면 방문여부를 False로 바꿔주고 리스트의 값을 꺼내준다.
            visited[i] = False
            result.pop()

# 입력받기
import sys
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

result = [] # 답 저장을 위한 리스트
visited = [False] * n # 방문 여부를 확인 할 리스트

data.sort() # 사전순으로 나타내기 위해 정렬
dfs(0)
