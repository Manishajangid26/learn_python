# write a program to take a int an input and print  if the number is prime or not.

num = int(input("enter a number"))

for x in range (2 , num):
    if num % x == 0:
        temp_var = False
        break
    else:
        temp_var = True

if temp_var:
        print("prime")
else:
        print("not prime")           


 




























# num = int(input("enter a no :"))
# if num>1:
#     for i in range(2 , num):
#         if(num % i) == 0:
#             print(num , "no is prime")
#         else:
#             print(num , "no is not prime")    
