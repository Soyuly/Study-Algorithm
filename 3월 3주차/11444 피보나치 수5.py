def multiply(a,b):
    result =  [[0,0],[0,0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (a[i][k] * b[k][j] %1000000007)

    return result

def pow(a,n):
    if n == 1:
        return a
    if n % 2 == 0:
        temp = pow(a,n//2)
        return multiply(temp,temp)
    
    else:
        temp = pow(a, n - 1)
        return multiply(temp,a)


import sys

num = int(sys.stdin.readline())

fib = [[1,1],[1,0]]

result = pow(fib,num)

print(result[0][1] %1000000007)