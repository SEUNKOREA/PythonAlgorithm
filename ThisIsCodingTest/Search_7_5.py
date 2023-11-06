def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
products = list(map(int, input().split()))

m = int(input())
wants = list(map(int, input().split()))

products.sort()
wants.sort()

for i in range(m):
    result = binary_search(products, wants[i], 0, n-1)
    if result == None:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')