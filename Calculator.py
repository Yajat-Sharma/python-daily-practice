def add(a,b):
    return a + b
def sub(a,b) : 
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return "Cannot divide by zero" if b == 0 else a / b

a = int(input("Enter first number:-"))
b = int(input("Enter second number:- "))
c = int(input('''What task should it do
          1 - add
          2 - sub 
          3 - mul
          4 - div :- 
          '''))

ops = {1: add, 2: sub, 3:mul, 4:div}
if c in ops:
    print(ops[c](a,b))
else:
    print("Invaild choice")



