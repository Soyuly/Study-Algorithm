n = int(input())

# 정수 삼각형을 담을 배열
tri = []

# 값 입력 받음
for i in range(n):
    temp = list(map(int,input().split()))
    tri.append(temp)

# 0으로 채워진 dp배열을 만들어줌
dp = [[0] * (i + 1) for i in range(n)]

# 첫번째 최대값은 항상 고정
dp[0][0] = tri[0][0]

# 값이 한개면 맨 위 한개를 출력하고 종료
if n == 1:
    print(tri[0][0])
    exit()

# 3개의 작은 삼각형으로 구성해서, 값을 비교해 나감.
for i in range(len(tri) - 1):
    for j in range(len(tri[i])):
        dp[i+1][j] = max(dp[i+1][j],  dp[i][j] + tri[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + tri[i+1][j+1])


# dp에서 최대한 큰 수 구함
print(max(dp[n-1]))