import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

# 이진탐색을 위해 데이터를 정렬함
data.sort()


m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

# 이진탐색 알고리즘 그대로
for i in find:
    flag = False
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high)//2

        # 찾으면 1을 출력
        if i == data[mid]:
            print(1)
            flag = True
            break

        if i < data[mid]:
            high = mid - 1

        else:
            low = mid + 1

    if not flag:
        print(0)
        


