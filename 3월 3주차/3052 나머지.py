import sys

num = [False] * 42
count = 0
for i in range(10):
    temp = int(sys.stdin.readline().strip())
    num[int(temp % 42)] = True

for i in num:
    if i:
        count += 1

print(count)