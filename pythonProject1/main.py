number = int(input())
word = list(str(number))

n = len(word)
count = 0
for pos in range(n):
    value = word[pos]
    x = word.count(str(pos))
    if str(x) == str(pos):
        count += 1
print(count)