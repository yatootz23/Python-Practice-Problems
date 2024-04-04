n = 20
num = n * (n-1)
while (n > 1):
    if(num % n != 0):
        print(num, n, num % n)
        num *= n
    n -= 1
print(num)