string = input()
string = [s for s in string]
string.sort()
sum = 0
text = ''
for s in string:
    try:
        sum += int(s)
    except:
        text += s
text += str(sum)
print(text)
