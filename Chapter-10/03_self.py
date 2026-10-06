class Employee :
    language = "JS" #this is a class attribute 
    salary = 100000

    def getinfo(self):
        print(f"Language is {self.language}. The salary is {self.salary}.")

    #There is no use of self . instant of using self we use the static method
    @staticmethod
    def greet():
        print("Good Morning.")

#sujal is a object .
sujal = Employee()
sujal.language="PY"
sujal.greet()
sujal.getinfo()

