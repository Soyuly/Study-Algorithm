import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())
array = list(str(a*b*c))

result = ''
for i in range(10):
    result += str(array.count(str(i))) + '\n'

print(result.strip())