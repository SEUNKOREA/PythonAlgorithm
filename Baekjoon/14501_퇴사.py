from itertools import product

n = int(input())
data = [] # (time, price, None)
for _ in range(n):
    temp = list(map(int, input().split()))
    temp.append(None)
    data.append(temp)

first = data[:]
first[0][2] = True
second = data[:]
second[0][2] = False

for array in [first, second]:
    for i in range(n):
        if array[i][2] == None:
            if array[i][0] <= n-i:
                data[i][2] = True
                answer += data[i][1]
                for j in range(i+1, i+1+data[i][0]-1):
                    data[j][2] = False
            else:
                data[i][2] = False
                print("pass")
        
        for i in range(n):
            print(data[i])
        print()

print(answer)