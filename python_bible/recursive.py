#!/usr/bin/python3
def main():
    num = int(input("Enter a non-negative integer:\n"))
    fact = factorial(num)
    print("The factorial of",num,"is",fact)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

main()

#Using recursion for generators
def crazy(min_):
    yield min_
    g=crazy(min_+1)
    while True:
        yield next(g)
        yield min_

i = crazy(1)
#print(i)