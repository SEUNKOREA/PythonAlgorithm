import sys

data = []
while True : 
    l, p, v = map(int, sys.stdin.readline().split())
    if l == 0:
        break
    data.append([l, p, v])

for i in range(len(data)):
    l, p, v = data[i][0], data[i][1], data[i][2]
    answer = (v // p) * l
    if v % p >= l:
        answer += l
    else: 
        answer += v % p
    print(f"Case {i+1}: {answer}")