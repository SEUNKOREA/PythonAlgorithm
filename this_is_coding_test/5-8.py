def dfs(start, graph, visited):
    visited[start] = True
    print(start, end = ' ')

    for node in graph[start]:
        if not visited[node]:
            dfs(node, graph, visited)

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

dfs(1, graph, visited)