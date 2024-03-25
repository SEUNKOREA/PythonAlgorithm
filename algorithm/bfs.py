"""
BFS
1. 탐색시작노드를 큐에 삽입하고 방문처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
"""

from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9

def bfs():
    start = 1
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        print(now, end=' ')
        for adj_node in graph[now]:
            if not visited[adj_node]:
                q.append(adj_node)
                visited[adj_node] = True

bfs()