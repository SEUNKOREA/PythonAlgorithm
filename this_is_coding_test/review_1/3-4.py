"""
이코테 그리디 실전3. 숫자카드 게임
"""
# 2중 반복문 구조를 이용하는 답안
answer = 0
n, m = map(int, input().split())
for i in range(n):
    data = list(map(int, input().split()))
    row_min = 10001
    for j in range(m):
        if data[j] < row_min:
            row_min = data[j]
    answer = max(answer, row_min)
print(answer)