import sys

n, m = map(int, sys.stdin.readline().split())

no_listen = {}
result = []

for _ in range(n):
    no_listen[sys.stdin.readline().strip()] = True

for _ in range(m):
    no_see = sys.stdin.readline().strip()
    try:
        if no_listen[no_see]:
            result.append(no_see)
    except:
        pass

result.sort()

print(len(result))
print('\n'.join(map(str,result)))