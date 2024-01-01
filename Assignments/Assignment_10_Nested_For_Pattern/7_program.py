"""
Program7 : Row = 4
$ = $ =
$ = $ =
$ = $ =
$ = $ =
"""
Doller = 36
Equal = 61
for i in range(4):
    for j in range(4):
        if j % 2 == 0:
            print(chr(Doller), end = " ")

        else:
            print(chr(Equal), end = " ")

    print()
