class Employee:
    company = "ITC"
    name = "Sujal"
    salary = 120000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language : {self.language}")

class Programeer(Employee , Coder ):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programeer()

b.show()
b.showLanguage()
b.printLanguages()