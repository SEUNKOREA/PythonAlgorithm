# 상하좌우
coord = [1,1]
cnt = 0
n = int(input())
for plan in list(input().split()):
    if plan == 'L':
        if coord[1]==1: continue
        coord[1] -= 1
        cnt += 1
    elif plan == 'R':
        if coord[1]==5: continue
        coord[1] += 1
        cnt += 1
    elif plan == 'U':
        if coord[0]==1: continue
        coord[0] -= 1
        cnt += 1
    elif plan == 'D':
        if coord[0]==n: continue
        coord[0] += 1
        cnt += 1
print(coord[0], coord[1])

