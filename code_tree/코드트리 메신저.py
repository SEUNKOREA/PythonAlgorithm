import copy
import sys
sys.stdin = open('input.txt', 'r')

def find_parent(parent, x, power, c, answer):
    if x == c:
        if not status[x]:
            answer = 0
        else:
            print(f"x={x}")
            answer += 1
    if power == 0:
        return x, answer
    if parent[x] != x and status[x]:
        return find_parent(parent, parent[x], power-1, c, answer)
    return x, answer


N, Q = map(int, input().split()) # 채팅방의수, 명령의 개수
parent = [0]
authority = [0]
status = [True for _ in range(N+1)] # 알림망 설정 기능 True=>ON

# Q개의 명령을 차례로 입력받음
for i in range(Q):
    print(f"{i}번째 명령")
    command = list(map(int, input().split()))
    if i == 0: # 첫번째 명령은 항상 사내 메신저 준비 명령
        _, parent_tmp, authority_tmp = command[0], command[1:N+1], command[N+1: ]
        parent += parent_tmp # 인덱스와 노드번호를 맞추기 위해서 0번 노드의 부모는 0으로 설정
        authority += authority_tmp # 인덱스와 노드번호를 맞추기 위해서 0번 노드의 power는 0으로 설정

    else:
        cmd = command[0]
        if cmd == 200: # 알림망 설정 ON/OFF
            c = command[1]
            if status[c]:
                status[c] = False
            else:
                status[c] = True

        elif cmd == 300: # 권한 세기 변경
            c, power = command[1], command[2]
            authority[c] = power

        elif cmd == 400: # 부모 채팅방 교환
            c1, c2 = command[1], command[2]
            parent[c1], parent[c2] = parent[c2], parent[c1]

        elif cmd == 500: # 알림받을 수 있는 채팅방 조회
            c = command[1]
            answer = 0
            # 우선순위에 따라서 도달할 수 있는 parent값 업데이트
            ans = copy.deepcopy(parent)
            for j in range(1, N + 1):
                power = authority[j]
                if power == 0:
                    ans[j] = j
                else:
                    print(j)
                    ans[j], tmp = find_parent(ans, j, power, c, 0)
                    if c != j:
                        answer += tmp
            print(f"ans: {ans}")
            print(answer)

    print(f"parent: {parent}")
    print(f"status: {status}")
    print(f"authority: {authority}")
    print()








