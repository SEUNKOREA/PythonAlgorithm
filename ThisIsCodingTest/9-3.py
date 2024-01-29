INF = int(1e9)

# 노드의 개수
n = int(input())
# 간선의 개수
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신 ~ 자기자신 거리 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력받기
for _ in range(m):
    # a에서 b로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라서 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=" ")
    print()