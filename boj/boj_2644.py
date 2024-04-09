"""
BOJ 2644. 촌수계산
https://www.acmicpc.net/problem/2644
"""

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(s, e):
    q = deque([s])
    visited[s] = 1
    while q:
        now = q.popleft()
        if now == e:
            return visited[e] - 1
        for adj in graph[now]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] += visited[now]+1
    return -1

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

n = int(input()) # 전체 사람수
s, e = map(int, input().split()) # 촌수를 계산해야하는 서로 다른 두사람의 번호
m = int(input()) # 간선의 개수
graph = [[] for _ in range(n+1)]
for _ in range(m): # 부모 자식간의 입력으로 리스트 업데이트
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

visited = [0] * (n+1)

ans = bfs(s, e)
print(ans)