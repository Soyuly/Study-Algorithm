# 브루트포스로 해결하려다가 실패,,,
# height = max(tree)
# for i in range(max(tree), 0, -1):
#     result = list(map(lambda x : x - i if x - i >= 0 else 0, tree))

#     if sum(result) == m:
#         print(i)
#         exit()
#     elif sum(result) > m:
#         print(i)
#         exit()

import sys

# 값을 입력 받음
n, target = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

# 이진탐색을 위해 데이터 정렬함
tree.sort()

# 파이썬에서 시간초과 안뜨게 하기 위해서 더하는것도 이진탐색으로 구현함.
# mid보다 큰 index를 이진 탐색으로 구해서, 해당 부분만 더하기를 해서
# 값을 return 함
def sum(target):
    result = 0
    low = 0
    high = len(tree)
    
    # mid보다 최대값을 구하는 
    # 이진탐색 알고리즘
    while low < high:
        midd = (low + high) // 2

        if tree[midd] <= target:
            low = midd + 1

        else:
            high = midd

    # 해당 index를 기반으로 합을 구함
    for i in range(low, len(tree)):
        result += (tree[i] - target)

    return result

# 이진탐색 시작
low = 0
high =  tree[n-1]
height = 0

# 톱의 길이로 자른 나무의 길이가 목표치보다 많으면 
# 톱의 길이를 올려주고 값을 찾음.
# 아니면 값을 내려주고 값을 찾음
while low <= high:
    cut = 0
    mid = (low + high) // 2
    
    cut = sum(mid)
    
    if cut >= target:
        height = mid
        low = mid + 1
    else:
        high = mid - 1
        
print(height)



