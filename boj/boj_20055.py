"""
BOJ 20055 컨베이어 벨트 위의 로봇
출처: https://www.acmicpc.net/problem/20055
"""
import sys
sys.stdin = open('input.txt', 'r')

class Belt():
    def __init__(self, power):
        self.power = power
        self.robot = 0

N, K = map(int, input().split())
powers = list(map(int, input().split()))

belt = []
for i in range(2*N):
    belt.append(Belt(powers[i]))

time = 0

lst = []
cnt = 0
while True:
    time += 1


    # [1] 벨트가 각 칸 위에 있는 로봇과 함께 회전한다.
    # belt = [belt[-1]] + belt[0:-1]
    belt.insert(0, belt.pop())
    if belt[N-1].robot != 0:
        belt[N-1].robot = 0

    # [2] 가장 먼저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 이동
    for i in range(N-2, -1, -1):
        if belt[i].robot != 0: # 로봇이 위치해있다면
            # 다음 칸으로 이동할 수 있는지 확인
            if belt[i+1].robot == 0 and belt[i+1].power > 0:
                belt[i].robot = 0
                belt[i + 1].robot = 1
                belt[i + 1].power -= 1
                if belt[i + 1].power == 0:
                    cnt += 1

            if i+1 == N-1:
                belt[i + 1].robot = 0

    # [3] 0번째 벨트의 내구도가 0이 아니라면 로봇을 올린다.
    if belt[0].power != 0:
        belt[0].robot = 1
        belt[0].power -= 1
        if belt[0].power == 0:
            cnt += 1

    # print(time, end=' ')
    # for i in range(2*N):
    #     print(f"{(belt[i].power, belt[i].robot)}", end=' ')
    # print()

    # cnt = 0
    # for i in range(2*N):
    #     if belt[i].power == 0:
    #         cnt += 1
    if cnt >= K:
        break


print(time)


