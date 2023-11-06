n = int(input())
data = list(map(int, input().split()))

data.sort() # 걸리는 시간 오름차순 정렬

answer = 0

for i in range(n):
    answer += data[i] * (n-i)

print(answer)
