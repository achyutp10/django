# sample = {1: "Coffee", 2: "Tea", 3: "Juice"}
# print(sample[1])
# sample[2] = "Abc"
# print(sample)

# del sample[3]
# print(sample)

my_d = {1: "Test", "Name": "Jim"}
# print(type(my_d))
# print(my_d["Name"])
# print(my_d[1])
# my_d[2] = "Test 2"
# print(my_d)
# del my_d[1]

for x in my_d:
    print(x)
for key, value in my_d.items():
    print(str(key) + " : " + str(value))
