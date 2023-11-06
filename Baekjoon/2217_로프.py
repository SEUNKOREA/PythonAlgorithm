n = int(input())
rope = [int(input()) for _ in range(n)]

rope.sort()

answer = 0
for i in range(len(rope)):
    num_use = len(rope) - i
    max_weight = rope[i] * num_use
    if answer < max_weight:
        answer = max_weight
print(answer)
