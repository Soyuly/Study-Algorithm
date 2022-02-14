n = int(input())

tri = []

for i in range(n):
    temp = list(map(int,input().split()))
    tri.append(temp)

dp = [[0] * (i + 1) for i in range(n)]
dp[0][0] = tri[0][0]

if n == 1:
    print(tri[0][0])
    exit()


for i in range(len(tri) - 1):
    for j in range(len(tri[i])):
        dp[i+1][j] = max(dp[i+1][j],  dp[i][j] + tri[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + tri[i+1][j+1])

print(max(dp[n-1]))