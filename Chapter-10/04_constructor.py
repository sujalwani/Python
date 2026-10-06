class Employee :
    language = "JS" 
    salary = 100000

    def __init__(self,name,salary,language): #dunder method which is automatically call
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object .")

    def getinfo(self):
        print(f"Language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Morning.")

sujal = Employee("Sujal",120000,"PY")
# sujal.name = "Sujal"
print(sujal.name ,sujal.salary,sujal.language)


