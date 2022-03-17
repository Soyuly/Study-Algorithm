from audioop import mul


def multiply(A, B):
    result = [[0 for _ in range(n)]  for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= 1000

    return result

def pow(A,n):
    if n == 1:
        return A

    if n % 2 == 0:
        temp = pow(A, n//2)
        return multiply(temp,temp)
    else:
        temp = pow(A, n-1)
        return multiply(temp,A)

import sys

n, b = map(int, sys.stdin.readline().split())

A = [0] * n

for i in range(n):
    A[i] = list(map(int, sys.stdin.readline().split()))


result = pow(A,b)

for i in result:
    for j in i:
        print(j % 1000, end=' ')
    
    print()
