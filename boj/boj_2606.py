"""
BOJ 2606. 바이러스
출처: https://www.acmicpc.net/problem/2606
"""
import sys
sys.stdin = open('input.txt', 'r')
def dfs(node):
    visited[node] = True
    global cnt
    cnt += 1

    for adj in graph[node]:
        if not visited[adj]:
            dfs(adj)

n = int(input()) # 노드의 개수
m = int(input()) # 간선의 개수

# 정답(웜바이러스에 걸리게되는 컴퓨터의 수 count)
cnt = 0
# 연결리스트 그래프
graph = [[] for _ in range(n+1)]
# 방문정보를 추적할 리스트
visited = [False] * (n+1)

# 간선정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

print(cnt-1)