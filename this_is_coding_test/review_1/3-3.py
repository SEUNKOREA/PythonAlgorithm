"""
이코테 그리디 실전3. 숫자카드 게임
"""
# min() 함수를 이용하는 답안 예시
answer = 0
n, m = map(int, input().split())
for _ in range(n):
    data = list(map(int, input().split()))
    answer = max(answer, min(data))
print(answer)