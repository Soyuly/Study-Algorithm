# Algorithm
# 처음에는 맨 좌측상단의 색깔을 기준으로, 바꿔야 되는 줄 알아서 이것 때문에 완전 삽질한 문제
# 문제의 핵심은 8x8 판을 임의로 선택해서, 검은색과 하얀색을 기준으로 각각 칠했을때 뭐가 더 유리한지
# 1차적으로 구하고 이러한 값들을 최소값을 구하는 문제였음.

# 모든 체스판을 차례대로 탐색하고, 이때 8x8의 판에서 4가지의 케이스가 있는데
# (짝수, 짝수) 좌표이면 왼측상단의 좌표랑 같아야 함, 만약에 틀리면 색을 다시 칠해야하므로 count + 1
# (짝수, 홀수) 좌표이면  왼측상단의 좌표랑 달라야 함, 만약에 틀리면 색을 다시 칠해야하므로 count + 1
# (홀수, 짝수) 좌표이면  왼측상단의 좌표랑 달라야 함, 만약에 틀리면 색을 다시 칠해야하므로 count + 1
# (홀수, 홀수) 좌표이면  왼측상단의 좌표랑 같아야 함, 만약에 틀리면 색을 다시 칠해야하므로 count + 1

# N X M 행렬을 8X8공간만큼 순회하고, 그 공간안에서 for문을 돌려서 해당 조건이 맞는지 검사하고 count해줌
# 왼측 상단이 블랙일때와 화이트일때 각각 구하고, 여기서 최소값을 minimum리스트에 추가함.
# 그래서 체스판 전체를 순회했을때 나온 개수들의 최소값을 구한다.

# N X M 행렬
n, m = map(int, input().split())

# 체스판과 최소값을 구하기 위한 minimum
chess = []
minimum = []

# 값 추가
for i in range(n):
    wb = input()
    chess.append(list(wb))

# c,r은 체스판 전체를 순회하기 위한 변수, r을 -1한 이유는 while문을 시작하자마자 r에 1을 더하는데
# 처음은 (0,0)을 맞춰주기 위함.
c = 0
r = -1

while True:
    # 좌측상단이 검은색 or 흰색일때의 개수
    cnt_b = 0
    cnt_w = 0

    # 체스판 전체를 순회하는데, 만약 8을 더했을때 열의 길이를
    # 안넘으면 r에 1을 더해주고 순회하며, 넘었을 경우 다음 줄로
    # 넘어가야하기 때문에 c에 1을 더해줌. 만약 c도 넘으면 다 순회
    # 한것이므로 종료
    if r + 8 < m:
        r += 1
    else:
        if c + 8 < n:
            r = 0
            c += 1
        else:
            break

    for i in range(c, 8 + c):
        for j in range(r, 8 + r):

            # (짝수, 짝수) 좌표 일때
            if (i-c) % 2 == 0 and (j-r) % 2 == 0:
                if chess[i][j] != 'B':
                    cnt_b += 1
                if chess[i][j] != 'W':
                    cnt_w += 1

            # (짝수, 홀수) 좌표 일때
            elif (i-c) % 2 == 0 and (j-r) % 2 == 1:
                if chess[i][j] == 'B':
                    cnt_b += 1
                if chess[i][j] == 'W':
                    cnt_w += 1

            # (홀수, 짝수) 좌표 일때
            elif (i-c) % 2 == 1 and (j-r) % 2 == 0:
                if chess[i][j] == 'B':
                    cnt_b += 1
                if chess[i][j] == 'W':
                    cnt_w += 1

            # (홀수, 홀수) 좌표 일때
            elif (i-c) % 2 == 1 and (j-r) % 2 == 1:
                if chess[i][j] != 'B':
                    cnt_b += 1
                if chess[i][j] != 'W':
                    cnt_w += 1

    minimum.append(min(cnt_w, cnt_b))

# print(minimum)
print(min(minimum))
