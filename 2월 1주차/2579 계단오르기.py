cases = int(input())

stairs = [0]
dp = [0] * (cases + 1)
for i in range(cases):
    stairs.append(int(input()))


for i in range(1, cases + 1):
    if i == 1:
        dp[i] = stairs[1]
   
    elif i == 2:
        dp[i] = max(stairs[1], stairs[2], stairs[1] + stairs[2])

    elif i == 3:
        dp[i] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    
    else:
        dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])


print(dp[cases])
