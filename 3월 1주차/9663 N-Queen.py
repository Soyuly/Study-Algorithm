count = 0
def check(q):
    for i in range(q):
        if row[q] == row[i] or abs(row[q] - row[i]) == q - i:
            return False
    return True

def dfs(num):
    global count
    if num == n:
        count += 1
        return
    
    for i in range(n):
        row[num] = i
        if check(num):
            dfs(num + 1)

import sys

n = int(sys.stdin.readline())

row = [0] * n
dfs(0)
print(count)

