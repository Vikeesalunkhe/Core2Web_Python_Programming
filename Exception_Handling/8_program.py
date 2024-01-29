#exception handling


class B(Exception):
    print("In B")

class C(B):
    print("In c")

class D(C):
    print("in D")

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
