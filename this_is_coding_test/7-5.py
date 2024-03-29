n = int(input())
stock = list(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

# 매장에 있는 부품번호 오름차순 정렬
stock.sort()

# 이진탐색 코드
def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        
        if stock[mid] == target:
            return True

        if stock[mid] < target:
            start = mid + 1
        elif stock[mid] > target:
            end = mid - 1
    
    return False

for i in range(m):
    target = request[i]
    if binary_search(0, n-1, target):
        print("yes", end=' ')
    else:
        print("no", end=" ")