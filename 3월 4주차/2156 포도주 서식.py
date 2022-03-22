import sys

# 값을 입력받음
n = int(sys.stdin.readline().rstrip())

# 포도주의 양을 담을 배열
g =[0]

#dp배열
dp = [0] * (n+1)

for _ in range(n):
    g.append(int(sys.stdin.readline().rstrip()))

# dp의 첫번째는 항상 포도주의 첫번째 값
dp[1] = g[1]

# 길이가 2이면 dp[1]을 출력하고 종료
if len(g) == 2:
    print(dp[1])
    exit()

# dp[2]는 포도주의 양에서 항상 첫번째와 두번째를 더한 값
dp[2] = g[1] + g[2]

# 포도주 양이 2개이면, dp[2]가 최대값 고정이므로 종료
if len(g) == 3:
    print(dp[2])
    exit()

dp[3] = max(dp[1] + g[3], dp[2], g[2] + g[3])

# f(n) = max(dp[i-2] + g[i], dp[i-3] + g[i-1] + g[i], dp[i-1])
for i in range(4,n+1):
    dp[i] = max(dp[i-2] + g[i], dp[i-3] + g[i-1] + g[i], dp[i-1])

# 최대값 출력
print(dp[-1])