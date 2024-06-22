# hirechical inheritance
class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass

# hybrid inheritance

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C)
    pass