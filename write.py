# file = open("demo.txt","w")
# file_data = file.write("i am learn java from online")

# file = open("demo.txt","a")
# file.write("\n hello my name is manisha")

# print(type(file_data))
# print(file_data)


with open("demo.txt","a") as file:
    # print(file.write("hiiiii"))
    print(file.writelines("my name is manisha"))