import sys
input = sys.stdin.readline

# 시험장의 개수(n)
n = int(input())
# 각 시험장에 있는 응시자의 수
data = list(map(int, input().split()))
# 총감독관이 감독하는 응시자수(b), 부감독관이 감독하는 응시자수(c)
b, c = map(int, input().split())

# 해당 응시자의 수를 커버하는데 필요한 감독관의 수를 저장할 빈 리스트
array = [-1] * 1000001

# 응시자의 수 중복 제거
data_no_replicate = list(set(data))
# 중복을 제거한 각 응시자 수에 필요한 감독관의 수 계산
for student in data_no_replicate:
    # 총감독관이 감독하는 학생수 제외
    idx = student
    student -= b
    num_supervisor = 1

    # 총감독관으로 커버가 안되는 경우 부감독관
    if student > 0:
        while student > 0:
            student -= c
            num_supervisor += 1
    array[idx] = num_supervisor

answer = 0
for d in data:
    answer += array[d]
print(answer)