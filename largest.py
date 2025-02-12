# 4. Write a program that take 10 number from user and display which is the largest number.

i = 0
largest = int(input("enter a number :"))
while i<2:
    num = int(input("enter number :"))
    if(num>largest):
        largest = num
    i +=1
print("The largest no is :",largest)

