
def squares(N): 
    for i in range(1, N+1): 
        yield i*i 

for i in squares(5): 
    print(i)