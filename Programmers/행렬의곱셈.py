A = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
B = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

answer = []
for A_row in A:
    ans = []
    for B_col in zip(*B):
        s = 0
        for a, b in zip(A_row, B_col):
            s += (a * b)
        ans.append(s)
    answer.append(ans)

print(answer)