## 이코테 <시각> p.113
## CKPT
"""
시각을 구현하는 법 > 시간, 분, 초 나눠서 3중반복문 돌리기
"""


n = int(input())

answer = 0
for hour in range(0, n+1):
    for min in range(60):
        for sec in range(60):
            time = str(hour)+str(min)+str(sec)
            if '3' in time:
                answer += 1
print(answer)
