from collections import deque
import copy

# 듣고자 하는 강의의 수
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v+1)]
# 각 각의 시간을 0으로 초기화
time = [0] * (v+1)

# 방향그래프의 모든 간선정보 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]   # 강의시간 업데이트
    for x in data[1:-1]:
        indegree[i] += 1    # 진입차수 업데이트
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for node in graph[now]:
            result[node] = max(result[node], result[now]+time[node])
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)


    for i in range(1, v+1):
        print(result[i])

topology_sort()


