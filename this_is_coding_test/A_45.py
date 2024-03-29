"""
출처: https://www.acmicpc.net/problem/3665
"""

from collections import deque

for tc in range(int(input())):
    # 팀의 수(n) == 노드의 개수
    n = int(input())
    # 작년 순위 정보 입력받기
    data = list(map(int, input().split()))

    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접행렬 초기화
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # 올해 변경된 순위 정보입력
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상정렬 시작
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상정렬 결과가 오직 하나인지의 여부
    cycle = False # 그래프 내 사이클이 존재하는 지 여부

    for i in range(n):
        if len(q) == 0: # n번을 돌기 전에 큐가 비었다면 사이클이 발생했다는 의미
            cycle = True
            break
        if len(q) >= 2: # 큐에 든 원소가 2개라면 가능한 정렬결과가 여러 개라는 의미
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j]: # 현재노드와 연결된 노드의 간선 삭제
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 된 경우 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)


    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for r in result:
            print(r, end=' ')
        print()
