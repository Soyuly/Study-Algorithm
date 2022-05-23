import sys

a, b = map(str,sys.stdin.readline().split())
a = list(a)
a.reverse()

b = list(b)
b.reverse()
print(max(int(''.join(a)),int(''.join(b))))
