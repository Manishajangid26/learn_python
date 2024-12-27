#write a program that take a number ar input and display by 3 if the number is divisible by 3 
#and display 5 id number is divisible by 5 and display by both if number is divisible by both 3 and 5.





num = int(input("enter any no :"))
if(num%3==0 and num%5==0):
    print("number is divisible by both 3 and 5")        

elif(num%5==0):
    print("number is divisible by 5")
elif(num%3==0):
    print("number is divisible by 3")