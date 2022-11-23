def generate_primes(n):
    num = 2
    while n > 0:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            yield num
            n -= 1
        num += 1

for num in generate_primes(10):
    print(num)