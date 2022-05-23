import sys

n, m = map(int,sys.stdin.readline().split())

if m > n//2:
    m = n - m


dp = [1] * ( m + 1)

for i in range(1,m + 1):
    dp[i] = dp[i-1] * i



result = 1
for i in range(n, n - m , -1):
    result = result * i

print(result // dp[-1])