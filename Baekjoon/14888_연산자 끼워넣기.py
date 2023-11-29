from itertools import permutations
from collections import deque

n = int(input())
number_list_cp = deque(map(int, input().split()))
n_plus, n_minus, n_mul, n_div = map(int, input().split())
operator = "+" * n_plus + "-" * n_minus + "*" * n_mul + "/" * n_div
operator_candidates = set(permutations(operator, n-1))

min = 9876543210
max = -987654321

for operator_list in operator_candidates:
    number_list = number_list_cp.copy()
    answer = number_list.popleft()
    # log = str(answer)
    operator_list = deque(operator_list)
    while number_list:
        temp = number_list.popleft()
        if operator_list:
            op = operator_list.popleft()
            #log += op
        #log += str(temp)
        if op == '+':
            answer += temp
        elif op == '-':
            answer -= temp
        elif op == "*":
            answer *= temp
        elif op == "/":
            if answer < 0:
                answer = (-1 * answer) // temp
                answer *= (-1)
            else:
                answer //= temp
    # log += "="
    # log += str(answer)
    if answer > max:
        max = answer
    if answer < min:
        min = answer
    # print(log)

print(max)
print(min)