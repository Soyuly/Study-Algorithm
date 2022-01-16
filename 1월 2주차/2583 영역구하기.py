import sys
sys.setrecursionlimit(15000)
# 알고리즘
# 이 문제의 관건은 문제에 해당하는 영역을 생성하는게 제일 어려운 것 같음.
# 보통의 문제는 좌측 상단이 (0,0)이지만 이 문제에서는 좌측 하단이 (0,0)이라서 까다로움
# 해당 조건에 맞게 그림만 그리면 빈공간에서 dfs를 통해 개수를 구하면 끝.


def dfs(x, y, cnt):
    visited[x][y] = True

    for i in range(4):
        # 해당 좌표만큼 이동함
        nx = x + dx[i]
        ny = y + dy[i]

        # 해당 좌표가 범위를 넘지 않으면 개수를 추가함
        if (0 <= ny < n) and (0 <= nx < m):
            if space[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                cnt = dfs(nx, ny, cnt)
    return cnt


# m x n 행렬, k개의 개수
m, n, k = map(int, input().split())

# 좌표 이동을 위한 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 개수 저장을 위한 count 리스트
count = []

# 그래프 생성
space = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]


for i in range(k):
    # 좌측xy, 우측xy
    lx, ly, rx, ry = map(int, input().split())
    #   파이썬 상의 행렬                문제의 행렬
    # [(0,0) (0,1) (0,2)]         # [(2,0) (2,1) (2,2)]
    # [(1,0) (1,1) (1,2)]         # [(1,0) (1,1) (1,2)]
    # [(2,0) (2,1) (2,2)]         # [(0,0) (0,1) (0,2)]
    # 자세히 보면 문제의 행렬에서 (행의 개수 -1) 에서 해당 좌표를
    # 빼게 되면똑같게 만들 수 있음
    # 즉 M x N행렬에서 문제의 좌표가(x,y)이면 구하려는 좌표는
    # ((M-1) - x,y)로 공식화할 수 있음.

    for j in range(ly, ry):
        for k in range(lx, rx):
            space[m - 1 - j][k] = 1


# 값이 0(빈공간)이고 방문되지 않았을때만 dfs를 돌린다.
# 그후 해당 범위의 크기를 저장해서 count리스트에 넣는다
for i in range(len(space)):
    for j in range(len(space[0])):
        if space[i][j] == 0 and not visited[i][j]:

            cnt = dfs(i, j, 1)
            count.append(cnt)

# count개수가 곧 빈공간이 개수
print(len(count))

# 정렬하여 출력
for i in sorted(count):
    print(i, end=' ')
