import sys
n = int(sys.stdin.readline().strip())

avg = list(map(int, sys.stdin.readline().split()))

m= max(avg)
avg = list(map(lambda x: x / m * 100, avg))

print(sum(avg)/ n)