import heapq
INF = int(1e9)

# 도시의 개수(n), 통로의 개수(m), 메시지를 보내고자 하는 도시(c)
n, m, c = map(int, input().split())

# 통로에 관한 정보 업데이트
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    # x에서 y로 이어지는 통로가 있으며 메시지가 전달되는 시간이 z
    graph[x].append((y, z))

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start=c)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작노드는 제외해야 하므로 count-1 출력
print(count-1, max_distance)

