from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


answer = 0

while True:
    group_num = 0
    union = [[-1] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if union[x][y] == -1:
                q = deque([(x, y)])
                union[x][y] = group_num
                group = [(x, y)]
                populate = data[x][y]
                while q:
                    xx, yy = q.popleft()

                    for i in range(4):
                        nx = xx + dx[i]
                        ny = yy + dy[i]

                        if 0 <= nx < n and 0 <= ny < n:
                            if union[nx][ny] == -1:
                                diff = abs(data[xx][yy] - data[nx][ny])
                                if l <= diff <= r:
                                    q.append((nx, ny))
                                    union[nx][ny] = group_num
                                    group.append((nx, ny))
                                    populate += data[nx][ny]
                # 인원 나누기
                populate //= len(group)

                for g in group:
                    data[g[0]][g[1]] = populate

                group_num += 1

    if group_num == n*n:
        break
    
    answer += 1

print(answer)


    


