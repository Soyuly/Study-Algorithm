import sys

num = int(sys.stdin.readline().rstrip())

dp = [[1] * 10] * num

for i in range(1, num):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:]) % 10007

print(sum(dp[-1]) % 10007)