# multiple if statement 
age = int(input("Enter your age : "))

# If statement no 1
if(age%2==0):
    print("a is even .")
# End of If statement 1

# If statement no 2
if (age>=18):
    print("You are eligible for vote.")
    print("You are eligible for drive a vechile.")
elif(age<0):
    print("You are entering a invalid age.")
elif(age==0):
    print("You are entering a 0 which is not a vaild age .")
else:
    print("You are not eligible for vote.")
    print("You are not eligible for drive a vechile.")
#enf of If Statement 2 
