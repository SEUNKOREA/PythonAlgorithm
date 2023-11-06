n = input()

mid = len(n)//2

left = [int(i) for i in n[:mid]]
right = [int(i) for i in n[mid:]]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
