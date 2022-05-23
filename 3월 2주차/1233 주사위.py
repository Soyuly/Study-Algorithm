import sys

s1, s2, s3 = map(int, sys.stdin.readline().split())
result = [0] * (s1 + s2 + s3 + 1)


for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            result[i+j+k] += 1


print(result.index(max(result)))
