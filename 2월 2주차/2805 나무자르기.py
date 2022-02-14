import sys

n, target = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

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

tree.sort()

def sum(target):
    result = 0
    low = 0
    high = len(tree)

    while low < high:
        midd = (low + high) // 2

        if tree[midd] <= target:
            low = midd + 1

        else:
            high = midd

    for i in range(low, len(tree)):
        result += (tree[i] - target)
    


    return result



low = 0
high =  tree[n-1]
height = 0
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



