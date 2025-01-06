# Write a program that take number from user and display sum of Numbers Until user put a negetive value

i = 1
sum = 0
while i <= 10:
    number = int(input("enter positive number :"))

    if number > 0:
        sum += number
    i += 1

print("total of numbers are=",sum)    

