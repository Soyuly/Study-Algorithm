# 너비우선탐색
from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()

        # 해당 범위만큼 좌표 이동시킴.
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 해당 범위에 존재하고 값이 0이면 큐에 추가하고
            # 현재 이동한 길이 추가
            if (0 <= nx < N) and (0 <= ny < M):
                if not space[nx][ny]:
                    for i in space:
                        print(i)
                    print()
                    queue.append((nx, ny))
                    space[nx][ny] = space[x][y] + 1


# 해당 문제는 너비우선탐색을 통해 최적의 경로를 찾는 문제이다.
# 현재 위치에서 8방향으로 탐색을 한 후, 그 위치로 이동하면 현재 탐색한 개수 + 1
# 을 해주어서 최적의 경로를 찾아준다

# N x M 행렬
N, M = map(int, input().split())

# 큐를 선언
queue = deque()
space = []

# 8방향으로 가기 위해 리스트 선언
# (-1,-1) (-1,0) (1,1)
# (0,-1)  (기준) (0,1)
# (1,-1)  (1,0)  (1,1)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 아기상어 입력 받음.
for i in range(N):
    temp = list(map(int, input().split()))
    space.append(temp)

# 그래프 전체 탐색을 해보고, 아기상어가 존재하면
# 큐에 넣어줌
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j] == 1:
            queue.append((i, j))

# bfs 실행
bfs()

# 최대값 출력을 위한 리스트
result = []
for i in space:
    result.append(max(i))

print(max(result) - 1)
