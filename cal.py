def add(a , b):
    print("add :",a+b)


def sub(a , b):
    print("sub :",a-b)

def mul(a , b):
    print("multi :",a*b)   

num1 = int(input("enter a no :"))     
num2 = int(input("enter a no :"))     
op = input("+ , = , *")
if op == "+" :
    add(num1,num2)
elif op == "-":
    sub(num1,num2)
else:
    mul(num1,num2)




    