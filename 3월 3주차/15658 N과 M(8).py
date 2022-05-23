def dfs(depth,visited):
    if depth == m:
        print(' '.join(map(str,result)))
        return

    for i in range(n):
        if i >= visited:
            result.append(nums[i])
            dfs(depth + 1,i)
            result.pop()



import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
result = []
dfs(0,0)