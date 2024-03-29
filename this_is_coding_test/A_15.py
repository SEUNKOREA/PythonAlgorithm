from collections import deque
# 도시의 개수, 도로의 개수, 거리정보, 출발 도시의 번호
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # a -> b 단방향 도로 존재

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()

    for adj_node in graph[now]:
        if distance[adj_node] == -1:
            distance[adj_node] = distance[now] + 1
            q.append(adj_node)

flag = False

for i in range(1, n+1):
    if distance[i] == k:
        flag = True
        print(i)
if flag == False:
    print(-1)