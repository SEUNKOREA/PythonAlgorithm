# 전체 회사의 개수와 경로의 개수
n, m = map(int, input().split())

# 무한정의
INF = int(1e9)
# 그래프 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신 ~ 자기자신 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 그래프 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


# 플로이드 워셜 알고리즘 수행
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

# 회사, 소개팅
x, k = map(int, input().split())

answer = graph[1][k]+graph[k][x]
if answer >= INF:
    answer = -1
print(answer)





