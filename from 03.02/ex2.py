x=int(input("Enter the value to caculator the factory: "))
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
print (fact(x))