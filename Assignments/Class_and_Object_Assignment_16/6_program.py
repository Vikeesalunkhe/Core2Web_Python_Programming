'''
6. WAP for following MRO with flow diagram

[<class '__main__.E'>, <class '__main__.D'>, <class '__main__.B'>, <class
'__main__.C'>, <class '__main__.A'>, <class 'object'>]
'''
class A:
    pass

class C(A):
    pass

class B(C):
    pass

class D(B):
    pass

class E(D):

    pass

Obj = E()

print(E.__mro__)

#O/p (<class '__main__.E'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

