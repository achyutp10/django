# class A:
#     def a(self):
#         return 'Function inside A'
    
# class B:
#     def a(self):
#         return 'Function inside B'

# class C(B,A):
#     pass

# c = C()
# print(c.a())

# class A:
#     def b(self):
#         return "Function inside A"

# class B:
#     def b(self):
#         return "Function inside B"

# class C(A, B):
#     def b(self):
#         return "Function inside C"
#     pass

# class D(C):
#     pass

# d = D()
# print(d.b())

class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro())