INF = int(1e9)

# 전체 회사의 개수(n)와 경로의 개수(m)
n, m = map(int, input().split())

# 출발지점에서 도착지점까지 도달하는 최단경로 이차원 리스트 초기화
distance = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신까지의 거리 0으로 초기화
for i in range(1, n+1):
    distance[i][i] = 0

# 회사 사이의 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1
    distance[b][a] = 1

# 방문판매(x), 소개팅 상대(k)
x, k = map(int, input().split())

for mid in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            distance[start][end] = min(distance[start][end], distance[start][mid] + distance[mid][end])

answer = distance[1][k] + distance[k][x]
if answer >= INF:
    print(-1)
else:
    print(answer)


