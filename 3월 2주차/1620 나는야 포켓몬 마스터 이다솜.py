import sys

n, m = map(int, sys.stdin.readline().split())
pocketmon = {}

for i in range(n):
    pocketmon[i+1] = sys.stdin.readline().strip()

number = dict(map(reversed, pocketmon.items()))
result = ''
for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        result += (pocketmon[int(q)] + '\n')
    else:
        result += (str(number[q]) + '\n')

print(result)