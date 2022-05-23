import sys
n = sys.stdin.readline()

num = list(map(lambda x: int(x), list(sys.stdin.readline().strip())))

print(sum(num))