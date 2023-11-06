# 계수 정렬 방식으로 해결하기
n = int(input())
products = list(map(int, input().split()))

m = int(input())
wants = list(map(int, input().split()))

counts = [0] * (max(products)+1)

for product in products:
    counts[product] += 1

for want in wants:
    if counts[want] == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')


# 답안
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')