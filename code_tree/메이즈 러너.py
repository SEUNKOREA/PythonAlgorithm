import sys
sys.stdin = open('input.txt', 'r')
import copy

def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_squre():
    for length in range(2, n+1):
        for si in range(1, n+2-length):
            for sj in range(1, n+2-length):
                contain_exit, contain_parti = False, False
                for i in range(si, si+length):
                    for j in range(sj, sj+length):
                        if arr[i][j] == -11: contain_exit = True
                        if -11 < arr[i][j] < 0: contain_parti = True
                if contain_exit and contain_parti:
                    return si, sj, length

def turn_left(si, sj, length):
    org_arr = [narr[i][sj:sj+length] for i in range(si, si+length)]
    new_arr = [[0] * length for _ in range(length)]

    # 회전한 부분 배열
    for i in range(length):
        for j in range(length):
            new_arr[j][length - i - 1] = org_arr[i][j]


    # 회전한 부분 배열 결과 원래 배열에 적용
    for i in range(length):
        for j in range(length):
            if 1 <= new_arr[i][j] <= 9:
                narr[si + i][sj + j] = new_arr[i][j] - 1
            else:
                narr[si + i][sj + j] = new_arr[i][j]

def find_exit(si, sj, length):
    for i in range(si, si+length):
        for j in range(sj, sj+length):
            if narr[i][j] == -11:
                return i, j

### 입력
# 좌표의 크기, 참가자의 수, 게임시간
n, m, k = map(int, input().split())
# n x n 미로정보 (가장자리 10으로 감쌈)
arr = [[10] * (n+2)] + [[10] + list(map(int, input().split())) + [10] for _ in range(n)] + [[10] * (n+2)]
# 참가자 좌표정보
for _ in range(m):
    x, y = map(int, input().split())
    arr[x][y] -= 1 # 참가자의 위치는 -1
# 출구좌표
exit_x, exit_y = map(int, input().split())
arr[exit_x][exit_y] = -11    # 출구의 위치는 -11

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
remain = m
total = 0

# ### 디버깅
# print("초기상태")
# for a in arr[1: -1]:
#     print(a[1:-1])

while time < k:
    time += 1

    # ### 디버깅
    # print(f"time = {time}")

    ### 참가자의 이동
    narr = copy.deepcopy(arr)
    for x in range(1, n+1):
        for y in range(1, n+1):
            if -11 < arr[x][y] < 0: # 참가자가 위치한 곳
                cur_dist = get_dist(x, y, exit_x, exit_y)
                ti = -1 # 타겟인덱스
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if not 1 <= arr[nx][ny] <= 10: # 이동할수 있는 지점이라면(벽이 아닌 지점)
                        dist = get_dist(nx, ny, exit_x, exit_y)
                        if dist < cur_dist: # 거리가 짧아진다면 이동
                            # print(f"{(x, y)} >> {(nx, ny)}")
                            total -= arr[x][y] # 이동거리 누적
                            narr[x][y] -= arr[x][y] # 기존 위치에서 이동
                            if arr[nx][ny] == -11: # 이동하는 위치가 출구
                                remain += arr[x][y] # 남아있는 참가자의 수 업데이트
                                # print(f"{(x, y)} 사라짐")
                            elif -11 < arr[nx][ny] <= 0: # 다른 참가자가 위치한 곳이거나 빈칸인 경우
                                narr[nx][ny] += arr[x][y]
                            break
    arr = narr
    ### 디버깅
    # print("이동 후 맵 상태")
    # for a in narr[1: -1]:
    #     print(a[1:-1])
    # print("남아있는 사람", remain)
    # cnt = 0
    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         if -11 < narr[i][j] < 0:
    #             cnt += 1
    # print(cnt)
    # print()


    ### 남아있는 참가자가 없으면 게임종료
    if remain <= 0:
        break

    ### 출구와 참가자 최소 1명을 포함한 가장 작은 정사각형 찾기
    si, sj, length = find_squre()
    # print("정사각형 정보", si, sj, length)
    ### 정사각형 회전
    turn_left(si, sj, length)
    ### 출구위치 업데이트
    exit_x, exit_y = find_exit(si, sj, length)
    arr = copy.deepcopy(narr)

    ### 디버깅
    # print("회전 후")
    # for a in narr[1: -1]:
    #     print(a[1:-1])
    # print()

print(total)
print(exit_x, exit_y)