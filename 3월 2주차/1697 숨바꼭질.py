def bfs(n):
    queue = deque() # 덱 선언
    queue.append((0,n)) # 덱에 (개수, 현재 숫자)를 튜플 형식으로 같이 추가 해준다.
    visited[n] = True # 일단 처음 방문했으니 방문 체크

    while True:
        result, v = queue.popleft() # 개수와 정점을 꺼낸다
        
        # 만약에 찾으려는 숫자를 발견하면 종료
        if v-1 == k or v + 1 == k or v * 2 ==k:
            return result + 1

        # 헤당 범위만큼 큐에 넣는다.
        for i in [ v - 1, v + 1, v * 2 ]:
            if 0 <= i <= 100000 and not visited[i]:
                queue.append((result + 1, i))
                visited[i] = True

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [False] * 100001

# 만약에 수빈이와 동생이 같으면 이동할 필요 없으므로 0을 출력하고 종료
if n == k:
    print(0)
    exit()

# bfs 실행
print(bfs(n))

