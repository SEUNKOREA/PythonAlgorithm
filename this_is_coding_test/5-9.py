from collections import deque

def bfs(start, graph, visited):
    visited[start] = True
    q = deque([start])

    while q:
        now = q.popleft()
        print(now, end= ' ')

        for node in graph[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
    return 

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9

bfs(1, graph, visited)
