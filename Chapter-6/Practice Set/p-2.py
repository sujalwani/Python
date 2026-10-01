marks1 = int(input("Enter marks out of 100 : "))
marks2 = int(input("Enter marks out of 100 : "))
marks3 = int(input("Enter marks out of 100 : "))

total_percentage = (100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print(f"Student is pass with the percentage of {total_percentage}")
else:
    print(f"Student is fail with the percentage of {total_percentage}")