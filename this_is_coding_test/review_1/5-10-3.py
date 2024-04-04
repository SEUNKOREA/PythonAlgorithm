"""
이코테 DFS/BFS 실전3. 음료수 얼려먹기
DFS 풀이(교재풀이방식)
"""

n, m = map(int, input().split())
array = [list(map(int, list(input()))) for _ in range(n)]

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0: # 현재노드를 아직 방문하지 않았다면
        graph[x][y] = 1 # 현재노드 방문처리
        # 상하좌우 위치 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)