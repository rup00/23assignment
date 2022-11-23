s = {1,2,3,4,5}
i = iter(s)

while True:
    try:
        print(next(i))
    except StopIteration:
        break