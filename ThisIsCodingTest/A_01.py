n = int(input())
data = list(map(int, input().split()))
data.sort() # 오름차순 정렬

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

    