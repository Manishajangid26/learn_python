# Write a program that take to input from user one is a large string and second input has to be a single 
# character we have to find that character inside the given string but we are not allowed to use anyof the 
# inbuilt methods of string.

# a = input("enter a string :")
# b = input("enter a string :")
# find = 0 

# i = 0
# while i < len(a):
#     if a[i] == b:
#         find += 1
#     i += 1 
# print(fin d)  







a = input("enter a string :")
b = input("enter charector :")


def find_char(string , char):
    count = 0
    for i in string:
        if i == b:
            count += 1
    print(count)

result = find_char(a ,b)
print(find_char)            





















# if a[0]==b:
#     find += 1
# if a[1] == b:
#     find += 1
# if a[2] == b:
#     find += 1
# if a[3] == b:
#     find += 1
# if a[4] == b:
#     find += 1
               