def multi_table(number):
    i = 1
    test = ""
    while i<11:
        num = number*i
        test = test+ f"{number} * {i} = {num}\n"
        
        i += 1
    return test[:-1]

print(multi_table(5))






# def multi_table(number):
#     if 1 <=number <=10:
#         table =[]
#         for i in range(1,10):
#             table.append(f"{number}*{i}={number*i}")
#         return table
# print(multi_table(5))            