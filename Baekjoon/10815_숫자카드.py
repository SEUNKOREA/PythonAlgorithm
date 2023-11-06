n = int(input())
num_list = list(map(int, input().split()))
m = int(input())
judge_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1

num_list.sort()

for i in range(m):
    a = binary_search(num_list, judge_list[i], start=0, end=n-1)
    if a == -1:
        print(0, end = ' ')
    else:
        print(1, end = ' ')
    