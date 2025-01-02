# Write a program that take 10 number from user and count how many number are +ve and how many number are -ve.


num = 1
while num<=10:
    number = int(input("enter a number :"))
    if number>0:
        print(number,"positive number")
    else:
        print("negative number")
    
    num += 1       