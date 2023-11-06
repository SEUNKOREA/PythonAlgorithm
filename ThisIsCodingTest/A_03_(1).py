# 내 풀이
data = input()

count = 1
temp = data[0]
for i in range(1, len(data)):
    if temp != data[i]:
        temp = data[i]
        count += 1

if count % 2 == 1:
    print((count - 1)//2)
else:
    print(count//2)

