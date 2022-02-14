# Algorithm
# 도저히 점화식이 안떠올라서 솔루션 참고해서 이해했습니다.
# 마지막 전 계단을 밟았을때 or 마지막 계단을 밟았을때 나눠서 계산
num = int(input())

stairs = []
dp = []
for i in range(num):
    stairs.append(int(input()))

print(stairs)

for i in range(num):
    # 무조건 첫번째 계단만 선택
    if i == 0:
        dp.append(stairs[i])
        continue

    # 첫번째 계단 or 두번째 계단부터 올라갈 것인지에 대한 최대값
    if i == 1:
        dp.append(max(stairs[0], stairs[1]))
        continue

    # 첫번째-세번째 계단 or 두번째-세번째 계단
    if i == 2:
        dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
        continue

    dp.append(max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i]))

print(dp)
