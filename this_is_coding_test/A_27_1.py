import sys

input = sys.stdin.readline

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, start, end, target):
    if start > end:
        return None
    
    mid = (start + end) // 2

    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (array[mid] == target) and (array[mid-1] < target or mid == 0):
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 
    elif (array[mid] >= target):
        return first(array, start, mid-1, target)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 
    else:
        return first(array, mid+1, end, target)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, start, end, target):
    if start > end:
        return None
    
    mid = (start + end) // 2

    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (array[mid] == target) and (mid == len(array)-1 or array[mid+1] > target):
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 
    elif (array[mid] > target):
        return last(array, start, mid-1, target)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 
    else:
        return last(array, mid+1, end, target)

def get_count(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, 0, n-1, x)

    if a == None:
        return 0
    
    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, 0, n-1, x)

    return b-a+1

n, x = map(int, input().split())
data = list(map(int, input().split()))

count = get_count(data, x)

if count == 0:
    print(-1)
else:
    print(count)