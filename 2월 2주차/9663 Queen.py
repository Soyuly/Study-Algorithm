n = int(input())

chess = [[False] * n for _ in range(n)]

chess[0][0] = True
# for i in range(n):
#     for j in range(n):

for k in range(n):
    chess[0][k] = True
    chess[k][0] = True
            
    try:
        chess[0+k][0+k] = True
    except:
        pass
            
    try:
        chess[0 - k][0 + k] = True
    except:
        pass
            
    try:
        chess[0+k][0 - k] = True
    except:
        pass
                
    try:
        chess[0 - k][0 - k] = True
    except:
        pass
                
for i in chess:
    print(i)