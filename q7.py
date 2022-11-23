def Fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i in Fibonacci():
    print(i)