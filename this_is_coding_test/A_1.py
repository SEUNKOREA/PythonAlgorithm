n = int(input())
fears = list(map(int, input().split()))

# 공포도 오름차순 정렬
fears.sort()

# 총 그룹수
answer = 0
# 현재 그룹에 포함된 인원 수
cnt = 0

for fear in fears:
    cnt += 1
    if cnt >= fear:
        answer += 1
        cnt = 0

print(answer)