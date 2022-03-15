import sys
num = [0] * 9
for i in range(9):
    num[i] = int(sys.stdin.readline().strip())

result = str(max(num)) + '\n' + str(num.index(max(num)) + 1)

print(result)