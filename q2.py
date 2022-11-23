def odd_natural_number(n):
    for i in range(1, n*2, 2):
        yield i

for x in odd_natural_number(5):
    print(x)