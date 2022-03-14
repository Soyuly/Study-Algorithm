import sys
import heapq

n = int(sys.stdin.readline().strip())

heap = []
result = ''
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        try:
            result += str(heapq.heappop(heap)) + '\n'
            
        except:
            result += '0' + '\n'
    else:
        heapq.heappush(heap,x)

print(result)