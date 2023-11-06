n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [i for i in range(max(data)+1)]

start = 0
end = max(data)+1

while start <= end:
    mid = (start + end) // 2
    remain = []
    for x in data:
        if x < array[mid]: remain.append(0)
        else: remain.append(x-array[mid]) 
    if sum(remain) == m:
        print(array[mid])
        break
    elif sum(remain) > m:
        start = mid+1
    else:
        end = mid - 1
    