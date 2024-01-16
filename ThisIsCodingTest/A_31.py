def process(n, m, data):
    answer = 0

    array = [[] for _ in range(m)]
    for i in range(len(data)):
        array[i%4].append(data[i])

    for i in range(1, m):
        for j in range(n):
            value = -1
            for t in [j-1, j, j+1]:
                if 0 <= t < n:
                    if value < array[i-1][t]:
                        value = array[i-1][t]
            array[i][j] += value
    
    return max(array[-1])

# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     data = list(map(int, input().split()))
#     print(process(n, m, data))

process(3, 4, [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7])
process(4, 4, [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2])
