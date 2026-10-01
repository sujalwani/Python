age = int(input("Enter your age: "))

#If elif else ladder 

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

if(age>=18):
    print("Yes")
else:
    print("No")
