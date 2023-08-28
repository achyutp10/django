def typeCasting():
    print(len("Hello"))
    print(str(55))
    print(int("55"))
    print(float(55))
    print(10 == 10)
    print(10 == 10.00)
    print(10 + 10.00)
    print(type(10 + 10.00))


typeCasting()

user_num_1 = input("First number is: ")
user_num_2 = input("Second number is: ")
user_sum = user_num_1 + user_num_2
print(user_sum)

# This is error cannot concatenate string and a float
# num_1 = input('First number is: ')
# num_2 = input('Second number is: ')
# user_sum = float(num_1) + float(num_2)
# print("The sum of: " + num_1 + " and " + num_2 + " is " + user_sum)

num_1 = input("First number is: ")
num_2 = input("Second number is: ")
user_sum = float(num_1) + float(num_2)
print("The sum of: " + str(num_1) + " and " + str(num_2) + " is " + str(user_sum))
