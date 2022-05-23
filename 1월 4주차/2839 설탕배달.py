import sys


num = int(input())
dp = [sys.maxsize] * (num + 1)

for i in range(1, num + 1):
    if i % 3 == 0:
        dp[i] = int(i / 3)
       

    elif i % 5 == 0:
        dp[i] = int(i / 5)
        

    if i >= 5:

        dp[i] = min(dp[i],dp[i - 3] + 1, dp[i - 5] + 1)

if dp[num] >= sys.maxsize:
    print(-1)
else :
    print(dp[num])
