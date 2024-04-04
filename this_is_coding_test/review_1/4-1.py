"""
이코테 구현 예제 4-1. 상하좌우
"""
n = int(input())
plans = input().split()

# 상하좌우 0123
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기위치
x, y = 0, 0

# 계획서 순차적으로 확인하면서 이동
for plan in plans:
    if plan == 'U':
        i = 0
    elif plan == 'D':
        i = 1
    elif plan == 'L':
        i = 2
    elif plan == 'R':
        i = 3
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < n:
        x, y = nx, ny

print(x+1, y+1)
