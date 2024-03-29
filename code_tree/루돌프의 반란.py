"""
코드트리: 루돌프의 반란
https://www.codetree.ai/training-field/frequent-problems/problems/rudolph-rebellion/description?page=1&pageSize=20
"""
def in_board(x, y):
    if 1 <= x <= N and 1 <= y <= N:
        return True
    else:
        return False

def interaction(santa_num, sa_nx, sa_ny, lu_dx, lu_dy):  # santa_num >>> another_santa_num
    another_santa_num = array[sa_nx][sa_ny]  # 기존에 존재하던 산타번호
    array[sa_nx][sa_ny] = santa_num  # another_santa_num을 민 산타 배치
    santa[santa_num].x = sa_nx  # 산타 위치 정보 업데이트
    santa[santa_num].y = sa_ny

    # 루돌프로부터 밀린 산타에게 또 밀린 산타는 뒤로 한칸 이동
    sa_nnx = sa_nx + lu_dx
    sa_nny = sa_ny + lu_dy
    if in_board(sa_nnx, sa_nny):
        if array[sa_nnx][sa_nny] == 0:  # 빈칸
            array[sa_nnx][sa_nny] = another_santa_num  # 새로운 위치에 산타 배치
            santa[another_santa_num].x = sa_nnx  # 산타 위치 정보 업데이트
            santa[another_santa_num].y = sa_nny
        else:
            interaction(another_santa_num, sa_nnx, sa_nny, lu_dx, lu_dy)
    else:
        santa[another_santa_num].status = -1
        global live_santa
        live_santa -= 1
class Santa():
    def __init__(self, n, x, y, status, status_time, score):
        self.n = n
        self.x = x
        self.y = y
        self.status = status
        self.status_time = status_time
        self.score = score

import sys
sys.stdin = open('input.txt', 'r')

# 산타가 방향을 탐색하는 방향 (상>우>하>좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 게임판 크기, 게임턴 수, 산타의 수, 루돌프 힘, 산타 힘
N, M, P, C, D = map(int, input().split())
# 게임판 정보
array = [[0 for _ in range(N+1)] for _ in range(N+1)]
# 루돌프의 초기 위치
lu_x, lu_y = map(int, input().split())
array[lu_x][lu_y] = -1 # 루돌프 배치
# 산타 정보 입력
santa = {}
for _ in range(P):
    # n번 산타의 초기위치 x, y
    n, x, y = map(int, input().split())
    array[x][y] = n # 게임판에 산타배치
    santa[n] = Santa(n, x, y, 1, 0, 0)

# 게임이 n턴 동안 진행
live_santa = P
for stage in range(1, M+1):
    if live_santa <= 0:
        break
    # print(f"stage {stage}-----")
    # print('초기상태')
    # for a in array[1:]:
    #     print(a[1:])
    # print()

    ### 루돌프이동
    # 게임에서 탈락하지 않은 산타 중에서 가장 가까운 산타의 위치 찾기
    closeX, closeY = lu_x, lu_y # 가장 가까운 산타의 위치를 저장할 변수 초기화
    min_dist = int(1e9)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if array[i][j] != 0 and array[i][j] != -1:
                dist = (lu_x - i)**2 + (lu_y - j)**2
                if dist <= min_dist:
                    min_dist = dist
                    closeX, closeY = i, j

    # 루돌프가 이동할 한 칸의 방향 계산
    lu_dx, lu_dy = 0, 0 # 루돌프가 이동할 한 칸의 방향을 위한 변수 초기화
    if closeX - lu_x > 0:
        lu_dx = 1
    elif closeX - lu_x < 0:
        lu_dx = -1
    if closeY - lu_y > 0:
        lu_dy = 1
    elif closeY - lu_y < 0:
        lu_dy = -1

    if lu_dx == 0 and lu_dy == 0: #루돌프가 이동할 방향이 없다면
        pass
    else: # 루돌프가 이동한다면
        # 루돌프의 다음 위치
        lu_nx = lu_x + lu_dx
        lu_ny = lu_y + lu_dy

        # 루돌프의 다음 위치 확인
        if in_board(lu_nx, lu_ny): # 게임판 안에 있는 경우
            if array[lu_nx][lu_ny] == 0: # 빈칸
                array[lu_nx][lu_ny] = -1  # 새로운 위치에 루돌프 배치
                array[lu_x][lu_y] = 0     # 기존 루돌프 위치 빈칸만들기
                lu_x, lu_y = lu_nx, lu_ny # 루돌프 위치 값 업데이트
            else: # 산타가 존재
                sa_x, sa_y = lu_nx, lu_ny
                santa_num = array[sa_x][sa_y] # 기존에 존재하던 산타번호 저장
                santa[santa_num].score += C # 루돌프와 부딪힌 산타는 C점 얻음
                santa[santa_num].status = 0 # 루돌프와 부딪힌 산타는 기절
                santa[santa_num].status_time = stage

                array[lu_nx][lu_ny] = -1 # 새로운 위치에 루돌프 배치
                array[lu_x][lu_y] = 0  # 기존 루돌프 위치 빈칸만들기
                lu_x, lu_y = lu_nx, lu_ny  # 루돌프 위치 값 업데이트

                # 산타가 루돌프가 이동한 방향으로 뒤로 C칸 밀림
                sa_nx = sa_x + lu_dx * C
                sa_ny = sa_y + lu_dy * C
                if in_board(sa_nx, sa_ny): # 산타가 밀리는 위치가 보드 안에 있는 경우
                    if array[sa_nx][sa_ny] == 0: # 빈칸
                        array[sa_nx][sa_ny] = santa_num # 새로운 위치에 산타 배치
                        santa[santa_num].x = sa_nx # 산타 위치 정보 업데이트
                        santa[santa_num].y = sa_ny
                    else: # 또 다른 산타가 존재
                        interaction(santa_num, sa_nx, sa_ny, lu_dx, lu_dy)
                else: # 산타가 밀려서 보드 밖으로 넘어가는 경우
                    santa[santa_num].status = -1  # 루돌프와 부딪혀서 보드 밖으로 넘어간 산타는 탈락
                    live_santa -= 1
        else: # 게임판 밖에 있으면 움직이지 않는다.
            pass
    # print("루돌프 이동 후")
    # for a in array[1:]:
    #     print(a[1:])
    # print()


    ### 산타 이동
    for n in range(1, P+1):
        # print(f"{n}번 산타 상태 {santa[n].status}")
        if santa[n].status == 0: # 기절한 산타라면
            if santa[n].status_time + 2 == stage:
                santa[n].status = 1
        if santa[n].status ==1 : # 생존한 산타만 움직임
            # 현재 산타의 좌표
            sa_x = santa[n].x
            sa_y = santa[n].y
            before_dist = (sa_x - lu_x)**2 + (sa_y - lu_y)**2 # 현재좌표에서 루돌프와의 거리

            # 루돌프와 가까워질 수 있는지 확인
            idx = -1
            for i in range(4):
                sa_nx = sa_x + dx[i]
                sa_ny = sa_y + dy[i]
                if in_board(sa_nx, sa_ny) and (array[sa_nx][sa_ny] == 0 or array[sa_nx][sa_ny] == -1):
                    # 유효한 좌표이면서 빈칸이거나 루돌프가 존재해서 이동가능한 경우
                    after_dist = (sa_nx - lu_x)**2 + (sa_ny - lu_y)**2
                    if after_dist < before_dist: # 루돌프와의 거리를 비교해서 현재위치보다 루돌프와 가까워지는 경우에만 이동
                        before_dist = after_dist
                        idx = i
            if idx != -1: # 산타가 이동하는 경우
                # 산타의 다음 위치 계산
                sa_nx = sa_x + dx[idx]
                sa_ny = sa_y + dy[idx]

                if array[sa_nx][sa_ny] == -1: # 다음 위치에 루돌프가 존재하는 경우 충돌 발생
                    santa[n].status = 0 # 기절
                    santa[n].status_time = stage
                    santa[n].score += D # 산타는 D만큼 점수를 얻음
                    sa_nx -= (dx[idx] * D) # 자신이 이동해온 반대 방향으로 D칸만큼 밀려남
                    sa_ny -= (dy[idx] * D)

                    if not in_board(sa_nx, sa_ny):
                        santa[n].status = -1 # 밀려나는 위치가 보드 밖이라면 그 산타는 탈락
                        live_santa -= 1
                        array[sa_x][sa_y] = 0 # 기존 산타 위치 빈칸으로 변경
                    else: # 밀려난 위치가 보드 안인 경우
                        if array[sa_nx][sa_ny] == 0: # 밀려난 위치가 빈칸이라면
                            array[sa_x][sa_y] = 0  # 기존 산타 위치 빈칸으로 변경
                            array[sa_nx][sa_ny] = n # 밀려난 위치에 산타 배치
                            santa[n].x = sa_nx
                            santa[n].y = sa_ny
                        elif array[sa_nx][sa_ny] != n: # 밀려난 위치에 자기자신이 아닌 다른 산타가 존재한다면
                            array[sa_x][sa_y] = 0  # 기존 산타 위치 빈칸으로 변경
                            interaction(n, sa_nx, sa_ny, -dx[idx], -dy[idx])
                elif array[sa_nx][sa_ny] == 0: # 다음 위치가 빈칸인 경우
                    array[sa_x][sa_y] = 0 # 기존 위치 비워주고
                    array[sa_nx][sa_ny] = n # 새로운 위치에 산타 배치
                    santa[n].x = sa_nx # 산타 위치 업데이트
                    santa[n].y = sa_ny
            else: # 산타가 이동하지 않는 경우
                pass
        # print(f"{n}번 산타이동 후")
        # for a in array[1:]:
        #     print(a[1:])
        # print()

    # 매턴 이후 아직 탈락하지 않은 산타들에게 1점 씩 부여
    for i in range(1, P+1):
        if santa[i].status != -1:
            santa[i].score += 1

for i in range(1, P+1):
    print(santa[i].score, end=' ')