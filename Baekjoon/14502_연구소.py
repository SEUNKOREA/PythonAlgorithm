from itertools import combinations
n, m = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(n)]
temp = [[0]*m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 빈 공간 좌표(즉, 벽을 세울 수 있는 조합을 계산하기 위해서)
emtpy_coord = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            emtpy_coord.append((i, j))

# 벽을 3개 세우는 조합
candidates = list(combinations(emtpy_coord, 3))

# 각 조합에 대해서 
answer = 0
for cand in candidates:
    for x in range(n):
        for y in range(m):
            temp[x][y] = data[x][y]

    count = 0
    # 해당 경우에 벽을 세움
    for c in cand:
        temp[c[0]][c[1]] = 1 

    # 바이러스 퍼트리기
    def virus(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    virus(nx, ny)
    for x in range(n):
        for y in range(m):
            if temp[x][y] == 2:
                virus(x, y)

    # 안전공간 계산
    for x in range(n):
        for y in range(m):
            if temp[x][y] == 0:
                count += 1
    answer = max(answer, count)

print(answer)

