#!/usr/bin/python3
class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print("Hello!")

#output 10
print(MyClass.a)

#output function Myclass(func)
print(MyClass.func)

# doc string
print(MyClass.__doc__)