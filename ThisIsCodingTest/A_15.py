from collections import deque

# n: 도시의 개수
# m: 도로의 개수
# k: 거리정보
# x: 출발 도시의 번호
n, m, k, x = map(int, input().split())

# 출발도시에서부터 모든 도시(인덱스)까지의 최단거리가 저장될 배열 (-1로 초기화)
distance = [-1] * (n+1)
# 출발도시에서 출발도시 자기자신까지의 거리는 0으로 설정한다.
distance[x] = 0

# 인접한 도로정보가 저장될 배열
# 각 인덱스는 하나의 도시를 나타내며 인덱스에 해당하는 도시와 인접한 도시가 리스트의 요소로 추가되어있다.
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([x])

while q:
    now = q.popleft()
    for adj in graph[now]:
        if distance[adj] == -1:
            distance[adj] = distance[now] + 1
            q.append(adj)

flag = True
for idx, value in enumerate(distance):
    if idx == 0:
        continue
    if value == k:
        flag = False
        print(idx)
if flag:
    print(-1)



