#dfs. 함수
def dfs(x,y):
    # 방문여부 표시
    graph[x][y] = 0

    #8개의 방향으로 전부 이동해봄
    for k in range(8):
        tx = x
        ty = y

        # 해당 범위에 맞으면 이동해서 섬이 있는지 체크
        if 0 <= x + dx[k] < h and 0 <= y + dy[k] < w:
            tx += dx[k]
            ty += dy[k]


            if graph[tx][ty] == 1:
                graph[tx][ty] = 0
                dfs(tx,ty)
                    
                    


import sys

sys.setrecursionlimit(10000) # 재귀함수 깊이 설정

# 상하좌우 대각선 방향까지 걸어갈 수 있는거리
dx = [-1,  0,  1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1,  0, 0,  1, 1, 1]

printCount = '' # 개수를 출력하기 위한 문자열

while True:
    count = 0 # 한 대륙당 섬의 개수 
    w, h = map(int, sys.stdin.readline().split())

    # (0,0)은 종료
    if w == 0 and h == 0:
        break

    graph = [0] * h 

    for i in range(h):
        # graph.append(list(map(int, sys.stdin.readline().split())))
        graph[i] = list(map(int, sys.stdin.readline().split()))

    # 2중 for문을 돌려서 만약 그래프가 1일때 섬이 있으므로
    # dfs함수를 실행한다 만약에 돌아오면 섬을 다 돈것이므로 
    # count를 1증가한다
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                count += 1
    
    
    # 개수 저장
    printCount += (str(count) + '\n')


print(printCount)