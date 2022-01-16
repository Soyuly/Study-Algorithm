# 깊이 우선 탐색
def dfs(x, y):
    # 일단 이 함수가 호출되면, 해당 배추를 방문한것으로
    # visited를 True로 바꾸어준다.
    temp_x = 0  # xy좌표를 1씩 증감하기 위한 변수
    temp_y = 0
    visited[x][y] = True

    # xy증감 좌표가 총 4개이니 4번 반복문을 돌림.
    for i in range(4):
        # 각각의 변수에 xy 증감을 시작한다.
        temp_x = x + loc_x[i]
        temp_y = y + loc_y[i]

        # 이 좌표가 해당 배추 밭을 초과하거나 마이너스이면 오류가 발생하므로
        # 이를 방지해줌.
        cabbage_range = temp_y >= 0 and temp_y < len(cabbage[0]) and temp_x >= 0 and temp_x < len(cabbage)
        
        if cabbage_range:
            # 만약 배추가 있고, 방문하지 않으면 dfs함수 실행
            if cabbage[temp_x][temp_y] == 1 and not visited[temp_x][temp_y]:
                # print("dfs재귀실행", temp_x, temp_y)
                dfs(temp_x, temp_y)


# 파이썬에서는 최대 재귀함수 호출 개수가 1000개로 제한.
# 이를 풀어주기 위해서 해당 코드를 작성 하였음.
# 1000개로 제한하면 백준 런타임 에러 발생
import sys

limit_number = 15000
sys.setrecursionlimit(limit_number)

t = int(input())  # 테스트 케이스 수
count = []  # 개수를 저장하기 위한 리스트

# 배추가 연결되어있으면 하나로 취급하므로
# x, y각각 1씩 증감하여 지렁이 하나로 가능한지 체크
# 하는 리스트
loc_x = [-1, 1, 0, 0]
loc_y = [0, 0, -1, 1]

# 테스트케이스 수 만큼 반복문을 돌림.
for i in range(t):
    cnt = 0  # 개수를 세줌

    # m은 가로(열), n은 세로(행), k는 배추의 개수(정점)
    m, n, k = map(int, input().split())

    # 해당 m n만큼 0으로 가득 채워져 있는
    # 리스트를 만들어줌
    cabbage = [[0]*m for i in range(n)]

    # 방문횟수를 체크하기 위한 변수
    visited = [[False]*m for i in range(n)]

    # 배추의 개수만큼 값을 입력 받는다.
    for i in range(k):
        v1, v2 = map(int, input().split())
        cabbage[v2][v1] = 1

    # 편의를 위해서 해당 배추밭을 보여줌.
    for i in range(n):
        print(cabbage[i])

    # 인접행렬에서 모든 배추를 알기 위해
    # 이중for문으로 하나씩 요소를 순회함.
    for i in range(n):
        for j in range(m):
            # 배추가 존재하고, 지렁이가 없다면 dfs함수 호출 후
            # 카운트증가
            if cabbage[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                # 이 함수를 호출한건 한 영역을 이미 다 방문했고,
                # 다른 영역을 가니까 지렁이가 추가로 필요함.
                # 그래서 cnt를 1증가.
                cnt += 1
                # print("cnt실행", i, j)
    
    count.append(cnt)

for i in count:
    print(i)
