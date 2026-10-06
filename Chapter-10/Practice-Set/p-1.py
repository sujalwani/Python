class Programmer :
    company = "Microsoft"

    def __init__(self,name,salary,pincode):
        self.name = name 
        self.salary = salary
        self.pincode = pincode

p = Programmer("Sujal",4200000,442301)
print(p.name,p.salary,p.pincode,p.company)
r = Programmer("Rohit",7800000,45678)
print(r.name,r.salary,r.pincode,r.company)