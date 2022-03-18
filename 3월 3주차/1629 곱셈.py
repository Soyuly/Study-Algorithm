import sys

a,b,c = map(int,sys.stdin.readline().split())

def pow(target, num):
   
    if num == 1:
        return target % c

    if num % 2 == 0:
        temp = pow(target, num // 2)
        return temp * temp % c
    else:
        temp = pow(target, num -1)
        return temp * target %c

print(pow(a,b))
