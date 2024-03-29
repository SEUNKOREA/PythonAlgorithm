import sys

input = sys.stdin.readline

# 집의 개수(n), 공유기의 개수(c)
n, c = map(int, input().split())
# 집의 좌표
array = [int(input()) for _ in range(n)]

# 집의 위치 오름차순
array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2

    # 실제 공유기 설치
    value = array[0]
    cnt = 1
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)