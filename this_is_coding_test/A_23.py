n = int(input())
data = []

for _ in range(n):
    name, kor, eng, mat = input().split()
    data.append((name, int(kor), int(eng), int(mat)))

data.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(data[i][0]) 