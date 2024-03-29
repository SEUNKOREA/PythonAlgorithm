import heapq

INF = int(1e9)

# 전체 회사의 개수(n)와 경로의 개수(m)
n, m = map(int, input().split())

# 회사 사이의 정보 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

# 방문판매(x), 소개팅 상대(k)
x, k = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        # 이미 방문한 노드의 경우 건너뛰기
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]

to_k = dijkstra(1, k)
to_x = dijkstra(k, x)

if to_k == INF or to_x == INF:
    print(-1)
else:
    print(to_k + to_x)



