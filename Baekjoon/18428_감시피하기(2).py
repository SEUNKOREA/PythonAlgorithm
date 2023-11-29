from itertools import combinations

n = int(input())
graph = []
teachers = []
spaces = []

for i in range(n):
    row = input().split()
    graph.append(row)
    for j in range(n):
        if row[j] == 'T':
            teachers.append((i, j))
        elif row[j] == 'X':
            spaces.append((i, j))

candidates = list(combinations(spaces, 3))
#print(f"총 후보의 개수는 :{len(candidates)}\n")
# cnt = len(candidates)

def dfs(x, y, dir):

    nx = x + dir[0]
    ny = y + dir[1]

    # 그래프의 범위를 벗어나지 않는 경우
    while (nx >= 0 and nx < n and ny >= 0 and ny < n):
        # print(f"({nx}, {ny}) 탐색을 시작합니다.")
        # 학생을 만나면 True 반환
        if graph[nx][ny] == 'S':
            #print(f"({nx}, {ny})에서 학생을 만났습니다.")
            return True
        # 벽을 만난경우
        elif graph[nx][ny] == 'O':
            #print(f"({nx}, {ny})에서 벽을 만났습니다.")
            return False
        nx += dir[0]
        ny += dir[1]
        
    return False


def check_findness():
    direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    for teacher in teachers:
        for i in range(4):
            # 학생을 한 명이라도 찾은 경우
            if dfs(teacher[0], teacher[1], direction[i]) == True:
                return True
    return False


find = False

for candidate in candidates:
    # 해당하는 좌표에 벽 세우기
    for coord in candidate:
        graph[coord[0]][coord[1]] = 'O'
    # for g in graph:
    #     print(g)
    # cnt -= 1

    # 각각의 선생님들에 대해서 전 방향으로 탐색시작
    # 학생을 한 명도 못 찾은 경우
    if not check_findness():
        find = True
        break
        
    # 다음 후보 벽 좌표로 넘어가기 위해서 원상복구
    for coord in candidate:
        graph[coord[0]][coord[1]] = 'X'

# print(cnt)
if find == True:
    print("YES")
else:
    print("NO")