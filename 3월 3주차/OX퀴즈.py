import sys

t = int(sys.stdin.readline().strip())

s = ''
for i in range(t):
    score = 1
    result = 0
    quiz = list(sys.stdin.readline().strip())

    for i in quiz:
        if i == 'O':
            result += score
            score += 1
        elif i == 'X':
            score = 1
        
    s += str(result) + '\n'

print(s)