num1 = float(input("enter a number"))
num2 = float(input("enter a number"))
operator = input("enter an operator(+ - * /):")
# if  operator=="+":
#     print(num1+num2)
# elif operator == "-":
#     print(num1-num2)
# elif operator == "*":
#     print(num1*num2)
# elif operator == "/":
#     print(num1/num2)

# else :
#     print("invalid operaror")



if  operator=="+":
    print(num1+num2)
if operator == "-":
    print(num1-num2)
if operator == "*":
    print(num1*num2)
if operator == "/":
    print(num1/num2)
if operator not in '+ - * /' : 
    print("invalid operator")  


       