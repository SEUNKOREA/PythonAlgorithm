INF = int(1e9)

# 학생수(n), 학생성적 비교수(m)
n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]
# 두 학생의 성적을 비교한 정보
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 0
# 자기자신
for i in range(1, n+1):
    graph[i][i] = 0

# 플루이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

answer = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[i][j] != INF:
            count += 1
    if count == n:
        answer += 1
print(answer)


