def sumofn(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return n+sumofn(n-1)

n = int(input("Enter any number : "))
sumOfN = sumofn(n)
print(sumOfN)