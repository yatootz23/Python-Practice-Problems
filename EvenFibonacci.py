count1 = 0
count2 = 1
temp = 0
sum = 0
while (count2 < 4000000):
    temp = count1
    count1 = count2
    count2 += temp
    if (count2 % 2 == 0):
        sum += count2
print(sum)