string = input()

length = len(string)

left = string[:length//2]
right = string[length//2:]

left_sum = 0
right_sum = 0

for l in left:
    left_sum += int(l)
for r in right:
    right_sum += int(r)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")