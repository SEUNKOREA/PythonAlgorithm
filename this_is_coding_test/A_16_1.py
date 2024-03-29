from itertools import combinations
from collections import deque

n, m = map(int, input().split())

graph = [[0] * (m+1) for _ in range(n+1)]

empty = []
virus = []

for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, m+1):
        if row[j-1] == 0:   # 빈칸정보 저장
            empty.append((i, j))
        elif row[j-1] == 2: # 바이러스 정보 저장
            virus.append((i, j))
        graph[i][j] = row[j-1]

# 빈칸 중에서 새롭게 벽을 세울 조합 구하기
candidates = combinations(empty, 3)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

for candidate in candidates:

    # 지도 초기화
    data = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            data[i][j] = graph[i][j]
    
    
    # 벽 세우기
    for wall in candidate:
        data[wall[0]][wall[1]] = 1


    # 바이러스 전파
    for v in virus:
        q = deque([v])
        
        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 1<= nx <= n and 1 <= ny <= m:
                    if data[nx][ny] == 0:
                        data[nx][ny] = 2
                        q.append((nx, ny))

    
    # 안전공간 개수 count
    safety = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if data[i][j] == 0:
                safety += 1

    answer = max(safety, answer)

print(answer)