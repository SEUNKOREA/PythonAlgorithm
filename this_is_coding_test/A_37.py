INF = int(1e9)

# 도시의 개수(n)
n = int(input())
# 버스의 개수(m)
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 버스의 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 출발하여 b에 도착하는데 드는 비용 c
    graph[a][b] = min(graph[a][b], c)


# 자기자신까지의 거리는 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] >= INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()