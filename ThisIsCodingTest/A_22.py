from collections import deque

def get_next_coord(coord, new_map):
    (x1, y1), (x2, y2) = coord
    next_coord = []

    # 이동(상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx1, ny1, nx2, ny2 = x1+dx[i], y1+dy[i], x2+dx[i], y2+dy[i]
        if new_map[nx1][ny1] == 0 and new_map[nx2][ny2] == 0:
            next_coord.append({(nx1, ny1), (nx2, ny2)})
    
    # 회전 (로봇이 가로방향일 경우)
    if x1 == x2:
        for i in [1, -1]:
            nx1, ny1, nx2, ny2 = x1 + i, y1, x2 + i, y2
            if new_map[nx1][ny1] == 0 and new_map[nx2][ny2] == 0:
                next_coord.append({(x1, y1), (nx1, ny1)})
                next_coord.append({(x2, y2), (nx2, ny2)})
    
    # 회전 (로봇이 세로방향일 경우)
    if y1 == y2:
        for i in [1, -1]:
            nx1, ny1, nx2, ny2 = x1, y1 + i, x2, y2 + i
            if new_map[nx1][ny1] == 0 and new_map[nx2][ny2] == 0:
                next_coord.append({(x1, y1), (nx1, ny1)})
                next_coord.append({(x2, y2), (nx2, ny2)})
    
    return next_coord

def solution(board):
    # 맵 확장
    n = len(board)
    new_map = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_map[i+1][j+1] = board[i][j]
    
    q = deque([]) # 순회할 위치가 저장될 큐
    visited = [] # 방문한 위치가 저장될 리스트

    # 현재위치
    start = {(1, 1), (1, 2)}
    q.append((start, 0))
    visited.append(start)

    while q:
        coord, cost = q.popleft()

        # 목적지에 도착한 경우 반복문 빠져나감
        if (n, n) in coord:
            return cost
        
        for next_coord in get_next_coord(coord, new_map):
            if next_coord not in visited:
                q.append((next_coord, cost+1))
                visited.append(next_coord)
    return 0

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))