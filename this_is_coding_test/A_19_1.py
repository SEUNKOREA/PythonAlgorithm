from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
data = list(map(int, input().split()))

operators = []
for i in range(4):
    for op_num in range(data[i]):
        if i == 0:
            operators.append("+")
        elif i == 1:
            operators.append("-")
        elif i == 2:
            operators.append("*")
        else:
            operators.append("/")

candidates = permutations(operators, n-1)
candidates = set(candidates)

final_max = -1000000001
final_min = 1000000001

for candidate in candidates:
    result = numbers[0]
    for i in range(n-1):
        num = numbers[i+1]
        if candidate[i] == '+':
            result += num
        elif candidate[i] == '-':
            result -= num
        elif candidate[i] == '*':
            result *= num
        elif candidate[i] == '/':
            if result < 0:
                result *= (-1)
                result //= num
                result *= (-1)
            else:
                result //= num
    final_max = max(result, final_max)
    final_min = min(result, final_min)

print(final_max)
print(final_min)