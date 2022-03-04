# 백트래킹 -> 왔던 것을 기억하고 다시 되돌아간다.


def dfs(num): # num은 수열의 개수

    # 만약 수열의 개수가 최대 개수에 도달하면
    # 해당 수열을 str로 변환시키고 출력하고
    # return한다
    if num == m:
        print(' '.join(map(str,graph)))
        return
    
    # 아닐 경우에 n만큼 반복문을 돌고
    # 방문했으면 수열에 해당 숫자를 추가하고
    # 개수를 하나 추가한채 다시 dfs를 돌린다.

    # 재귀함수를 호출한 후에는 다시 되돌아갸 하기때문에
    # 다시 방문여부를 false로 해주고 그래프를 하나빼준다.
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            graph.append(i)
            dfs(num + 1)
            visited[i] = False
            graph.pop()




import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int,input().split())

graph = []
visited = [False] * (n+1)

dfs(0)