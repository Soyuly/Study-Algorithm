# 이문제는 Pypy 인터프리터 + stdin.readline()안쓰면
# 시간 초과 걸리는 끔찍한 문제...

# Alogrithm
# 높이가 최대 256 이므로, 각 높이별 최소 시간을 구한다.
# 현재 땅이 for문의 높이보다 작으면 블럭을 제거한다. => 그 개수를 remove에 더한다
# 현재 땅이 for문의 높이보다 크면 블럭을 추가한다. => 그 개수를 add에 더한다.
# 그렇게 시간을 구하고, 최소 시간을 구함

import sys
input = sys.stdin.readline

# N : 행 M : 열 B : 인벤토리 개수
N, M, B = map(int, input().split())

world = []
for i in range(N):
    world.append(list(map(int, input().split())))

# 최소값과 높이를 정의
minCnt = 1e9
height = 0

# 높이가 256이므로 땅 256만큼 for문 돌림
for i in range(257):
    remove = 0
    add = 0

    for j in range(N):
        for k in range(M):
            if world[j][k] > i:
                remove += (world[j][k] - i)
            else:
                add += (i - world[j][k])

    # 인벤토리에 블럭이 없는데 쌓으면 안되므로 break
    if add > B + remove:
        break

    # 높이가 i일때 시간
    cnt = (remove * 2) + add

    # 최소값을 구함
    if minCnt >= cnt:
        minCnt = cnt
        height = i


print(minCnt, height)
