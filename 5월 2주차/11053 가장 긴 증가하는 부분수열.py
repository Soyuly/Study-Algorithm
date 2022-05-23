def binarySearch(target):
    low = 0
    high = len(blist)
    
    while low < high:
        mid = (low + high) // 2
        
        if  target <= blist[mid]:
            high = mid
    
        else:
            low = mid + 1
    
    if low - 1 < 0:
        return -1
    
    else:
        return low - 1

import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
blist = sorted(a)

dp = [0] * n
result = []

dp[0] = 1

for i in range(1,n):
    index= binarySearch(a[i])
    print(i, 'index', index, blist[index])
    
    if index < 0:
        dp[i] = dp[a.index(a[i])]
    else : 
        dp[i] = dp[a.index(blist[index])] + 1


print(max(dp))