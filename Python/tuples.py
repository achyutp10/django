# cannot be changed // immuatable datatype

my_tuples = (1, "strings", 4.5, True)
print(my_tuples[1])
print(type(my_tuples[1]))
print(my_tuples.count("strings"))
print(my_tuples.index(4.5))

for x in my_tuples:
    print(x)
