import sys
sys.stdin = open('input.txt', 'r')

N, M, H, K = map(int, input().split())

# 도망자 좌표 및 방향
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))

# 도망자 방향 좌 우 하 상
di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]
opp = {0:1, 1:0, 2:3, 3:2} # 반대방향


# 나무좌표 입력
tree = set()
for _ in range(H):
    i, j = map(int, input().split())
    tree.add((i, j))


# 술래방향 상 우 하 좌 (바깥쪽으로 돌 때)
tdi = [-1, 0, 1, 0]
tdj = [0, 1, 0, -1]

mx_cnt, cnt, flag, val = 1, 0, 0, 1
ti, tj, td = (N+1)//2, (N+1)//2, 0

answer = 0

for k in range(1, K+1): # K턴만큼 게임진행
    # [1] 도망자의 이동 (arr)
    for i in range(len(arr)):
        if abs(arr[i][0]-ti) + abs(arr[i][1]-tj) <= 3: # 술래와의 거리가 3 이하인경우
            ni, nj = arr[i][0] + di[arr[i][2]], arr[i][1] + dj[arr[i][2]]
            if 1 <= ni <= N and 1 <= nj <= N: # 범위 안
                if (ni, nj) != (ti, tj):      # 다음 위치가 술래 위치가 아니면
                    arr[i][0], arr[i][1] = ni, nj
            else: # 범위 밖
                arr[i][2]=opp[arr[i][2]]# 반대 방향전환 및 저장
                ni,nj=arr[i][0]+di[arr[i][2]],arr[i][1]+dj[arr[i][2]]
                if (ni, nj) != (ti, tj):      # 다음 위치가 술래 위치가 아니면
                    arr[i][0], arr[i][1] = ni, nj


    # [2] 술래의 이동
    cnt += 1
    ti, tj = ti+tdi[td], tj+tdj[td]

    if (ti, tj) == (1, 1): # 안쪽으로 돌기
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td = 2             # 초기방향은 아래
    elif (ti, tj) == ((N+1)//2, (N+1)//2): # 바깥쪽으로 돌기
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0             # 초기방향은 위
    else:
        if cnt == mx_cnt:
            cnt = 0
            td = (td + val) % 4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                mx_cnt += val


    # [3] 도망자 잡기 (술래자리 포함 세칸)
    # 나무가 없는 도망자면 잡힘
    tset = set(((ti, tj), (ti+tdi[td], tj+tdj[td]), (ti+tdi[td]+tdi[td], tj+tdj[td]+tdj[td])))
    for i in range(len(arr)-1, -1, -1):
        if (arr[i][0], arr[i][1]) in tset and (arr[i][0], arr[i][1]) not in tree:
            arr.pop(i)
            answer += k

    # 도망자가 없다면 더이상 점수도 없음
    if not arr:
        break
print(answer)