from itertools import combinations
from collections import deque

n = int(input())

graph = []

teachers = []
students = []
empty = []

for i in range(n):
    graph.append(input().split())
    for j in range(n):
        if graph[i][j] == "T":
            teachers.append((i, j))
        elif graph[i][j] == "S":
            students.append((i, j))
        else:
            empty.append((i, j))

candidates = combinations(empty, 3)

def watch(i, x, y):
    # 위쪽 방향으로 감시
    if i == 0:
        while x >= 0:
            if temp[x][y] == 'S':
                return True
            elif temp[x][y] == 'O':
                return False
            x -= 1
    # 아래쪽 방향으로 감시 
    elif i == 1:
        while x < n:
            if temp[x][y] == 'S':
                return True
            elif temp[x][y] == 'O':
                return False
            x += 1
    # 오른쪽 방향으로 감시
    elif i == 2:
        while y < n:
            if temp[x][y] == 'S':
                return True
            elif temp[x][y] == 'O':
                return False
            y += 1
    # 왼쪽 방향으로 감시
    elif i == 3:
        while y >= 0:
            if temp[x][y] == 'S':
                return True
            elif temp[x][y] == 'O':
                return False
            y -= 1
    return False


def process():
    # 모든 선생님의 위치를 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(i, x, y):
                return True
    return False

flag = False
for candidate in candidates:
    # candidate = [(1, 1), (2, 2), (0, 3)]
    
    # 그래프 복사
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = graph[i][j]
    
    # 장애물 세우기
    for (x, y) in candidate:
        temp[x][y] = 'O'
    
    if not process():
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")
    


