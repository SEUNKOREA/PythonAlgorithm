"""
DFS
1. 탐색시작노드를 스택에 삽입하고 방문처리를 한다
2. 스택의 최상단 노드에 방문하지 않은 인접노드가 있으면 그 인접노드를 스택에 넣고 방문처리를 한다.
이 때, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
"""

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

def dfs(node):
    visited[node] = True # 현재노드 방문처리
    print(node, end=' ')
    for adj_node in graph[node]:
        if not visited[adj_node]:
            dfs(adj_node)

dfs(1)
