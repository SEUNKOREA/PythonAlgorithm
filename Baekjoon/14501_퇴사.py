n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

d = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    ### 가능여부 확인
    if n-i >= array[i][0]:
        d[i] = max(array[i][1]+d[i+array[i][0]], d[i+1])
    else:
        d[i] = d[i+1]

print(d[0])