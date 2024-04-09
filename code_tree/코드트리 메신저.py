MAX_N = 8+1
MAX_D = 22

a, p, val = [0] * MAX_N, [0] * MAX_N, [0] * MAX_N
noti = [False] * MAX_N
nx = [[0 for _ in range(MAX_D)] for _ in range(MAX_N)]

def init(inputs):
    global n, a, p, val, nx
    # 부모 채팅 정보를 입력받습니다.
    for i in range(1, n+1):
        p[i] = inputs[i]
    # 권한 정보를 입력받습니다.
    for i in range(1, n+1):
        a[i] = inputs[i+n]
        if a[i] > 20: # 채팅의 권한이 20을 초과하는 경우 20으로 제한합니다.
            a[i] = 20

    # nx 배열과 val 값을 초기화
    for i in range(1, n+1):
        cur = i     # 현재노드번호
        x = a[i]    # 현재노드의 권한
        # 상위채팅으로 이동하며 nx와 val 값을 갱신합니다.
        while p[cur] and x: # 현재노드의 부모와 권한이 둘 다 0이 아닌경우
            cur = p[cur]    # 현재노드의 부모노드
            x -= 1          # 부모노드로 하나 올라가면 권한의 세기가 하나 떨어진다.
            if x:           # 권한이 0이 아니라면
                nx[cur][x] += 1 # 부모노드는
            val[cur] += 1
    print(p)
    print(a)
    for nnx in nx:
        print(nnx)
    print()
    print(val)

import sys
sys.stdin = open('input.txt', 'r')

n, q = map(int, input().split())
for _ in range(q):
    inputs = list(map(int, input().split()))
    query = inputs[0]
    if query == 100:
        init(inputs)