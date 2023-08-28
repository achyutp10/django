myList=[1,2,3]
def add(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl
    # lst.append(item)
    # return lst
nli = add(myList,4)
print(myList)
print(nli)