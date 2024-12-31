# Write a program to take 5 number as input and print which one is positive and which one is negative.

num = 1
while num<=5:
    number = int(input("enter a number :"))
    if number>0:
        print(number,"positive number")
    elif number<0:
        print(number,"negative number")
    else:
        print("zero")

    num += 1       
