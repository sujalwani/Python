def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a = int(input("Enter any number : "))
b = int(input("Enter any number : "))
c = int(input("Enter any number : "))

greatest = greatest(a,b,c) 
print(f"Greatest from {a,b,c} is {greatest}")