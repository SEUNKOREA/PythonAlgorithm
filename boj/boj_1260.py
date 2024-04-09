"""
BOJ 1260. DFS와 BFS
출처: https://www.acmicpc.net/problem/1260
"""
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for adj in graph[node]:
        if not visited[adj]:
            dfs(adj)

def bfs(node):
    visited[node] = True
    q = deque([node])
    while q:
        now = q.popleft()
        print(now, end=' ')
        for adj in graph[now]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True


# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())
# 그래프 연결리스트 정보
graph = [[] for _ in range(n+1)]
# 방문정보를 저장할 리스트
visited = [False] * (n+1)
# 간선이 연결하는 두 정점의 번호
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()

dfs(v)
print()

# 방문정보를 저장할 리스트
visited = [False] * (n+1)

bfs(v)