location = input()
LOC_TO_ID = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
             'e': 5, 'f': 6, 'g': 7, 'h': 8}

x = LOC_TO_ID[location[0]]
y = int(location[1])

cnt = 0
dx = [-2, -2, 2, 2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx <= 0 or ny <= 0 or nx > 8 or ny > 8:
        continue
    
    cnt += 1
print(cnt)