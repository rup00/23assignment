
def prime_numbers():
    num = 2
    while True:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            yield num
        num += 1

for num in prime_numbers():
    if num > 100:
         break
    print(num)