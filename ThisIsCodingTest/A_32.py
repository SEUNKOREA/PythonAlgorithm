n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array = array[::-1]

for i in range(1, n):
    for j in range(len(array[i])):
        value = -1
        for temp in [j, j+1]:
            if value <= array[i-1][temp]:
                value = array[i-1][temp]
        array[i][j] += value

print(array[-1][0])
