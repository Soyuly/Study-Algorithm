import sys
num = int(input())

dp = [None] * (num + 1)

if num == 1:
    print(0)
    exit()
elif num == 2:
    print(1)
    exit()
elif num == 3:
    print(1)
    exit()
else:
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

for i in range(4,num + 1):
    if i % 2 ==0 and i % 3 ==0:
        dp[i] = min(dp[i//2] + 1, dp[i-1] + 1, dp[i//3] + 1)

    elif i % 2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)

    elif i % 3 ==0:
        dp[i] = min(dp[i//3] + 1, dp[i-1] + 1)

    else:
        dp[i] = dp[i-1] + 1

print(dp[num])
