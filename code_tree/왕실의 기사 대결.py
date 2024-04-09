import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, Q = map(int, input().split())

# 보드판 (빈칸 0, 함정 1, 벽 2)
# 가장 자리를 벽으로 둘러싸서 보드판을 넘어가는 경우를 처리할 수 있도록한다.
board = [[2 for _ in range(N+2)] for _ in range(N+2)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(N):
        board[i][j+1] = data[j]

# 기사정보
knight = {} # 기사의 r,c,h,w,k 정보를 저장하기 위함
init_k = [0] * (M+1) # 답 구할 때 필요한 초기 체력정보 미리 저장
for i in range(1, M+1):
    r, c, h, w, k = map(int, input().split())
    knight[i] = [r, c, h, w, k]
    init_k[i] = k

def push(start, d):
    q = []
    pset = set()
    damage = [0]*(M+1)

    q.append(start)
    pset.add(start)

    while q:
        cur = q.pop(0)
        ci, cj, h, w, k = knight[cur]
        ni = ci + dx[d]
        nj = cj + dy[d]
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if board[i][j] == 2:
                    return
                if board[i][j] == 1:
                    damage[cur] += 1

        for idx in knight:
            if idx in pset: continue
            ti, tj, th, tw, tk = knight[idx]

            if ni <= ti+th-1 and ni+h-1 >= ti and tj <= nj+w-1 and nj <= tj+tw-1:
                q.append(idx)
                pset.add(idx)
    damage[start] = 0

    for idx in pset:
        si, sj, h, w, k = knight[idx]
        if k <= damage[idx]:
            knight.pop(idx)
        else:
            ni = si + dx[d]
            nj = sj + dy[d]
            knight[idx] = [ni, nj, h, w, k-damage[idx]]

# 명령
for _ in range(Q):
    i, d = map(int, input().split())
    if i in knight:
        push(i, d)

ans = 0
for idx in knight:
    ans += init_k[idx] - knight[idx][-1]
print(ans)