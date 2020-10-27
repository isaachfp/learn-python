#!/usr/bin/python3
class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        # o self indica que o objeto passa a si próprio como argumento
        print("Hello!")

#output 10
print(MyClass.a)

#output function Myclass(func)
print(MyClass.func)

# doc string
print(MyClass.__doc__)

ob = MyClass()

ob.func() # é o mesmo que escrever 'MyClass.func(ob)'
print(ob.__doc__)