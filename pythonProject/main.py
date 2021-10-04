input1 = 5
input2 = [2849, 1620, 705, 1, 30]
avg = sum(input2) / input1
dif = 0
for i in range(input1):
    if avg > input2[i]:
        dif += abs(avg - input2[i])
print(int(dif))
