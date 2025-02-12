file1 = file2 = file3 = ""
with open("files/file")as file1:
    file1 = file1.readlines()

with open("files/file2")as file2:
    file2 = file2.readlines()

with open("files/file3")as file3:
    file3 = file3.readlines()

with open("files/file4")as file4:
    file4.writelines(file1)          
    file4.writelines(file2)          
    file4.writelines(file3)          