# 케이스 수를 구함
case = int(input())

# 구하려는 n 번째 숫자
num = []
for i in range(case):
    num.append(int(input()))

# 1,2,3번째는 default로 추가
dp = []
dp.append(0)
for i in range(3):
    dp.append(1)

# f(n) = f(n-2) + f(n-3)
for i in range(4, max(num) + 1):
    dp.append(dp[i-3] + dp[i-2])

for i in num:
    print(dp[i])
