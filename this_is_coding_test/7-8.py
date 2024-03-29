import sys

input = sys.stdin.readline

# 떡의개수(n), 요청한 떡의 길이(m)
n, m = map(int, input().split())
# 떡의 개별 높이
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    
    # 잘라진 떡의 양 계산
    for x in array:
        if x > mid:
            total += x - mid
    
    # 떡의 양이 부족한 경우 
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우
    else:
        result = mid
        start = mid + 1

print(result)




