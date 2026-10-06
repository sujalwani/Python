class Employee :
    language = "JS" #this is a class attribute 
    salary = 100000

#sujal is a object .
sujal = Employee()
sujal.name  = "Sujal Wani" #this is an instance attribute 
print(sujal.name ,sujal.salary , sujal.language)

yash = Employee()
yash.name = "Yash 100kar"
print(yash.name,yash.language , yash.salary)

#Here name is instannce attribute and salary and language are class attributes as they directly bbelonng to the class . 