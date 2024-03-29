# 반복적으로 구현한 n!
def iterative_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n-1)

print(f"반복적으로 구현한 팩토리얼: {iterative_factorial(5)}")
print(f"재귀적으로 구현한 팩토리얼: {recursive_factorial(5)}")
