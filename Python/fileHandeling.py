# file = open('test.txt', mode = 'r')

# data = file.readline()
# print(data)
# file.close()

# with open('test.txt', mode = 'r') as file:
#   data = file.readline()
#   print(data)

# with open("test2.txt", "w") as file:
#     file.write("Hello World!")
#     file.writelines(["Hello World!",'\nThis is new line'])
# try:
#   with open("test2.txt", "a") as file:
#     file.write("Hello World!")
#     file.writelines(["\nHello World!",'\nThis is new line'])
# except FileNotFoundError as e:
#   print (e, "\nFile not found.")

# try:
#   with open("sample/test3.txt", "a") as file:
#     file.write("Hello World!")
#     file.writelines(["\nHello World!",'\nThis is new line'])
# except FileNotFoundError as e:
#   print (e, "\nFile not found.")

# with open('test.txt', 'r') as file:
#     print(file.read(44))
#     data = file.readline(2)

#     for x in data:
#         print(x)
# 
# import random
# f = open("petnames.txt", "r")
# f_content = f.read()
# f_content_list = f_content.split("\n")
# print(random.choice(f_content_list))

import random
f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))
