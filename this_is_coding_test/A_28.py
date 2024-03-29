import sys
input = sys.stdin.readline

# 데이터의 개수
n = int(input())
# 수열
array = list(map(int, input().split()))

def bisect_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 고정점인지 확인
        if array[mid] == mid:
            return mid
        
        elif array[mid] > mid:
            end = mid - 1
        
        else:
            start = mid + 1
    
    return False

result = bisect_search(array, 0, n-1)

if result:
    print(result)
else:
    print(-1)