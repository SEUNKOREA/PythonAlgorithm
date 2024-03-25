import copy
import sys
sys.stdin = open('input.txt', 'r')

# 4 * 4 정사각형에 존재하는 (물고기 번호, 방향) 입력
array = [[] for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i].append([data[2*j], data[2*j+1] - 1]) # 방향의 경우 인덱스의 번호로 접근가능하여야하므로 1빼서 저장

# 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish_location(array, fish_num):
    for i in range(4):
        for j in range(4):
            if array[i][j] == fish_num:
                return i, j
    return None

def move_fishes(array, shark_x, shark_y):
    # 1번 물고기부터 16번 물고기까지 번호가 작은 순서대로 이동시킴
    for fish_num in range(1, 17):
        fish_data = find_fish_location(array, fish_num)
        if fish_data == None: # 물고기의 위치를 못찾은 경우(물고기가 상어에 먹힌경우)
            continue
        else: # 물고기가 남아있는 경우
            fish_x, fish_y = fish_data
            fish_direction = array[fish_x][fish_y][1]
            for _ in range(8):
                fish_nx = fish_x + dx[fish_direction]
                fish_ny = fish_y + dy[fish_direction]

                # 이동이 가능하다면(공간 안에 있으면서 빈칸이거나 다른 물고기가 있는 칸이라면(즉, 상어가 아니라면))
                if (0 <= fish_nx < 4 and 0 <= fish_ny < 4) and not(fish_nx == shark_x and fish_ny == shark_y):
                    array[fish_nx][fish_ny][1] = fish_direction  # 지금까지 회전한 것 지금 위치에 반영
                    array[fish_x][fish_y], array[fish_nx][fish_ny] = array[fish_nx][fish_ny], array[fish_x][fish_y]
                    break
                fish_direction = (fish_direction + 1) % 8  # 왼쪽으로 45도 회전

# 현재 상어의 위치에서 이동가능한 칸을 찾는 함수
def get_shark_candidate_position(array, shark_x, shark_y):
    candidate_position = []
    shark_direction = array[shark_x][shark_y][1]
    for _ in range(4):
        shark_x += dx[shark_direction]
        shark_y += dy[shark_direction]
        # 공간 안에 있으면서 물고기가 있는 칸이거나 빈칸이 아니라면
        if (0 <= shark_x < 4 and 0 <= shark_y < 4) and 1 <= array[shark_x][shark_y][0] <= 16 and array[shark_x][shark_y][0] != 0 and array[shark_x][shark_y][0] != -1 :
            candidate_position.append((shark_x, shark_y))
    return candidate_position

# 시뮬레이션 시작
def simulate(array, shark_x, shark_y, ate):
    global answer

    array = copy.deepcopy(array)
    # 현재 상어가 위치한 부분에 있는 물고기 먹기
    ate += array[shark_x][shark_y][0] # 먹은 물고기 번호 Cnt
    array[shark_x][shark_y][0] = -1  # 먹은 위치 -1로 값 변경

    move_fishes(array, shark_x, shark_y)

    candidate_position = get_shark_candidate_position(array, shark_x, shark_y)
    if len(candidate_position) == 0:
        answer = max(answer, ate)
        return
    for shark_nx, shark_ny in candidate_position:
        simulate(array, shark_nx, shark_ny, ate)

answer = 0
simulate(array, 0, 0, 0)
print(answer)








