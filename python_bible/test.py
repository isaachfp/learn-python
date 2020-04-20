#!/usr/bin/python3
def defArgFunc(empname,emprole="Manager"):
    print("Emp Name: ",empname)
    print("Emp Role: ",emprole)
    return;

def varLengthFunc(*varvallist):
    print("The output is: ")
    for varval in varvallist:
        print(varval)
    return;

print("Single value")
varLengthFunc(55)
print("Multiple values")
varLengthFunc(50,60,70,80)
print("Using default value")
defArgFunc(empname="Nick")
print("********************")
print("Overwriting default value")
defArgFunc(empname="Tom",emprole="CEO")
'''
for number in range(5):
    print(number,"Thank you")
languages=["R","Python","Scala","Java","Julia"]
for index in range(len(languages)):
    print("Current language is:",languages[index])
'''