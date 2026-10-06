class demo:
    a = 45

sujal=demo() 
print(sujal.a)  #print class attribute because instance attribute is not present 
sujal.a = 0     #instance attribute is set 
print(sujal.a)  #prints the instance attribute because instancce attribute is present 
print(demo.a)   #prints the class attribute
