n = int(input())
k = int(input())

### 맵 초기화
map_arr = [[0]*(n+1) for _ in range(n+1)]
### 사과 표시(1)
for _ in range(k):
    a, b = map(int, input().split())
    map_arr[a][b] = 1

### 방향정보 입력
info = []
l = int(input())
for _ in range(l):
    sec, c = input().split()
    info.append((int(sec), c))

def simulation():
    ### 뱀의 처음 머리위치(2)
    x, y = 1,1 
    map_arr[x][y] = 2
    ### 뱀이 차지하고 있는 위치정보
    snail = [(x,y)]
    ### 처음 방향(동쪽)
    d_idx = 0
    dx = [0, 1, 0, -1] # 동,남,서,북
    dy = [1, 0, -1, 0]
    ### 흐르는 시간
    time = 0
    ### 방향정보에서 비교할 시간 인덱스
    t_idx = 0

    while True:
        ### 다음 머리 위치값
        nx = x + dx[d_idx]
        ny = y + dy[d_idx]
        
        ### 다음 위치값이 map 내부에 있으며 자기자신과 만나지 않는다면
        if 1 <= nx and nx<=n and 1 <= ny and ny <= n and map_arr[nx][ny]!=2:
            ### 사과가 없다면
            if map_arr[nx][ny] == 0:
                map_arr[nx][ny] = 2 # 다음 위치로 뱀의 머리 이동
                snail.append((nx, ny))
                px, py = snail.pop(0) # 기존의 꼬리 위치를
                map_arr[px][py] = 0 # 앞으로 가져온다. (즉, 원래 아무것도 없는 상태로 돌려놓음)
            ### 사과가 있다면
            if map_arr[nx][ny] == 1:
                map_arr[nx][ny] = 2
                snail.append((nx, ny))

        ### 벽이나 자기자신과 부딪힘
        else:
            time += 1
            break
        
        x, y = nx, ny
        time += 1
        print(x,y)
        print(snail)

        ### 회전할 시간일 경우 회전방향에 맞춰서 방향전환
        if t_idx < l and time == info[t_idx][0]:
            if info[t_idx][1] == 'L':
                d_idx = (d_idx - 1) % 4
            else:
                d_idx = (d_idx + 1) % 4
            t_idx += 1

    return time

print(simulation())