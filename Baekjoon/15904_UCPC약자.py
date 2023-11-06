words = input().split()
words = [word for word in words if word.islower()==False]
words = ''.join(words)

answer = ['U','C','P','C']
answer.reverse()

cnt = 0

for w in words:
    if w == answer[-1]:
        answer.pop()
        cnt += 1
        if cnt == 4:
            print("I love UCPC")
            break
if cnt != 4:
    print("I hate UCPC")