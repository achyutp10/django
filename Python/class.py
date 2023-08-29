# class MyClass:
#     a = 5
#     print('Hello')
#     def hello(self):
#         print('Hello world')
# myc = MyClass()
# print(MyClass.a)
# print(myc.a)
# print(myc.hello())

class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
house = House()
print(house.num_rooms)
print(House.num_rooms)

house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)