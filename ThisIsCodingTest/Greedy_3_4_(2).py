n, k = map(int, input().split())
result = 0

while True:
    # n보다 작은 최대 배수
    target = (n // k) * k 
    # (n - n보다 작은 최대 배수) -> 1을 빼는 횟수
    result += (n - target)
    # n을 target값으로 업데이트
    n = target

    if n < k: # n이 k보다 클 때만 나누는 것이 의미있음(그렇지 않으면 -1 연산으로만 1을 만들 수 있다.)
        break
    
    result += 1
    n //= k

result += (n-1)
print(result)