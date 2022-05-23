import sys

t = int(sys.stdin.readline().strip())

result =''

for _ in range(t):
    r, s = map(str, sys.stdin.readline().split())
    string = list(map(lambda x: x*int(r), s))
    result += ''.join(string) + '\n'

print(result)