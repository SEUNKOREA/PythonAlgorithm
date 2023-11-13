import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
data = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    data[a].append(b)

## 시작지점으로부터 해당 인덱스에 해당하는 도시까지의 최단거리가 저장될 배열
distance = [-1] * (n+1)
distance[x] = 0 # 시작지점으로부터 자기자신까지의 거리는 0으로 설정

q = deque([x])

while q:
    # 내가 현재 탐색할 도시의 시작 위치
    # 처음에는 당연히 x로 시작
    # 이후에는 해당 도시와 인접한 도시들이 여기에 저장되어서 인접한 도시들을 탐색하게 되는 것
    now = q.popleft()

    # 현재 탐색하고 있는 도시와 인접한 도시들을 순회하면서
    for adj_city in data[now]:
        if distance[adj_city] == -1: # 거리값이 -1이라면 아직 순회 안된거니까 거리 업데이트
            # 시작위치부터 현재 탐색하고 있는 도시까지의 거리 + 1
            distance[adj_city] = distance[now] + 1
            # 다음에 또 순회해야하기 때문에 큐에 넣어준다.
            q.append(adj_city)

check = False
for idx, dist in enumerate(distance):
    if idx == 0:
        continue
    if dist == k:
        check = True
        print(idx)

if check == False:
    print(-1)