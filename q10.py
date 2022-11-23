def gcd(a, b): 
  
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
  

def coprime(a, b): 
      
    if (gcd(a, b) == 1): 
        print("Co-prime") 
    else: 
        print("Not Co-prime") 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
coprime(a, b)