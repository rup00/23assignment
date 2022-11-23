def valid(f): 
  
    def wrapper(a, b, c): 
  
        if (a + b <= c) or (a + c <= b) or (b + c <= a): 
            print("Perimeter can't be computed") 
          
        else: 
            f(a, b, c) 
   
    return wrapper 
  
@valid 
def triangle_perimeter(a, b, c): 
    print(a + b + c) 
  
a, b, c = 3, 4, 5
triangle_perimeter(a, b, c) 
  
a, b, c = 5, 1, 2
triangle_perimeter(a, b, c)