# Write a function reverseNumber() that takes a positive integer as input and returns the reversed number. For example, if the input is 123, the function should return 321.
 

def rev_str(data):
    data = str(data)
    return data[ ::-1 ]


print(rev_str(12345))






















# def reverse_Number(n):
#     reversed_number = 0
#     while n > 0:
#         last_digit = n % 10
#         reversed_number = reversed_number * 10 + last_digit
#         n = n // 10
#     return reversed_number

# number = int(input("enter a no :"))
# print("reverse number :", reverse_Number(number))        





















# def rev_num(n):
#     rev = 0
#     while (n > 0):
#         rem = n % 10
#         rev = (rev * 10) + rem
#         n = n // 10
#     return rev

# n = int(input("enter any no :"))
# rev = rev_num(n)
# print(rev)        

