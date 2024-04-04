"""
이코테 구현 예제 4-2. 시각
"""

n = int(input())
answer = 0
for hour in range(n+1):
    for min in range(60):
        for sec in range(60):
            time = str(hour) + str(min) + str(sec)
            if '3' in time:
                answer += 1
print(answer)