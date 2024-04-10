import heapq
def solution(n, paths, gates, summits):
    INF = int(1e9)

    # 연결리스트 정보 Update
    graph = [[] for _ in range(n+1)]
    for path in paths:
        a, b, cost = path # a >> b로 가는 경로의 비용이 cost
        # 양방향 도로이기 때문에 a, b 모두에 경로 추가 및 비용이 낮은 순서대로 탐색하기 위해 cost를 첫번쨰 요소로 넣어줌
        graph[a].append((cost, b))
        graph[b].append((cost, a))

    # 각 출입구에서 산봉우리까지의 최단거리를 담을 리스트
    distance = [INF] * (n+1)
    q = []
    for gate in gates:
        distance[gate] = 0 # 게이트까지의 거리는 0
        heapq.heappush(q, [0, gate])

    # 다익스트라
    while q:
        intensity, node = heapq.heappop(q)

        if distance[node] < intensity or node in summits:
            # 현재노드까지의 인텐시티보다 최단거리가 작으면 업데이트 X
            # 노드가 산봉우리라면 방문하지 않는다.
            continue

        for cost, adj_node in graph[node]:
            cost = max(distance[node], cost)
            if distance[adj_node] > cost:
                distance[adj_node] = cost
                heapq.heappush(q, [cost, adj_node])

    result = [-1, INF]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
    return result


if __name__ == "__main__":
    n = 5
    paths = [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]
    gates = [1, 2]
    summits = [5]

    ans = solution(n, paths, gates, summits)
    print(ans)