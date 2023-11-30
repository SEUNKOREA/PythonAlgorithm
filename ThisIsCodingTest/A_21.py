import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(n)] 

# 방향: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def process(x, y, index):
    # (x, y)의 위치와 연결된 연합국의 정보를 담는 리스트
    united = []
    united.append((x, y))

    # 연합국 지도에서 현재 위치에 연합국정보 표시
    union[x][y] = index 
    # 현재 연합의 전체 인구수
    total_num = graph[x][y]
    # 현재 연합 국가의 수
    total_country = 1

    # BFS를 위한 큐 자료구조 정의
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        # 현재위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 다음 확인하는 위치가 유효한 위치이면서 연합국 정보가 업데이트 안된 상항이라면
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에있는 나라와 인구차이가 L명이상 R명 이하라면
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    # 탐색대상으로 추가
                    q.append((nx, ny))
                    # 연합정보 업데이트
                    united.append((nx, ny))
                    union[nx][ny] = index
                    total_num += graph[nx][ny]
                    total_country += 1

    # 연합국가들끼리 인구를 분배
    for i, j in united:
        graph[i][j] = total_num // total_country




# 인구이동이 며칠동안 발생하는가
answer = 0

# 하나의 루프가 모든 연합국 찾아서 인구재배치 하는것까지
while True:
    # 매루프마다 연합국의 배열이 달라지기 때문에 연합국정보를 저장할 배열 선언
    # 인덱스에 해당하는 값은 연합국 정보
    # -1은 연합국이 아니라는 뜻
    union = [[-1] * n for _ in range(n)] 
    index = 0

    # 모든 국가들을 확인하면서 연합국끼리 인구배치 끝냄
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                
                print("현재 인구정보")
                for g in graph:
                    print(g)
                
                print("\n현재 연합국 상황")
                for u in union:
                    print(u)
                print("=======")

                index += 1
    print("종료조건을 확인합니다.")
    # 종료조건
    if index == n*n:
        break

    answer +=1
    print(answer)
    

# 정답출력
print(answer)