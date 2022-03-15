import sys

home = int(sys.stdin.readline().strip())
rgb = [[] for _ in range(home)]

for i in range(home):
    rgb[i] = list(map(int,sys.stdin.readline().split()))

# 2차원 dp 배열을 만들어서, 위에 2개를 더한 것중 최소값을 dp에 넣는다.
# 그리고 값을 쌓아가면서 최소값을 찾는다.
dp = [[10000000,10000000,10000000] for _  in range(home)] 
dp[0] = rgb[0]

for i in range(1,home):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + rgb[i][2]

print(min(dp[home-1]))