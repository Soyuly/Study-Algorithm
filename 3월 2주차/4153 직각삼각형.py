import sys

result = []
while True:
    tri = list(map(int, sys.stdin.readline().split()))

    if tri[0] == tri[1] == tri[2] == 0:
        break
    
    s3 = max(tri)
    tri.remove(s3)


    if (tri[0] ** 2 + tri[1] **2) == s3 ** 2:
        result.append("right")
    else:
        result.append('wrong')

print('\n'.join(map(str,result)))