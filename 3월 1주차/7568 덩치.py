N = int(input())

body = []

for _ in range(N):
    body.append(list(map(int,input().split())))




for i in range(N):
    rank = 1
    for j in range(N):
        if i==j :
            continue

        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            rank += 1
        else:
            pass
    
    print(rank, end=' ')

