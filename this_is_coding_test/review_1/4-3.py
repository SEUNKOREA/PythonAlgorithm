"""
이코테 구현 실전2. 왕실의 나이트
"""
input_data = input()

y = ord(input_data[0]) - 97
x = int(input_data[1]) - 1

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

answer = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        answer += 1
print(answer)

