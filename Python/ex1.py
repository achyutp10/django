# Use control flow and loops to solve a problem


num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]
num_list.sort()
count = 0
for idx, i in enumerate(num_list):
    if i == 36:
        print("Number found at position: ", idx)
        break
    count += 1
print(i)

# for idx, item in enumerate(favourites):
#     print(idx, item)
