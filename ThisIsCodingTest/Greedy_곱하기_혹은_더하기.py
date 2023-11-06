# 곱하기 혹은 더하기
string = "567"
result = 0

for idx, value in enumerate(string):
    if idx == 0 or value == '0' or value == '1' or result == 0:
        result += int(value)
    else:
        result *= int(value)

print(result)

### 다른 풀이 ###
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)