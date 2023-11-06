n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

# 각 무게가 몇 번 등장했는지 array에 기록한다.
for x in data:
    array[x] += 1

result = 0
for i in range(1, m+1): # 무게가 0은 없기 때문에 1부터 m+1까지 순회
    n -= array[i] # 전체 개수에서 지금 확인하고 있는 데이터의 개수를 빼서 
                  # 지금 확인하고 있는 데이터와 다른 데이터의 개수를 구한다.
    result += array[i] * n # 지금 확인하고 있는 데이터의 개수와 위에서 구한 n을 곱한 값을 누적해 나간다.
    print(f"{array[i]} * {n}")

print(result)
