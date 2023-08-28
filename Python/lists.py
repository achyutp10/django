list1 = [1, 2, 3, 4, 5]
list2 = ["a", "B", "C"]
list3 = ["Hello", 1, True, 40.22]

# print(list1[2])

# list4 = [1, [2, 3, 4], 5, 6]

# print(*list1)

for x in list1:
    print(x)


list1.insert(len(list1) - 1, 6)
list1.append(7)
list1.extend([8, 9])
list1.pop(4)
del list1[2]
print(list1, sep=" ")
