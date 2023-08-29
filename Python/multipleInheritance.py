# class A:
#     pass
# class B(A):
#     pass

# class A:
#    a = 1
   
# class B(A):
#    b = 2
   
# # class C(A, B):
# class C(B):
#    pass

# c = C()
# print(c.a)

# # issubclass(class A, class B)

# print(issubclass(A,B))
# print(issubclass(B,A))

# class Fruit():
#     def __init__(self, fruit):
#         print('Fruit type: ', fruit)


# class FruitFlavour(Fruit):
#     def __init__(self):
#         super().__init__('Apple')
#         print('Apple is sweet')

# apple = FruitFlavour()

class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a)

print("Instantiating B..")
b = B(a)
print(a)
