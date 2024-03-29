from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 이동
    for i in range(4):
        pos1_nx, pos1_ny, pos2_nx, pos2_ny = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하려는 좌표가 비워있어야함
        if board[pos1_nx][pos1_ny] == 0 and board[pos2_nx][pos2_ny] == 0:
            next_pos.append({(pos1_nx, pos1_ny), (pos2_nx, pos2_ny)})
                
    # 회전
    # 현재 가로로 놓여져 있는 경우
    if pos1_x == pos2_x:
        # 아래쪽으로 회전하거나 위쪽으로 회전하거나
        for i in [1, -1]:
            # 회전하려는 방향기준으로 블럭이 비워져 있는가
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
    # 현재 세로로 놓여져 있는 경우
    elif pos1_y == pos2_y:
        # 오른쪽으로 회전하거나 왼쪽으로 회전하거나
        for i in [1, -1]:
            # 회전하려는 방향을 기준으로 블럭이 비워져 있는가
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
    
    return next_pos

def solution(board):
    # 맵의 외각에 벽을 두는 형태로 맵 변경
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    # 너비우선탐색 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달했다면 최단거리이므로 반환
        if (n, n) in pos:
            return cost

        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문처리
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)