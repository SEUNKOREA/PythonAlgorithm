n = int(input())
data = input().split()

# 시작위치
x, y = 0, 0

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check_valid():
    if 0 <= nx < n and 0 <= ny < n:
        return True
    return False

for i in range(len(data)):
    if data[i] == 'L':
        nx = x + dx[0]
        ny = y + dy[0]        
    elif data[i] == 'R':
        nx = x + dx[1]
        ny = y + dy[1]    
    elif data[i] == 'U':
        nx = x + dx[2]
        ny = y + dy[2]    
    elif data[i] == 'D':
        nx = x + dx[3]
        ny = y + dy[3]    
    
    if check_valid():
        x, y = nx, ny
    else:
        continue

print(x+1, y+1)