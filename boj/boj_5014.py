import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def bfs():
    q = deque()
    visited = [0] * (F+1)

    q.append(S)
    visited[S] = 1 # Return 할 때는 -1로 리턴

    while q:
        c = q.popleft()
        if c == G:
            return visited[G]-1
        for nc in [c+U, c-D]: # 두방향
            if 1 <= nc <= F and visited[nc] == 0: # 범위내, 미방문
                q.append(nc)
                visited[nc] = visited[c] + 1
    # 목적지를 찾을 수 없는 경우
    return "use the stairs"

F, S, G, U, D = map(int, input().split())
ans = bfs()
print(ans)
