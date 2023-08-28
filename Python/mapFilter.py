menu = ['Abc', 'cDef', 'cGhi', 'Jkl', 'Mno', 'Pqr', 'Stu', 'Vwxyz']

def findFood(coffee):
    if coffee[0] == 'c':
        return coffee

# map_coffee = map(findFood, menu)
# print(map_coffee)
# for x in map_coffee:
#     print(x)

filter_coffee = filter(findFood, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)